---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-cloudsql-mysql-object"

title: "Google CloudSQL MySQL Source Form Property"
api-type: "cloudsql-mysql"
display-name: "Google CloudSQL MySQL"
integration-type: "database"
docs-name: "cloudsql-mysql"

description: "{{ api.form-properties.source-forms.cloudsql-mysql.description }}"

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
    value: "3306"

  - name: "database"
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
---