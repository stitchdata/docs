(ns tap-generate-docs-test
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
    (are [x y] (= (convert-unary-type nil x) y)
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
    (are [x y] (= (convert-unary-type nil x) (assoc y "description" ""))
      ["an_object" {"type" "object"
                    "properties" {"z" {"type" "string"}
                                  "a" {"type" "string"}}}]
      {"name" "an_object"
       "type" "object"
       "description" ""
       "object-properties" [{"name" "a"
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
       "object-properties" []}))

  (comment
    (convert-unary-type nil
                        ["an_array" {"type" "array"
                                     "items" {"type" "string"}}])
    )

  (testing "Arrays"
    (are [x y] (= (assoc y "description" "") (convert-unary-type nil x))
      ["an_array" {"type" "array"
                   "items" {"type" "string"}}]
      {"name" "an_array"
       "type" "array"
       "description" ""
       "array-attributes" [{"name" "value"
                            "type" "string"
                            "description" ""}]}

      ["an_array" {"type" "array"
                   "items" {"type" "number"}}]
      {"name" "an_array"
       "type" "array"
       "description" ""
       "array-attributes" [{"name" "value"
                            "type" "number"
                            "description" ""}]}

      ["an_array" {"type" "array"
                   "items" {"type" "string"
                            "format" "date-time"}}]
      {"name" "an_array"
       "type" "array"
       "description" ""
       "array-attributes" [{"name" "value"
                            "type" "date-time"
                            "description" ""}]}

      ["an_array" {"type" "array"
                   "items" {"type" ["string" "integer"]}}]
      {"name" "an_array"
       "type" "array"
       "description" ""
       "array-attributes" [{"name" "value"
                            "type" "integer, string"
                            "description" ""}]}

      ["an_array" {"type" "array"
                   "items" {"type" "object"
                            "properties" {"a" {"type" "string"}}}}]
      {"name" "an_array"
       "type" "array"
       "description" ""
       "array-attributes" [{"name" "a"
                            "type" "string"
                            "description" ""}]}

      ["an_array" {"type" "array"
                   "items" {"type" "object"
                            "properties" {"b" {"type" "string"}}}}]
      {"name" "an_array"
       "type" "array"
       "description" ""
       "array-attributes" [{"name" "b"
                            "type" "string"
                            "description" ""}]}

      ["an_array" {"type" "array"
                   "items" {"type" ["object"]
                            "properties" {"b" {"type" "string"}}}}]
      {"name" "an_array"
       "type" "array"
       "description" ""
       "array-attributes" [{"name" "b"
                            "type" "string"
                            "description" ""}]}

      ["an_array" {"type" "array"
                   "items" {"type" ["object" "string"]
                            "properties" {"a" {"type" "string"}}}}]
      {"name" "an_array"
       "type" "array"
       "description" ""
       "array-attributes" [{"name" "a"
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
       "array-attributes" [{"name" "value"
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
       "array-attributes" [{"name" "a"
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
       "array-attributes" [{"name" "a"
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
                    ["an_array" {"type" "array"
                                 ;; What could possibly be the right result here?
                                 "items" {"type" ["object" "string" "array"]
                                          "format" "date-time"
                                          "properties" {"a" {"type" "string"}
                                                        "value" {"type" "integer"}}}}]))))))

(comment
  (convert-multiary-type nil ["a_date" {"type" ["null" "string" "integer"]
                                        "format" "date-time"}])
  )

(deftest convert-multiary-type-tests
  (testing "Non-null types"
    ;; TODO convert-multiary-type -> convert-multiary?-type
    (are [x y] (= (convert-multiary-type nil x) y)
      ["a_date" {"type" ["null" "string" "integer"]
                 "format" "date-time"}]
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
       "object-properties" [{"name" "a"
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
       "array-attributes" [{"name" "amount",
                            "type" "number",
                            "description" ""}]}

      ["an_array" {"type" "array"
                   "items" {"type" ["null" "object"],
                            "properties" {}}}]
      ;; Note we know nothing about what it can be.
      {"name" "an_array",
       "type" "array",
       "description" ""})))

;; These are not throwing anymore, since an empty properties schema is valid. They now log.
#_(testing "Null types"
    (is (thrown? clojure.lang.ExceptionInfo
                 (convert-multiary-type nil ["a_null" {"type" "null"}])))
    (is (thrown? clojure.lang.ExceptionInfo
                 (convert-multiary-type nil ["a_null" {"type" ["null"]}]))))

(deftest convert-types-with-refs-tests
  (is (= (convert-multiary-type {"definitions" {"date" {"type" "string"
                                                        "format" "date-time"}}}
                                ["a_date" {"$ref" "#/definitions/date"}])
         {"name" "a_date"
          "type" "date-time"
          "description" ""}))
  (is (= (convert-multiary-type {"definitions" {"integer" {"type" "integer"}}}
                                ["an_integer" {"$ref" "#/definitions/integer"}])
         {"name" "an_integer"
          "type" "integer"
          "description" ""}))
  (is (thrown? clojure.lang.ExceptionInfo
               (convert-multiary-type {"definitions" {"integer" {"type" "integer"}}}
                                      ["an_string" {"$ref" "#/definitions/string"}]))))
