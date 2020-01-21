---
tap: "deputy"
version: "1"
key: "custom-field"

name: "custom_fields"
doc-link: "https://www.deputy.com/api-doc/Resources/CustomField"

description: |
  The `{{ table.name }}` table contains info about 

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The custom fieldID."
    #foreign-key-id: "custom-field-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the custom field was last modified."

  - name: "System"
    type: "string"
    description: ""

  - name: "Name"
    type: "string"
    description: ""

  - name: "ApiName"
    type: "string"
    description: ""

  - name: "DeputyField"
    type: "string"
    description: ""

  - name: "SortOrder"
    type: "integer"
    description: ""

  - name: "Default"
    type: "string"
    description: ""

  - name: "Type"
    type: "integer"
    description: ""

  - name: "ValueList"
    type: "string"
    description: ""

  - name: "Validation"
    type: "string"
    description: ""

  - name: "Helptext"
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