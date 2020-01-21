---
tap: "deputy"
version: "1"
key: "training-record"

name: "training_records"
doc-link: "https://www.deputy.com/api-doc/Resources/TrainingRecord"

description: |
  The `{{ table.name }}` table contains info about training records.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The training record ID."
    #foreign-key-id: "training-record-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the training record was last modified."

  - name: "Employee"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Module"
    type: "integer"
    description: ""
    foreign-key-id: "training-module-id"

  - name: "TrainingDate"
    type: "date"
    description: ""

  - name: "ExpiryDate"
    type: "date"
    description: ""

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "Comment"
    type: "string"
    description: ""

  - name: "File"
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