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

(def ^:dynamic *interactive* false)

(defn convert-simple-type
  [[k v :as property]]
  {"name" k
   "type" (if (string? (get v "type"))
            (get v "type")
            (string/join ", " (sort (filter (partial not= "null") (get v "type")))))
   "description" ""})

(declare convert-property)

(defn convert-array-property
  [definitions property]
  (cond (some (partial = "object") (get property "type"))
        (if (empty? (get property "properties"))
          {"type" (string/join ", " (filter (partial not= "null") (sort (get property "type"))))
           "object-properties" []}
          (map (partial convert-property definitions)
               (get property "properties")))

        :default
        (get property "type")))

(defn convert-property
  [definitions [k v :as property]]
  (cond (get v "$ref")
        (let [v (get definitions (second (string/split (get v "$ref") #"/")))]
          (when-not v
            (throw (Exception. "$ref used but none supplied")))
          (convert-property definitions [k v]))

        (some (partial = "object") (get v "type"))
        {"name" k
         "type" (string/join ", " (sort (filter (partial not= "null") (get v "type"))))
         "description" ""
         "object-properties" (sort-by #(get % "name")
                                      (map (partial convert-property definitions)
                                           (get v "properties")))}

        (some (partial = "array") (get v "type"))
        {"name" k
         "type" (string/join ", " (filter (partial not= "null") (sort (get v "type"))))
         "description" ""
         "array-attributes" (let [array-properties (convert-array-property
                                                    definitions
                                                    (if (get-in v ["items" "$ref"])
                                                      (let [v (get definitions (second (string/split (get-in v ["items" "$ref"]) #"/")))]
                                                        (when-not v
                                                          (throw (Exception. "$ref used but none supplied")))
                                                        v)
                                                      (get v "items")))]
                              (cond
                                (string? array-properties)
                                array-properties

                                (map? array-properties)
                                array-properties

                                ((complement map?) (first array-properties))
                                (string/join ", " (filter (partial not= "null") array-properties))

                                :default
                                (sort-by #(get % "name") array-properties)))}

        :default
        (convert-simple-type property)))

(defn convert-schema-file
  [definitions input-json-schema-file]
  {:pre [(string/ends-with? input-json-schema-file ".json")]}
  (let [schema-file        (io/file input-json-schema-file)
        tap-base-dir       (-> schema-file
                               (.getParentFile)
                               (.getParentFile)
                               (.getParentFile))
        schema-path        (.relativize (.toPath tap-base-dir)
                                        (.toPath schema-file))
        tap-name           (-> tap-base-dir
                               (.getName)
                               (string/replace #"^tap-" ""))
        tap-version        (string/replace (string/trim (:out (sh "python" "setup.py" "--version" :dir tap-base-dir)))
                                           #"^([0-9]+)\..+"
                                           "$1.x")
        stream-name        (string/replace (.getName schema-file) #".json$" "")
        schema             (with-open [r (io/reader input-json-schema-file)]
                             (json/read r))
        schema             (if (get schema "$ref")
                             (let [v (get definitions (second (string/split (get schema "$ref") #"/")))]
                               (when-not v
                                 (throw (Exception. "$ref used but none supplied")))
                               v)
                             schema)
        initial-properties (sort-by first (get schema "properties"))]
    (sorted-map-by (fn [x y]
                     (let [positions [
                                      "tap"
                                      "version"
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
                   "tap"                tap-name
                   "version"            tap-version
                   "name"               stream-name
                   "doc-link"           ""
                   "singer-schema"      (format "https://github.com/singer-io/tap-%s/blob/master/%s"
                                                tap-name
                                                schema-path)
                   "description"        ""
                   "replication-method" ""
                   "api-method"         {
                                         "name"     ""
                                         "doc-link" ""}
                   "attributes"         (sort-by #(get % "name") (map (partial convert-property definitions)
                                                                      initial-properties)))))

(comment
  (let [definitions-file "/Users/tvisher/Downloads/tap-closeio/tap_closeio/schemas/_sdc_definitions.json"
        schema-file      "/Users/tvisher/Downloads/tap-closeio/tap_closeio/schemas/users.json"
        definitions      (with-open [r (io/reader definitions-file)]
                           (json/read r))]
    (convert-schema-file definitions
                         schema-file))
  )

(def cli-options
  [["-o" "--output-directory DIRECTORY"
    "Directory to write output md files too"
    :default (io/file ".")
    :parse-fn io/file
    :validate [#(and (.exists %)
                     (.isDirectory %))
               "Output directory does not exists or is not a directory"]]
   ["-h" "--help"]])

(defn show-help
  [parsed-args]
  (println (str "tap-generate-docs"
                (:summary parsed-args)
                " json_schema_file.json ..."))
  (when (not *interactive*)
    (System/exit 0)))

(defn -main [& args]
  (let [parsed-args (cli/parse-opts args cli-options)]
    (def parsed-args parsed-args)
    (when (or (get-in parsed-args [:options :help])
              (empty? (:arguments parsed-args))
              ((complement every?) #(string/ends-with? % ".json") (:arguments parsed-args)))
      (show-help parsed-args))
    (let [file-names (:arguments parsed-args)
          files (map io/file file-names)
          definitions-file (first (filter #(= "_sdc_definitions.json" (.getName %))
                                         files))
          schema-files (filter #(not= "_sdc_definitions.json" (.getName %))
                               files)]
      (when ((complement every?) #(.exists %) files)
        (println "# All files must exist")
        (show-help parsed-args))
      (let [definitions (if definitions-file
                          (with-open [r (io/reader definitions-file)]
                            (json/read r))
                          {})]
        (doall
         (for [file schema-files]
           (let [converted-schema-file (convert-schema-file definitions file)
                 yaml-content (.dump (Yaml. (doto (DumperOptions.)
                                              (.setDefaultFlowStyle DumperOptions$FlowStyle/BLOCK)
                                              (.setDefaultScalarStyle DumperOptions$ScalarStyle/DOUBLE_QUOTED)
                                              (.setExplicitStart true)
                                              (.setIndent 4)
                                              (.setIndicatorIndent 2)
                                              (.setPrettyFlow true)
                                              (.setSplitLines true)))
                                     converted-schema-file)
                 target-file (io/file (get-in parsed-args [:options
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
        (System/exit 0)))))

(comment
  (binding [*interactive* true]
    (-main "-o"
           "/opt/code/docs/_integration-schemas/closeio/v1/"
           "/opt/code/tap-closeio/tap_closeio/schemas/activities.json"))
  )
