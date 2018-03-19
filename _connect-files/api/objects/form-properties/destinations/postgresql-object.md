---
content-type: "api-form"
form-type: "destination"
key: "destination-form-properties-postgresql-object"

title: "PostgreSQL Destination Form Property"
description: "{{ api.form-properties.destination-forms.postgresql.description }}"

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

examples:
  - code: |
      {
         "connection":{
            "host":"postgres.some-host.com",
            "port":5432,
            "database":"stitch",
            "username":"stitch_user",
            "password":"<PASSWORD>",
            "ssl":true
         }
      }
---