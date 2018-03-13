---
content-type: "api-form"
form-type: "destination"
key: "destination-form-properties-postgresql-object"

title: "PostgreSQL"
description: "{{ api.form-properties.destination-forms.postgresql.description }}"

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