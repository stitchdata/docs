---
content-type: "api-form"
form-type: "destination"
key: "destination-form-properties-snowflake-object"

title: "Snowflake"
description: "{{ api.form-properties.destination-forms.snowflake.description }}"

object-attributes:
  - name: "host"
    type: "string"
    description: "{{ connect.common.attributes.host }}"

  - name: "port"
    type: "integer"
    description: "{{ connect.common.attributes.port }}"

  - name: "database"
    type: "string"
    description: "{{ connect.common.attributes.database }}"

  - name: "username"
    type: "string"
    description: "{{ connect.common.attributes.username }}"

  - name: "password"
    type: "string"
    description: "{{ connect.common.attributes.password }}"

  - name: "ssl"
    type: "boolean"
    description: "{{ connect.common.attributes.ssl }}"

  - name: "role"
    type: "string"
    description: "**Optional**: The role to use."

examples:
  - code: |
      {
         "connection":{
            "host":"some-thing.snowflakecomputing.com",
            "port":443,
            "warehouse": "stitch_warehouse",
            "database":"stitch",
            "username":"stitch_user",
            "password":"<PASSWORD>",
            "role":"optional_role"
         }
      }
---