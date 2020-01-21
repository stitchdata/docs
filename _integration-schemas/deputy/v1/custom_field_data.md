---
tap: "deputy"
version: "1"
key: "custom-field-data"

name: "custom_field_data"
doc-link: "https://www.deputy.com/api-doc/Resources/CustomFieldData"

description: |
  The `{{ table.name }}` table contains info about custom field data.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The custom field data ID."
    foreign-key-id: "custom-field-data-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the was last modified."

  - name: "System"
    type: "string"
    description: ""

  - name: "F01"
    type: "string"
    description: ""

  - name: "F02"
    type: "string"
    description: ""

  - name: "F03"
    type: "string"
    description: ""

  - name: "F04"
    type: "string"
    description: ""

  - name: "F05"
    type: "string"
    description: ""

  - name: "F06"
    type: "string"
    description: ""

  - name: "F07"
    type: "string"
    description: ""

  - name: "F08"
    type: "string"
    description: ""

  - name: "F09"
    type: "string"
    description: ""

  - name: "F10"
    type: "string"
    description: ""

  - name: "F11"
    type: "string"
    description: ""

  - name: "F12"
    type: "string"
    description: ""

  - name: "F13"
    type: "string"
    description: ""

  - name: "F14"
    type: "string"
    description: ""

  - name: "F15"
    type: "string"
    description: ""

  - name: "F16"
    type: "string"
    description: ""

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---