---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-oracle-object"

title: "Oracle Source Form Property"
api-type: "oracle"
display-name: "Oracle"

source-type: "database"
docs-name: "oracle"
db-type: "oracle"

description: ""

uses-common-fields: true
object-attributes:
  - name: "default_replication_method"
    type: "string"
    required: false
    description: "{{ connect.common.attributes.default-replication-method }}"
    value: "{{ sample-property-data.default-replication-method }}"

  - name: "filter_schemas"
    type: "string"
    required: false
    description: "[PLACEHOLDER]"
    value: ""

  - name: "sid"
    type: "string"
    required: false
    description: "[PLACEHOLDER]"
    value: ""
---