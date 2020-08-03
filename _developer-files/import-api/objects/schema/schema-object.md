---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "import-api"
content-type: "api-structure"
key: "schema-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Schema"
description: "{{ site.data.import-api.data-structures.schema.description | flatify }}"
has-multiple-versions: "false"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "properties"
    type: "object"
    description: |
      The JSON schema that records in the `data` property must conform to.
    value: ""
      

# -------------------------- #
#          EXAMPLES          #
# -------------------------- #

examples:
  - code: |
      {
         "schema":{
            "properties":{
               "id":{
                  "type":"integer"
               },
               "name":{
                  "type":"string"
               },
               "age":{
                  "type":"number"
               },
               "has_magic":{
                  "type":"boolean"
               }
            }
         }
      }
---