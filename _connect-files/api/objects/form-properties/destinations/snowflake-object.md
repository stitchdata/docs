---
content-type: "api-form"
form-type: "destination"
key: "destination-form-properties-snowflake-object"

title: "Snowflake Destination Form Property"
api-type: "snowflake"
display-name: "Snowflake"

docs-name: "snowflake"
db-type: "snowflake"

description: ""

uses-common-fields: true
object-attributes:
  - name: "role"
    type: "string"
    required: false
    description: "The role to use."
    value: |
      "<OPTIONAL_ROLE>"

  - name: "warehouse"
    type: "string"
    required: true
    description: "The name of the Snowflake warehouse Stitch will connect to."
    value: |
      "<WAREHOUSE>"
---