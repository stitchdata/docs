(ns tap-generate-docs
  (:require [clojure.data.json :as json]
            [clojure.java.io :as io]
            [clojure.string :as string]
            [clojure.tools.cli :as cli])
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
  [[k v :as property]]
  (string? (v "type")))

(defn converted-unary-type?
  [candidate-converted-unary-type]
  (let [name (candidate-converted-unary-type "name")
        type (candidate-converted-unary-type "type")
        description (candidate-converted-unary-type "description")]
    (and (string? name)
         (string? type)
         (= "" description))))

;;; WARNING! Mutual Recursion Incoming!
(declare convert-simple-type)

(defn convert-array-object-type
  [[property-name property-json-schema-partial :as property]]
  (let [items (property-json-schema-partial "items")
        item-type (property-json-schema-partial "type")]
    (if (or (= "object" item-type)
            (= ["object"] item-type))
      (sort-by #(get % "name")
               (map convert-simple-type
                    (items "properties")))
      (let [object-properties (sort-by #(get % "name")
                                       (map convert-simple-type
                                            (items "properties")))
            other-properties (let [other-properties (filter (partial not= "object") item-type)]
                               (if ((set other-properties) "array")
                                 (throw (ex-info "Currently cannot handle a type with object _and_ array present"
                                                 {:property property}))
                                 other-properties))
            converted-other-properties [(convert-simple-type ["value"
                                                              (assoc items
                                                                     "type"
                                                                     other-properties)])]
            all-properties (sort-by #(% "name") (into object-properties converted-other-properties))]
        (if (< 1 (count (filter #(= "value" (get % "name")) all-properties)))
          object-properties
          all-properties)))))

(defn convert-unary-type
  [[property-name property-json-schema-partial :as property]]
  {:pre [(unary-type? property)]
   :post [(converted-unary-type? %)]}
  (let [base-converted-property {"name" property-name
                                 "type" (if (and (= "string" (property-json-schema-partial "type"))
                                                 (contains? property-json-schema-partial "format"))
                                          (property-json-schema-partial "format")
                                          (property-json-schema-partial "type"))
                                 "description" ""}
        ;; TODO maybe rename?
        lift-object-properties (fn [items]
                                 ;; TODO this sorting has to be able to move elsewhere
                                 (sort-by #(get % "name")
                                          (map convert-simple-type
                                               (items "properties"))))]
    (cond (= "object" (property-json-schema-partial "type"))
          (assoc base-converted-property "object-properties" (lift-object-properties property-json-schema-partial))

          (= "array" (property-json-schema-partial "type"))
          (assoc base-converted-property
                 "array-attributes"
                 (let [items (property-json-schema-partial "items")
                       item-type (items "type")]
                   (if (or (= "object" item-type)
                           ((set item-type) "object"))
                     (convert-array-object-type items)
                     [(convert-simple-type ["value" items])])))

          :default
          base-converted-property)))

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
    (if-let [object-properties (or (converted-prop-1 "object-properties")
                                   (converted-prop-2 "object-properties"))]
      (assoc base-properties "object-properties" object-properties)
      base-properties)))

(defn property->unary-type-properties
  [[k v :as property]]
  (filter #((partial not= "null") (get-in % [1 "type"]))
          (let [type (v "type")]
            (if (string? type)
              [property]
              (map (fn [type]
                     [k (assoc v "type" type)])
                   (v "type"))))))

(defn convert-simple-type
  "Simple Type = not a array or object"
  [[k v :as property]]
  (let [unary-type-properties (property->unary-type-properties property)
        converted-unary-type-properties (map convert-unary-type unary-type-properties)
        property (if (empty? converted-unary-type-properties)
                   (throw (ex-info "Null unary type passed for property"
                                   {:property property}))
                   (reduce merge-unary-types converted-unary-type-properties))]
    property))

;; ;; TODO still need to port $ref

;; (defn convert-schema-file
;;   [input-json-schema-file]
;;   {:pre [(string/ends-with? input-json-schema-file ".json")]}
;;   (let [schema-file        (io/file input-json-schema-file)
;;         tap-base-dir       (-> schema-file
;;                                (.getParentFile)
;;                                (.getParentFile)
;;                                (.getParentFile))
;;         schema-path        (.relativize (.toPath tap-base-dir)
;;                                         (.toPath schema-file))
;;         tap-name           (-> tap-base-dir
;;                                (.getName)
;;                                (string/replace #"^tap-" ""))
;;         tap-version        (string/replace (string/trim (:out (sh "python" "setup.py" "--version" :dir tap-base-dir)))
;;                                            #"^([0-9]+)\..+"
;;                                            "$1.x")
;;         stream-name        (string/replace (.getName schema-file) #".json$" "")
;;         schema             (with-open [r (io/reader input-json-schema-file)]
;;                              (json/read r))
;;         ;; schema             (if (get schema "$ref")
;;         ;;                      (let [v (get definitions (second (string/split (get schema "$ref") #"/")))]
;;         ;;                        (when-not v
;;         ;;                          (throw (Exception. "$ref used but none supplied")))
;;         ;;                        v)
;;         ;;                      schema)
;;         ;; TODO throw if the top level schema is not the shape we expect
;;         ;; (i.e. is not an object with properties)
;;         initial-properties (get schema "properties")]
;;     ;; sorted-map-by _requires_ a comparator implementation, so don't try
;;     ;; to change this.
;;     (sorted-map-by (fn [x y]
;;                      (let [positions [
;;                                       "tap"
;;                                       "version"
;;                                       "name"
;;                                       "doc-link"
;;                                       "singer-schema"
;;                                       "description"
;;                                       "replication-method"
;;                                       "api-method"
;;                                       "attributes"
;;                                       ]
;;                            x-pos     (.indexOf positions x)
;;                            y-pos     (.indexOf positions y)]
;;                        (cond (= x-pos y-pos)
;;                              0

;;                              (< x-pos y-pos)
;;                              -1

;;                              (> x-pos y-pos)
;;                              1)))
;;                    ;; TODO much of the following should be tap-fs lookups
;;                    "tap"                tap-name
;;                    "version"            tap-version
;;                    "name"               stream-name
;;                    "doc-link"           ""
;;                    "singer-schema"      (format "https://github.com/singer-io/tap-%s/blob/master/%s"
;;                                                 tap-name
;;                                                 schema-path)
;;                    "description"        ""
;;                    "replication-method" ""
;;                    "api-method"         {
;;                                          "name"     ""
;;                                          "doc-link" ""}
;;                    "attributes"         (sort-by #(get % "name")
;;                                                  ;; TODO this call should by convert-multiary-property
;;                                                  (map convert-property initial-properties)))))

;; (comment
;;   (let [definitions-file "/Users/tvisher/Downloads/tap-closeio/tap_closeio/schemas/_sdc_definitions.json"
;;         schema-file      "/Users/tvisher/Downloads/tap-closeio/tap_closeio/schemas/users.json"
;;         definitions      (with-open [r (io/reader definitions-file)]
;;                            (json/read r))]
;;     (convert-schema-file definitions
;;                          schema-file))
;;   )

;; (def cli-options
;;   [["-h" "--help"]])

;; (defn show-help
;;   [parsed-args]
;;   (println "tap-generate-docs" (:summary parsed-args) " <tap-name>")
;;   (when (not *interactive*)
;;     (System/exit 0)))

;; (comment
;;   (cli/parse-opts ["shopify"] cli-options)
;;   )

;; (defn tap-name?
;;   "Input to this is `shopify`, not `tap-shopify.

;;   TAP-NAME is valid if /opt/code/tap-TAP-NAME exists,
;;   /opt/code/tap-TAP-NAME/setup.py, and
;;   /opt/code/tap-TAP-NAME/tap_TAP-NAME/schemas/*.json exists."
;;   [tap-name]
;;   (if (string? tap-name)
;;     ;; tap-name is a string
;;     (if (string/starts-with? tap-name "tap-")
;;       false
;;       (let [tap-dir (format "/opt/code/tap-%s"
;;                             tap-name)
;;             tap-setup-script (format "%s/setup.py"
;;                                      tap-dir)
;;             tap-schema-dir (format "%s/tap_%s/schemas"
;;                                    tap-dir
;;                                    tap-name)]
;;         (and (.isDirectory (io/file tap-dir))
;;              (.exists (io/file tap-setup-script))
;;              (.isDirectory (io/file tap-schema-dir))
;;              (some #(string/ends-with? % ".json") (.list (io/file tap-schema-dir))))))
;;     false))

;; (defn tap-name->schema-files
;;   [tap-name]
;;   {:pre [(tap-name? tap-name)]}
;;   (let [schema-dir (io/file (format "/opt/code/tap-%s/tap_%s/schemas"
;;                                     tap-name
;;                                     tap-name))
;;         schema-files (.list schema-dir)]
;;     (map (partial io/file schema-dir) schema-files)))

;; (defn tap-name->tap-fs
;;   [tap-name]
;;   {:pre [(tap-name? tap-name)]}
;;   {:tap-name tap-name
;;    :tap-directory (io/file (format "/opt/code/tap-%s"
;;                                    tap-name))
;;    ;; This is the base URI for loading definitions.
;;    :tap-schema-dir (io/file (format "/opt/code/tap-%s/tap_%s/schemas"
;;                                     tap-name
;;                                     tap-name))
;;    :tap-schemas (tap-name->schema-files tap-name)})

;; (comment
;;   (convert-schema-file (first schema-files))
;;   )

;; (defn -main [& args]
;;   (let [parsed-args (cli/parse-opts args cli-options)]
;;     (when (or (get-in parsed-args [:options :help])
;;               (= 1 (count (:arguments parsed-args)))
;;               (not (every? tap-name? (:arguments parsed-args))))
;;       (show-help parsed-args))
;;     (let [[tap-name] (:arguments parsed-args)
;;           tap-fs (tap-name->tap-fs tap-name)
;;           schema-files (:tap-schemas tap-fs)]
;;       (def tap-fs tap-fs)
;;       (def schema-files schema-files)
;;       (doall
;;        (for [file schema-files]
;;          ;; TODO (convert-schema-file tap-fs file)
;;          (let [converted-schema-file (convert-schema-file file)
;;                yaml-content (.dump (Yaml. (doto (DumperOptions.)
;;                                             (.setDefaultFlowStyle DumperOptions$FlowStyle/BLOCK)
;;                                             (.setDefaultScalarStyle DumperOptions$ScalarStyle/DOUBLE_QUOTED)
;;                                             (.setExplicitStart true)
;;                                             (.setIndent 4)
;;                                             (.setIndicatorIndent 2)
;;                                             (.setPrettyFlow true)
;;                                             (.setSplitLines true)))
;;                                    converted-schema-file)
;;                ;; TODO Use make logic to avoid updating unedited schemas
;;                target-file (io/file (get-in parsed-args [:options
;;                                                          :output-directory])
;;                                     (string/replace (.getName file)
;;                                                     #".json$"
;;                                                     ".md"))]
;;            converted-schema-file
;;            #_(println (format "Writing converted %s to %s"
;;                               file
;;                               target-file))
;;            #_(spit target-file
;;                    (string/replace (str yaml-content "---\n")
;;                                    #"\"([^\"]+?)\":"
;;                                    "$1:")))))
;;       #_(let [definitions (if definitions-file
;;                             (with-open [r (io/reader definitions-file)]
;;                               (json/read r))
;;                             {})]
;;           (doall
;;            (for [file schema-files]
;;              (let [converted-schema-file (convert-schema-file definitions file)
;;                    yaml-content (.dump (Yaml. (doto (DumperOptions.)
;;                                                 (.setDefaultFlowStyle DumperOptions$FlowStyle/BLOCK)
;;                                                 (.setDefaultScalarStyle DumperOptions$ScalarStyle/DOUBLE_QUOTED)
;;                                                 (.setExplicitStart true)
;;                                                 (.setIndent 4)
;;                                                 (.setIndicatorIndent 2)
;;                                                 (.setPrettyFlow true)
;;                                                 (.setSplitLines true)))
;;                                        converted-schema-file)
;;                    ;; TODO Use make logic to avoid updating unedited schemas
;;                    target-file (io/file (get-in parsed-args [:options
;;                                                              :output-directory])
;;                                         (string/replace (.getName file)
;;                                                         #".json$"
;;                                                         ".md"))]
;;                (println (format "Writing converted %s to %s"
;;                                 file
;;                                 target-file))
;;                (spit target-file
;;                      (string/replace (str yaml-content "---\n")
;;                                      #"\"([^\"]+?)\":"
;;                                      "$1:"))))))
;;       (when-not *interactive*
;;         (System/exit 0)))))

;; (comment
;;   (def ^:dynamic *interactive* true)
;;   (-main "shopify")
;;   )
