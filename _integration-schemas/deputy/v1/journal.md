---
tap: "deputy"
version: "1"
key: "journal"

name: "journal"
doc-link: "https://www.deputy.com/api-doc/Resources/Journal"

description: |
  The `{{ table.name }}` table contains info about journals.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The journal ID."
    #foreign-key-id: "journal-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the journal was last modified."

  - name: "Date"
    type: "date"
    description: ""

  - name: "EmployeeId"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Comment"
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