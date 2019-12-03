---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "import-api"
content-type: "api-structure"
key: "message-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Message"
description: "{{ site.data.import-api.data-structures.message.description | flatify }}"
has-multiple-versions: "false"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "action"
    type: "string"
    description: "This will always be `upsert`."
    value: "upsert"

  - name: "sequence"
    type: "integer"
    description: |
      {{ general.attributes.sequence | flatify }}
    value: "1550702340229"

  - name: "data"
    type: "object"
    description: |
      The record to be upserted into a table. The record data must conform to the JSON schema contained in the request's [Schema object]({{ site.data.import-api.data-structures.schema.section }}).
    value: ""


# -------------------------- #
#          EXAMPLES          #
# -------------------------- #

examples:
  - code: |
      {
        "action": "upsert",
        "sequence": 1574796577000,
        "data": {
          "id": 1,
          "name": "Finn",
          "age": 16,
          "has_magic": false
        }
      }
---