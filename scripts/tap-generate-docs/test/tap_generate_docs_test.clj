(ns tap-generate-docs-test
  (:require [clojure.java.io :as io])
  (:require [clojure.test :refer :all]
            [tap-generate-docs :refer :all]))

(deftest property->unary-type-properties-tests
  (are [x y] (= (set (property->unary-type-properties
                      x))
                (set y))
    ["a_string" {"type" "string"}]
    [["a_string" {"type" "string"}]]

    ["a_string" {"type" ["string"]}]
    [["a_string" {"type" "string"}]]

    ["a_string_or_int" {"type" ["string" "integer"]}]
    [["a_string_or_int" {"type" "string"}]
     ["a_string_or_int" {"type" "integer"}]]

    ["a_string_or_null" {"type" ["null" "string"]}]
    [["a_string_or_null" {"type" "string"}]]

    ["a_date_time" {"type" "string"
                    "format" "date-time"}]
    [["a_date_time" {"type" "string"
                     "format" "date-time"}]]

    ["a_date_time_or_integer" {"type" ["string" "integer"]
                               "format" "date-time"}]
    [["a_date_time_or_integer" {"type" "string"
                                "format" "date-time"}]
     ["a_date_time_or_integer" {"type" "integer"
                                "format" "date-time"}]]))

(deftest convert-unary-type-tests
  (testing "Simple types"
    (are [x y] (= (convert-unary-type nil nil x) y)
      ["property" {}]
      {"name" "property"
       "type" "anything"
       "description" ""}

      ["a_string" {"type" "string"}]
      {"name" "a_string"
       "type" "string"
       "description" ""}

      ["a_date_time" {"type" "string"
                      "format" "date-time"}]
      {"name" "a_date_time"
       "type" "date-time"
       "description" ""}

      ["an_integer" {"type" "integer"}]
      {"name" "an_integer"
       "type" "integer"
       "description" ""}

      ["fulfillment_status" {"type" "string"
                             "enum" ["fulfilled" "partial" "not_eligible"]}]
      {"name" "fulfillment_status"
       "type" "string"
       "description" "Valid values: fulfilled, not_eligible, partial."}
      ))

  (testing "Objects"
    (are [x y] (= (convert-unary-type nil nil x) (assoc y "description" ""))
      ["an_object" {"type" "object"
                    "properties" {"z" {"type" "string"}
                                  "a" {"type" "string"}}}]
      {"name" "an_object"
       "type" "object"
       "description" ""
       "subattributes" [{"name" "a"
                             "type" "string"
                             "description" ""}
                            {"name" "z"
                             "type" "string"
                             "description" ""}]}

      ["an_object" {"type" "object"
                    "properties" {}}]
      {"name" "an_object"
       "type" "object"
       "description" ""
       "subattributes" []}

      ["an_object" {"type" "object"
                    "properties" {"type" {"type" "string"}}}]
      {"name" "an_object"
       "type" "object"
       "description" ""
       "subattributes" [{"name" "type"
                             "type" "string"
                             "description" ""}]}))

  (testing "Arrays"
    (are [x y] (= (assoc y "description" "") (convert-unary-type nil nil x))
      ["an_array" {"type" "array"
                   "items" {"type" "string"}}]
      {"name" "an_array"
       "type" "array"
       "description" ""
       "subattributes" [{"name" "value"
                            "type" "string"
                            "description" ""}]}

      ["an_array" {"type" "array"
                   "items" {"type" "number"}}]
      {"name" "an_array"
       "type" "array"
       "description" ""
       "subattributes" [{"name" "value"
                            "type" "number"
                            "description" ""}]}

      ["an_array" {"type" "array"
                   "items" {"type" "string"
                            "format" "date-time"}}]
      {"name" "an_array"
       "type" "array"
       "description" ""
       "subattributes" [{"name" "value"
                            "type" "date-time"
                            "description" ""}]}

      ["an_array" {"type" "array"
                   "items" {"type" ["string" "integer"]}}]
      {"name" "an_array"
       "type" "array"
       "description" ""
       "subattributes" [{"name" "value"
                            "type" "integer, string"
                            "description" ""}]}

      ["an_array" {"type" "array"
                   "items" {"type" "object"
                            "properties" {"a" {"type" "string"}}}}]
      {"name" "an_array"
       "type" "array"
       "description" ""
       "subattributes" [{"name" "a"
                            "type" "string"
                            "description" ""}]}

      ["an_array" {"type" "array"
                   "items" {"type" "object"
                            "properties" {"b" {"type" "string"}}}}]
      {"name" "an_array"
       "type" "array"
       "description" ""
       "subattributes" [{"name" "b"
                            "type" "string"
                            "description" ""}]}

      ["an_array" {"type" "array"
                   "items" {"type" ["object"]
                            "properties" {"b" {"type" "string"}}}}]
      {"name" "an_array"
       "type" "array"
       "description" ""
       "subattributes" [{"name" "b"
                            "type" "string"
                            "description" ""}]}

      ["an_array" {"type" "array"
                   "items" {"type" ["object" "string"]
                            "properties" {"a" {"type" "string"}}}}]
      {"name" "an_array"
       "type" "array"
       "description" ""
       "subattributes" [{"name" "a"
                            "type" "string"
                            "description" ""}
                           ;; Really?
                           {"name" "value"
                            "type" "string"
                            "description" ""}]}

      ["an_array" {"type" "array"
                   "items" {"type" ["object" "string"]
                            "properties" {"z" {"type" "string"}}}}]
      {"name" "an_array"
       "type" "array"
       "description" ""
       ;; Really?
       "subattributes" [{"name" "value"
                            "type" "string"
                            "description" ""}
                           {"name" "z"
                            "type" "string"
                            "description" ""}]}

      ["an_array" {"type" "array"
                   "items" {"type" ["object" "string"]
                            "format" "date-time"
                            "properties" {"a" {"type" "string"}}}}]
      {"name" "an_array"
       "type" "array"
       "description" ""
       "subattributes" [{"name" "a"
                            "type" "string"
                            "description" ""}
                           ;; Really?
                           {"name" "value"
                            "type" "date-time"
                            "description" ""}]}

      ["an_array" {"type" "array"
                   "items" {"type" ["object" "string"]
                            "format" "date-time"
                            "properties" {"a" {"type" "string"}
                                          "value" {"type" "integer"}}}}]
      {"name" "an_array"
       "type" "array"
       "description" ""
       "subattributes" [{"name" "a"
                            "type" "string"
                            "description" ""}
                           ;; Really? Note that there is a conflict
                           ;; between the 'invented' column `value` from
                           ;; the "string" type and the 'real' `value`
                           ;; from the object properties.
                           {"name" "value"
                            "type" "integer"
                            "description" ""}]})
    (testing "Objects"
      (is (thrown? clojure.lang.ExceptionInfo
                   (convert-unary-type
                    nil
                    nil
                    ["an_array" {"type" "array"
                                 ;; What could possibly be the right result here?
                                 "items" {"type" ["object" "string" "array"]
                                          "format" "date-time"
                                          "properties" {"a" {"type" "string"}
                                                        "value" {"type" "integer"}}}}]))))))

(deftest convert-multiary-type-tests
  (testing "Non-null types"
    ;; TODO convert-multiary-type -> convert-multiary?-type
    (are [x y] (= (convert-multiary-type nil nil x) y)
      ["a_date" {"type" ["null" "string" "integer"]
                 "format" "date-time"}]
      {"name" "a_date"
       "type" "date-time, integer"
       "description" ""}

      ["a_date" {"anyOf" [{"type" ["null" "string"]
                           "format" "date-time"}
                          {"type" "integer"}]}]
      {"name" "a_date"
       "type" "date-time, integer"
       "description" ""}

      ["a_date" {"type" "string"
                 "format" "date-time"}]
      {"name" "a_date"
       "type" "date-time"
       "description" ""}

      ["a_date" {"type" ["null" "string"]
                 "format" "date-time"}]
      {"name" "a_date"
       "type" "date-time"
       "description" ""}

      ["an_object" {"type" ["object" "string"]
                    "format" "date-time"
                    "properties" {"z" {"type" "string"}
                                  "a" {"type" "string"}}}]
      {"name" "an_object"
       "type" "date-time, object"
       "description" ""
       "subattributes" [{"name" "a"
                             "type" "string"
                             "description" ""}
                            {"name" "z"
                             "type" "string"
                             "description" ""}]}

      ["an_array" {"type" "array"
                   "items" {"type" ["null" "object"],
                            "properties" {"amount" {"type" ["null" "number"]}}}}]
      {"name" "an_array",
       "type" "array",
       "description" "",
       "subattributes" [{"name" "amount",
                            "type" "number",
                            "description" ""}]}

      ["an_array" {"type" "array"
                   "items" {"type" ["null" "object"],
                            "properties" {}}}]
      ;; Note we know nothing about what it can be.
      {"name" "an_array",
       "type" "array",
       "description" ""})))

(deftest convert-multiary-null-type-tests
  (testing "Null types"
    (is (= {"name" "a_null"
            "type" "null"
            "description" ""}
           (convert-multiary-type nil nil ["a_null" {"type" "null"}])))
    (is (= {"name" "a_null", "type" "null", "description" ""}
           (convert-multiary-type nil nil ["a_null" {"type" ["null"]}])))))

(deftest convert-types-with-refs-tests
  (is (= (convert-multiary-type nil
                                {"definitions" {"date" {"type" "string"
                                                        "format" "date-time"}}}
                                ["a_date" {"$ref" "#/definitions/date"}])
         {"name" "a_date"
          "type" "date-time"
          "description" ""}))
  (is (= (convert-multiary-type nil
                                {"definitions" {"integer" {"type" "integer"}}}
                                ["an_integer" {"$ref" "#/definitions/integer"}])
         {"name" "an_integer"
          "type" "integer"
          "description" ""}))
  (is (thrown? clojure.lang.ExceptionInfo
               (convert-multiary-type nil
                                      {"definitions" {"integer" {"type" "integer"}}}
                                      ["an_string" {"$ref" "#/definitions/string"}]))))

(deftest maybe-remove-anyOf-test
  (are [x y] (= y
                (maybe-remove-anyOf x))
    ["field1" {"anyOf" [{"type" "string"}
                        {"type" "integer"}]}]
    ["field1" {"type" ["string" "integer"]}]

    ["field2" {"anyOf" [{"type" ["null" "string"]}
                        {"type" "integer"}]}]
    ["field2" {"type" ["null" "string" "integer"]}]

    ["field3" {"anyOf" [{"type" ["null" "string"]
                         "format" "date-time"}
                        {"type" "string"}]}]
    ["field3" {"type" ["null" "string"]
               "format" "date-time"}]

    ["field4" {"type" ["null" "string"]}]
    ["field4" {"type" ["null" "string"]}]))

(deftest convert-types-with-bad-refs-tests
  (is (thrown? clojure.lang.ExceptionInfo
               (convert-multiary-type nil
                                      nil
                                      ["an_bad_ref" {"$ref" "#/"}])))

  (is (thrown? clojure.lang.ExceptionInfo
               (convert-multiary-type nil
                                      nil
                                      ["an_bad_ref" {"$ref" ""}]))))

(deftest parse-json-schema-reference-tests
  (is (= {:file nil :json-pointer ["def"]}
         (parse-json-schema-reference "#/def")))
  (is (= {:file nil :json-pointer ["def" "foo" "bar"]}
         (parse-json-schema-reference "#/def/foo/bar")))
  (is (= {:file "definitions.json" :json-pointer ["def"]}
         (parse-json-schema-reference "definitions.json#/def")))
  (is (= {:file "shared/type-string.json" :json-pointer []}
         (parse-json-schema-reference "shared/type-string.json#/")))
  (is (= {:file "shared/type-string.json" :json-pointer ["def"]}
         (parse-json-schema-reference "shared/type-string.json#/def")))
  (is (= {:file "shared/type-string.json" :json-pointer ["def" "foo" "bar"]}
         (parse-json-schema-reference "shared/type-string.json#/def/foo/bar")))
  (is (= {:file "shared/type_string.json" :json-pointer ["def"]}
         (parse-json-schema-reference "shared/type_string.json#/def")))
  (is (= {:file nil :json-pointer []}
         (parse-json-schema-reference "#/")))

  (is (thrown? clojure.lang.ExceptionInfo
               (parse-json-schema-reference "foo-bar.json")))
  (is (thrown? clojure.lang.ExceptionInfo
               (parse-json-schema-reference "shared/foo_bar.json"))))

(deftest load-schema-file-tests
  (is (= {} (load-schema-file
             {:tap-schema-dir (io/file "test_schemas")}
             "definitions.json"))))

(deftest schema-file?-tests
  (is (schema-file? (io/file "test_schemas/valid_schema_file.json")))
  (is (not (schema-file? (io/file "test_schemas/invalid_schema_file.json"))))
  (is (not (schema-file? (io/file "test_schemas/non_existent_schema_file.json")))))
