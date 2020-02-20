(ns tap-generate-docs
  (:require [clojure.data.json :as json]
            [clojure.java.io :as io]
            [clojure.string :as string]
            [clojure.tools.cli :as cli]
            [instaparse.core :as insta])
  (:require [clojure.java.shell :refer [sh]])
  (:import (org.yaml.snakeyaml Yaml
                               DumperOptions
                               DumperOptions$FlowStyle
                               DumperOptions$ScalarStyle)))

(defonce ^:dynamic *interactive* false)

(comment
  (def ^:dynamic *interactive* true)
  )

(defn unary-type?
  [[_ property-json-schema-partial :as property]]
  (or (= {} property-json-schema-partial)
      (string? (property-json-schema-partial "type"))))

(defn type-declaration?
  "A valid type declaration is either a string or a list. Never a map,
   which covers the rest of JSON schema."
  [sub-schema]
  (or (sequential? sub-schema)
      (string? sub-schema)))

(defn converted-unary-type?
  [candidate-converted-unary-type]
  (or (= {} candidate-converted-unary-type)
      (let [name (candidate-converted-unary-type "name")
            type (candidate-converted-unary-type "type")
            description (candidate-converted-unary-type "description")]
        (and (string? name)
             (string? type)
             (string? description)))))

;;; WARNING! Mutual Recursion Incoming!
(declare convert-multiary-type)

(defn convert-object-properties
  [tap-fs schema properties]
  {:pre [(not (type-declaration? (properties "type")))]}
  (sort-by #(get % "name")
           (map (partial convert-multiary-type tap-fs schema) properties)))

(defn convert-array-object-type
  [tap-fs schema property property-json-schema-partial]
  {:pre [(not= "array" (property-json-schema-partial "type"))]}
  (let [item-type (property-json-schema-partial "type")]
    (if (or (= "object" item-type)
            (= ["object"] item-type))
      ;; Consequent
      (convert-object-properties tap-fs schema (property-json-schema-partial "properties"))
      ;; Alternate
      (let [object-properties (convert-object-properties tap-fs schema (property-json-schema-partial "properties"))
            other-properties (if (string? item-type)
                               [item-type]
                               (filter (partial not= "object") item-type))
            converted-other-properties (if (= ["null"] other-properties)
                                         []
                                         [(convert-multiary-type tap-fs
                                                                 schema
                                                                 ["value"
                                                                  (assoc property-json-schema-partial
                                                                         "type"
                                                                         other-properties)])])
            all-properties (sort-by #(% "name") (into object-properties converted-other-properties))]
        (if (< 1 (count (filter #(= "value" (get % "name")) all-properties)))
          object-properties
          all-properties)))))

(defn convert-unary-type
  "unary-type = a property that has a single type notated as a string (i.e.
  not [\"type\"] but \"type\"."
  [tap-fs schema [property-name property-json-schema-partial :as property]]
  {:pre [(unary-type? property)]
   :post [(converted-unary-type? %)]}
  (if (= {} property-json-schema-partial)
    {"name" property-name
     "type" "anything"
     "description" ""}
    (let [base-converted-property {"name" property-name
                                   "type" (if (and (= "string" (property-json-schema-partial "type"))
                                                   (contains? property-json-schema-partial "format"))
                                            (property-json-schema-partial "format")
                                            (property-json-schema-partial "type"))
                                   "description" ""}]
      (cond (= "object" (property-json-schema-partial "type"))
            (if (nil? (property-json-schema-partial "properties"))
              (throw (ex-info "Found object type without properties defined: " {:property-name property-name}))
              (assoc base-converted-property
                     "subattributes"
                     (convert-object-properties tap-fs schema (property-json-schema-partial "properties"))))
            (= "array" (property-json-schema-partial "type"))
            (let [items (property-json-schema-partial "items")
                  item-type (items "type")
                  converted-property (do
                                       (when ((set item-type) "array")
                                         (throw (ex-info (str "Currently cannot handle a type with arrays of arrays. "
                                                              "Discuss how docs output should work if encountered.")
                                                         {:property property})))
                                       (if (or (= "object" item-type)
                                               ((set item-type) "object"))
                                         (convert-array-object-type tap-fs schema property items)
                                         [(convert-multiary-type tap-fs schema ["value" items])]))]
              ;; TODO Log (or verify that it's already logged) dropped value
              (if (empty? converted-property)
                base-converted-property
                (assoc base-converted-property
                       "subattributes"
                       converted-property)))

            (and (= "string" (property-json-schema-partial "type"))
                 (contains? property-json-schema-partial "enum"))
            (if (empty? (property-json-schema-partial "enum"))
              (throw (ex-info "Enum passed without any valid values"
                              {:property property}))
              (assoc base-converted-property
                     "description"
                     (format "Valid values: %s."
                             (string/join ", " (sort (property-json-schema-partial "enum"))))))

            :default
            base-converted-property))))

(defn merge-unary-types
  [converted-prop-1 converted-prop-2]
  {:pre [(converted-unary-type? converted-prop-1)
         (converted-unary-type? converted-prop-2)
         (apply not= (map #(% "type") [converted-prop-1 converted-prop-2]))]}
  (let [base-properties {"name" (converted-prop-1 "name")
                         "type" (string/join ", "
                                             (sort (map #(get % "type")
                                                        [converted-prop-1 converted-prop-2])))
                         "description" ""}]
    (if-let [object-properties (or (converted-prop-1 "subattributes")
                                   (converted-prop-2 "subattributes"))]
      (assoc base-properties "subattributes" object-properties)
      base-properties)))

(defn property->unary-type-properties
  [[property-name property-json-schema-partial :as property]]
  (if (= {} property-json-schema-partial)
    [[property-name {}]]
    (filter #((partial not= "null") (get-in % [1 "type"]))
            (let [type (property-json-schema-partial "type")]
              (if (string? type)
                [property]
                (map (fn [type]
                       [property-name (assoc property-json-schema-partial "type" type)])
                     (property-json-schema-partial "type")))))))

(defn parse-json-schema-reference
  "Parse a json-schema-reference according to
  https://json-schema.org/understanding-json-schema/structuring.html#reuse

  Assumes that external references are defined in <file_name>.json and
  that <file_name>.json is loadable from the same place that the reference
  is defined.

  Also assumes json pointers use only names and slashes."
  [json-schema-reference]
  {:pre [(string? json-schema-reference)]
   :post [(contains? % :file)
          (every? string? (:json-pointer %))]}
  (let [res ((insta/parser "<JSONSCHEMAREFERENCE> = FILE? <ROOT> JSONPOINTER+
                  FILE = #'[-A-Za-z0-9_/]+.json'
                  ROOT = '#'
                  JSONPOINTER = <'/'> #'[A-Za-z0-9_]*'")
             json-schema-reference)
        res (if (insta/failure? res)
              (throw (ex-info "Malformed json-schema-reference"
                              {:json-schema-reference
                               json-schema-reference}))
              res)
        file (filter (comp (partial = :FILE) first) res)
        json-pointer (filter (comp (partial = :JSONPOINTER) first) res)
        json-pointer (if (= [[:JSONPOINTER ""]] json-pointer)
                       []
                       json-pointer)]
    {:file (second (first file))
     :json-pointer (map second json-pointer)}))

(defn read-schema
  [input-json-schema-file]
  (with-open [r (io/reader input-json-schema-file)]
    (json/read r)))

(defn schema-file?
  [input-json-schema-file]
  (try
    (let [json-schema (read-schema input-json-schema-file)]
      (or (and (or (= "object" (json-schema "type"))
                   (= ["null" "object"] (json-schema "type")))
               (contains? json-schema "properties"))
          (println (format "%s is not a valid schema file" input-json-schema-file))))
    (catch Exception e
      (println (format "%s is not valid schema file" input-json-schema-file)))))

(defn load-schema-file
  [{:keys [tap-schema-dir]} file]
  (read-schema (io/file tap-schema-dir file)))

(defn convert-multiary-type
  "multiary-type = a property that _may_ have more than one type."
  [tap-fs schema [property-name property-json-schema-partial
                  :as property]]
  (let [property (if (contains? property-json-schema-partial "$ref")
                   (let [{:keys [file json-pointer]}
                         (parse-json-schema-reference
                          (property-json-schema-partial "$ref"))

                         _
                         (when (and (nil? file)
                                    (empty? json-pointer))
                           (throw
                            (ex-info
                             "Infinite recursion json schema ref"
                             {:property-name
                              property-name

                              :property-json-schema-partial
                              property-json-schema-partial})))

                         schema
                         (if file (load-schema-file tap-fs file) schema)

                         referenced-json-schema-partial
                         (get-in schema json-pointer)]
                     (when (not referenced-json-schema-partial)
                       (throw (ex-info "$ref without matching definition"
                                       {:property property
                                        :schema schema})))
                     [property-name referenced-json-schema-partial])
                   property)]
    (let [unary-type-properties
          (property->unary-type-properties property)

          converted-unary-type-properties
          (map (partial convert-unary-type tap-fs schema)
               unary-type-properties)]
      (if (empty? converted-unary-type-properties)
        (do
          (println (str "Null unary type passed for property"
                        {:property property}))
          {"name" property-name
           "type" "null"
           "description" ""})
        (reduce merge-unary-types converted-unary-type-properties)))))

(defn tap-fs?
  [candidate-tap-fs]
  (and (every? #(contains? candidate-tap-fs %)
               [:tap-name :tap-directory :tap-schema-dir :tap-schemas])
       (not (empty? (candidate-tap-fs :tap-schemas)))))

(defn convert-schema-file
  [{:keys [tap-directory tap-name] :as tap-fs} input-json-schema-file]
  {:pre [(tap-fs? tap-fs)]}
  (let [schema-path        (.relativize (.toPath tap-directory)
                                        (.toPath input-json-schema-file))
        tap-version        (string/replace (string/trim (:out (sh "python" "setup.py" "--version" :dir tap-directory)))
                                           #"^([0-9]+)\..+"
                                           "$1.x")
        stream-name        (string/replace (.getName input-json-schema-file) #".json$" "")
        schema             (read-schema input-json-schema-file)
        ;; TODO Can probably be a `maybe-resolve-ref` function of some
        ;; kind. See `convert-multiary-type`. The main problem with
        ;; that is actually the shape of the thing we return with a ref.
        ;; Here's it the json-schema-partial. The other calling location
        ;; returns a property.
        schema             (if (contains? schema "$ref")
                             (let [{:keys [file] :as json-schema-reference}
                                   (parse-json-schema-reference (schema "$ref"))

                                   _
                                   (when (nil? file)
                                     (throw (ex-info "Infinite recursion json schema ref"
                                                     json-schema-reference)))

                                   referenced-json-schema-partial
                                   (get-in schema json-schema-reference)]
                               (when (not referenced-json-schema-partial)
                                 (throw (ex-info "$ref without matching definition"
                                                 {:schema-file input-json-schema-file
                                                  :schema      schema})))
                               referenced-json-schema-partial)
                             schema)
        initial-properties (get schema "properties")]
    ;; sorted-map-by _requires_ a comparator implementation, so don't try
    ;; to change this.
    (sorted-map-by (fn [x y]
                     (let [positions [
                                      "tap"
                                      "version"
                                      "key"
                                      "name"
                                      "doc-link"
                                      "singer-schema"
                                      "description"
                                      "replication-method"
                                      "api-method"
                                      "attributes"
                                      ]
                           x-pos     (.indexOf positions x)
                           y-pos     (.indexOf positions y)]
                       (cond (= x-pos y-pos)
                             0

                             (< x-pos y-pos)
                             -1

                             (> x-pos y-pos)
                             1)))
                   "tap"                (string/replace tap-name "tap-" "")
                   "version"            tap-version
                   "key"																""
                   "name"               stream-name
                   "doc-link"           ""
                   "singer-schema"      (format "https://github.com/singer-io/%s/blob/master/%s"
                                                tap-name
                                                schema-path)
                   "description"        ""
                   "replication-method" ""
                   "api-method"         {"name"     ""
                                         "doc-link" ""}
                   "attributes"         (convert-object-properties tap-fs schema initial-properties))))

(def cli-options
  [["-h" "--help" "Show help"]])

(defn tap-name?
  "Input to this is `shopify`, not `tap-shopify.

  TAP-NAME is valid if /opt/code/tap-TAP-NAME exists,
  /opt/code/tap-TAP-NAME/setup.py, and
  /opt/code/tap-TAP-NAME/tap_TAP-NAME/schemas/*.json exists."
  [tap-name]
  (if (string? tap-name)
    ;; tap-name is a string
    (if (string/starts-with? tap-name "tap-")
      false
      (let [tap-dir (format "/opt/code/tap-%s"
                            tap-name)
            tap-setup-script (format "%s/setup.py"
                                     tap-dir)
            tap-schema-dir (format "%s/tap_%s/schemas"
                                   tap-dir
                                   tap-name)]
        (and (.isDirectory (io/file tap-dir))
             (.exists (io/file tap-setup-script))
             (.isDirectory (io/file tap-schema-dir))
             (some #(string/ends-with? % ".json") (.list (io/file tap-schema-dir))))))
    false))

(defn tap-name->tap-directory
  [tap-name]
  {:pre [(tap-name? tap-name)]
   :post [(.getName %)]}
  (io/file "/opt/code" (format "tap-%s" tap-name)))

(defn tap-fs->schema-files
  [{:keys [tap-schema-dir] :as partial-tap-fs}]
  (let [schema-files (.list tap-schema-dir)]
    (->> schema-files
         (filter (partial re-matches #".*\.json"))
         (map (partial io/file tap-schema-dir)))))

(defn tap-directory->tap-fs
  [tap-directory]
  {:pre [(.exists tap-directory)]
   :post [(tap-fs? %)]}
  (let [tap-name             (string/trim (:out (sh "python" "setup.py" "--name" :dir tap-directory)))
        tap-code-package-dir (io/file tap-directory (string/replace tap-name "-" "_"))
        tap-schema-dir       (let [tap-schema-dir (io/file tap-code-package-dir "schemas")]
                               (if (.exists tap-schema-dir)
                                 tap-schema-dir
                                 (throw (ex-info "Schema directory does not exist"
                                                 {:tap-schema-dir tap-schema-dir}))))
        partial-tap-fs       {:tap-name       tap-name
                              :tap-directory  tap-directory
                              ;; This is the base URI for loading definitions.
                              :tap-schema-dir tap-schema-dir}
        tap-fs               (assoc partial-tap-fs :tap-schemas (tap-fs->schema-files partial-tap-fs))]
    tap-fs))

(defn tap-name->tap-fs
  [tap-name]
  {:pre [(tap-name? tap-name)]}
  (let [tap-directory (tap-name->tap-directory tap-name)]
    (tap-directory->tap-fs tap-directory)))

(defn cli-arg->tap-fs
  [cli-arg]
  {:pre [(string? cli-arg)]
   :post [(tap-fs? %)]}
  (try (tap-name->tap-fs cli-arg)
       (catch Error e
         (let [tap-directory (io/file cli-arg)]
           (try (tap-directory->tap-fs tap-directory))))))

(defn show-help
  [parsed-args]
  (println "tap-generate-docs"
           (:summary parsed-args)
           " [<tap-name> | <tap-directory>]")
  (when (not *interactive*)
    (System/exit 0)))

(defn tap-name->schema-files
  [tap-name]
  {:pre [(tap-name? tap-name)]}
  (let [schema-dir (io/file (format "/opt/code/tap-%s/tap_%s/schemas"
                                    tap-name
                                    tap-name))
        schema-files (.list schema-dir)]
    (map (partial io/file schema-dir) schema-files)))

(defn -main [& args]
  (let [parsed-args (cli/parse-opts args cli-options)]
    (if (or (get-in parsed-args [:options :help])
            (not= 1 (count (parsed-args :arguments)))
            (not (try (cli-arg->tap-fs (first (parsed-args :arguments)))
                      (catch Exception e)
                      (catch Error e))))
      (show-help parsed-args)
      (let [tap-fs       (cli-arg->tap-fs (first (parsed-args :arguments)))
            schema-files (:tap-schemas tap-fs)]
        (doall
         (for [file schema-files :when (schema-file? file)]
           (do (println (str "Processing file: " file))
               (let [converted-schema-file (convert-schema-file tap-fs file)
                  yaml-content          (.dump (Yaml. (doto (DumperOptions.)
                                                        (.setDefaultFlowStyle DumperOptions$FlowStyle/BLOCK)
                                                        (.setDefaultScalarStyle DumperOptions$ScalarStyle/DOUBLE_QUOTED)
                                                        (.setExplicitStart true)
                                                        (.setIndent 4)
                                                        (.setIndicatorIndent 2)
                                                        (.setPrettyFlow true)
                                                        (.setSplitLines true)))
                                               converted-schema-file)
                  ;; TODO Use make logic to avoid updating unedited schemas
                  ;; TODO Output to the properly formed
                  ;; /opt/code/docs/_integration-schemas/<tap-name>/v<N>/<schema-name>.md
                  target-file           (io/file (get-in parsed-args [:options
                                                                      :output-directory])
                                                 (string/replace (.getName file)
                                                                 #".json$"
                                                                 ".md"))]
              (println (format "Writing converted %s to %s"
                               file
                               target-file))
              (spit target-file
                    (string/replace (str yaml-content "---\n")
                                    #"\"([^\"]+?)\":"
                                    "$1:"))))))
        (when-not *interactive*
          (System/exit 0))))))

(comment
  (def ^:dynamic *interactive* true)
  (-main "bigcommerce")

  ;; Ensure you're fresh
  (do (dorun (map remove-ns '(tap-generate-docs tap-generate-docs-test)))
      (dorun (map load-file ["src/tap_generate_docs.clj" "test/tap_generate_docs_test.clj"]))
      (in-ns 'tap-generate-docs)
      (def ^:dynamic *interactive* true))
  )
