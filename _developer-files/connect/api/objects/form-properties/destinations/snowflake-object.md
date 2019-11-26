---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "destination"
key: "destination-form-properties-snowflake-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Snowflake Destination Form Property"
api-type: "snowflake"
display-name: "Snowflake"

docs-name: "snowflake"
db-type: "snowflake"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-common-fields: true
## See these fields in _data/connect/common/destination-forms.yml > all-destinations

object-attributes:
  - name: "role"
    type: "string"
    required: false
    read-only: false
    description: "The role to use."
    value: |
      "<OPTIONAL_ROLE>"

  - name: "warehouse"
    type: "string"
    required: true
    read-only: false
    description: "The name of the Snowflake warehouse Stitch will connect to."
    value: |
      "<WAREHOUSE>"
---