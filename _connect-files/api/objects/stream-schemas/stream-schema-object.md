---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-structure"
key: "stream-schema-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Stream Schema"
description: "{{ api.data-structures.stream-schemas.description }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "schema"
    type: "string"
    description: "The JSON schema describing the stream's fields."

  - name: "metadata"
    type: "array"
    description: "An array of [Metadata objects]({{ api.data-structures.metadata.top-level.section }})."

  - name: "non-discoverable-metadata-keys"
    type: "array"
    description: |
      An array of strings corresponding to `metadata` keys that can be modified.
    value: |
      "selected",
      "replication-method",
      "replication-key"

examples:
  - type: "Database source"
    code: |
      {
        "schema": "{\"definitions\":{\"sdc_recursive_boolean_array\":{\"items\":{\"$ref\":\"#/definitions/sdc_recursive_boolean_array\"},\"type\":[\"null\",\"boolean\",\"array\"]},\"sdc_recursive_integer_array\":{\"items\":{\"$ref\":\"#/definitions/sdc_recursive_integer_array\"},\"type\":[\"null\",\"integer\",\"array\"]},\"sdc_recursive_number_array\":{\"items\":{\"$ref\":\"#/definitions/sdc_recursive_number_array\"},\"type\":[\"null\",\"number\",\"array\"]},\"sdc_recursive_timestamp_array\":{\"format\":\"date-time\",\"items\":{\"$ref\":\"#/definitions/sdc_recursive_timestamp_array\"},\"type\":[\"null\",\"string\",\"array\"]},\"sdc_recursive_object_array\":{\"items\":{\"$ref\":\"#/definitions/sdc_recursive_object_array\"},\"type\":[\"null\",\"object\",\"array\"]},\"sdc_recursive_string_array\":{\"items\":{\"$ref\":\"#/definitions/sdc_recursive_string_array\"},\"type\":[\"null\",\"string\",\"array\"]}},\"type\":\"object\",\"properties\":{\"age\":{\"maximum\":2147483647,\"type\":[\"null\",\"integer\"],\"minimum\":-2147483648},\"has_magic\":{\"type\":[\"null\",\"boolean\"]},\"name\":{\"type\":[\"null\",\"string\"]},\"id\":{\"maximum\":2147483647,\"type\":[\"integer\"],\"minimum\":-2147483648}}}",
        "metadata": [
          {
            "breadcrumb": [
              "properties",
              "age"
            ],
            "metadata": {
              "sql-datatype": "integer",
              "selected-by-default": true,
              "inclusion": "available"
            }
          },
          {
            "breadcrumb": [],
            "metadata": {
              "database-name": "demni2mf59dt10",
              "schema-name": "public",
              "table-key-properties": [
                "id"
              ],
              "row-count": 0,
              "is-view": false
            }
          },
          {
            "breadcrumb": [
              "properties",
              "id"
            ],
            "metadata": {
              "sql-datatype": "integer",
              "selected-by-default": true,
              "inclusion": "automatic"
            }
          },
          {
            "breadcrumb": [
              "properties",
              "name"
            ],
            "metadata": {
              "sql-datatype": "text",
              "selected-by-default": true,
              "inclusion": "available"
            }
          },
          {
            "breadcrumb": [
              "properties",
              "has_magic"
            ],
            "metadata": {
              "sql-datatype": "boolean",
              "selected-by-default": true,
              "inclusion": "available"
            }
          }
        ],
        "non-discoverable-metadata-keys": [
          "selected",
          "replication-method",
          "replication-key",
          "view-key-properties"
        ]
      }

  - type: "SaaS source"
    code: |
      {
        "schema": "{\"type\":\"object\",\"properties\":{\"id\":{\"type\":[\"null\",\"integer\"]},\"sort_value\":{\"type\":[\"null\",\"string\"]},\"product_id\":{\"type\":[\"null\",\"integer\"]},\"updated_at\":{\"type\":[\"null\",\"string\"],\"format\":\"date-time\"},\"featured\":{\"type\":[\"null\",\"boolean\"]},\"position\":{\"type\":[\"null\",\"integer\"]},\"created_at\":{\"type\":[\"null\",\"string\"],\"format\":\"date-time\"},\"collection_id\":{\"type\":[\"null\",\"integer\"]}}}",
        "metadata": [
          {
            "breadcrumb": [
              "properties",
              "sort_value"
            ],
            "metadata": {
              "selected": false,
              "inclusion": "available"
            }
          },
          {
            "breadcrumb": [],
            "metadata": {
              "selected": true,
              "valid-replication-keys": [
                "updated_at"
              ],
              "table-key-properties": [
                "id"
              ],
              "forced-replication-method": "INCREMENTAL"
            }
          },
          {
            "breadcrumb": [
              "properties",
              "position"
            ],
            "metadata": {
              "selected": false,
              "inclusion": "available"
            }
          },
          {
            "breadcrumb": [
              "properties",
              "id"
            ],
            "metadata": {
              "selected": false,
              "inclusion": "automatic"
            }
          },
          {
            "breadcrumb": [
              "properties",
              "collection_id"
            ],
            "metadata": {
              "selected": true,
              "inclusion": "available"
            }
          },
          {
            "breadcrumb": [
              "properties",
              "featured"
            ],
            "metadata": {
              "selected": false,
              "inclusion": "available"
            }
          },
          {
            "breadcrumb": [
              "properties",
              "product_id"
            ],
            "metadata": {
              "selected": false,
              "inclusion": "available"
            }
          },
          {
            "breadcrumb": [
              "properties",
              "created_at"
            ],
            "metadata": {
              "selected": false,
              "inclusion": "available"
            }
          },
          {
            "breadcrumb": [
              "properties",
              "updated_at"
            ],
            "metadata": {
              "selected": false,
              "inclusion": "automatic"
            }
          }
        ],
        "non-discoverable-metadata-keys": [
          "selected",
          "replication-method",
          "replication-key",
          "view-key-properties"
        ]
      }
---