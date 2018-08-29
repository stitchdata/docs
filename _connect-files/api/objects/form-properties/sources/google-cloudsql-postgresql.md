---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-cloudsql-postgresql-object"

title: "Google CloudSQL PostgreSQL Source Form Property"
description: "{{ api.form-properties.source-forms.cloudsql-postgresql.description }}"

object-attributes:
  - name: "host"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.host }}"

  - name: "port"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.port }}"

  - name: "dbname"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.database }}"

  - name: "user"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.username }}"

  - name: "password"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.password }}"

  - name: "{{ connect.common.attributes.include-schemas-name }}"
    type: "string"
    required: false
    description: "{{ connect.common.attributes.include-schemas-description | flatify }}"


examples:
  - code: |
      {  
       "type":"platform.cloudsql_pg",
       "properties":{  
          "host":"cloudsql-postgresql.some-host.com",
          "port":"5432",
          "dbname":"stitch",
          "user":"stitch_user",
          "password":"<PASSWORD>",
          "{{ connect.common.attributes.include-schemas-name }}":"true"
        }
      }
---