---
content-type: "api-form"
form-type: "destination"
key: "destination-form-properties-snowflake-object"

title: "Snowflake Destination Form Property"
description: "{{ api.form-properties.destination-forms.snowflake.description }}"

object-attributes:
  - name: "host"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.host }}"

  - name: "port"
    type: "integer"
    required: true
    description: "{{ connect.common.attributes.port }}"

  - name: "database"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.database }}"

  - name: "username"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.username }}"

  - name: "password"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.password }}"

  - name: "ssl"
    type: "boolean"
    required: false
    description: "{{ connect.common.attributes.ssl }}"

  - name: "role"
    type: "string"
    required: false
    description: "The role to use."

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