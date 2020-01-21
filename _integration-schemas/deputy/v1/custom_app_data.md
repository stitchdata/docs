---
tap: "deputy"
version: "1"
key: "custom-app-data"

name: "custom_app_data"
doc-link: "https://www.deputy.com/api-doc/Resources/CustomAppData"

description: |
  The `{{ table.name }}` table contains info about custom app data.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The custom app data ID."
    #foreign-key-id: "custom-app-data-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the was last modified."

  - name: "DocumentId"
    type: "string"
    description: ""

  - name: "Data"
    type: "string"
    description: ""

  - name: "KeyInt"
    type: "integer"
    description: ""

  - name: "KeyString"
    type: "string"
    description: ""

  - name: "Label"
    type: "string"
    description: ""

  - name: "OperationalUnit"
    type: "integer"
    description: ""

  - name: "Employee"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Permission"
    type: "string"
    description: ""

  - name: "Deleted"
    type: "boolean"
    description: ""

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---