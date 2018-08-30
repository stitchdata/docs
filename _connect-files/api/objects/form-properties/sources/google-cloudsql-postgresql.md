---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-cloudsql-postgresql-object"

title: "Google CloudSQL PostgreSQL Source Form Property"
api-type: "cloudsql_pg"
display-name: "Google CloudSQL PostgreSQL"
integration-type: "database"
docs-name: "cloudsql-postgres"

description: "{{ api.form-properties.source-forms.cloudsql-postgresql.description }}"

object-attributes:
  - name: "anchor_time"
    type: "string"
    required: false
    description: |
      {{ connect.common.attributes.anchor-time | replace: "[INTEGRATION]",form-property.display-name }}
    value: "{{ sample-property-data.anchor-time }}"

  - name: "host"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.host }}"
    value: "{{ sample-property-data.host }}"

  - name: "port"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.port }}"
    value: "5432"

  - name: "dbname"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.database }}"
    value: "{{ sample-property-data.database }}"

  - name: "user"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.username }}"
    value: "{{ sample-property-data.user }}"

  - name: "password"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.password }}"
    value: "{{ sample-property-data.password }}"

  - name: "{{ connect.common.attributes.include-schemas-name }}"
    type: "string"
    required: false
    description: "{{ connect.common.attributes.include-schemas-description | flatify }}"
    value: "{{ sample-property-data.include-schema }}"
---