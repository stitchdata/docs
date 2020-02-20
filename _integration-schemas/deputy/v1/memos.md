---
tap: "deputy"
version: "1"
key: "memo"

name: "memos"
doc-link: "https://www.deputy.com/api-doc/Resources/Memo"

description: |
  The `{{ table.name }}` table contains info about memos.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The memo ID."
    #foreign-key-id: "memo-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the memo was last modified."

  - name: "ShowFrom"
    type: "date"
    description: ""

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "ShowTill"
    type: "date"
    description: ""

  - name: "Title"
    type: "string"
    description: ""

  - name: "Content"
    type: "string"
    description: ""

  - name: "Type"
    type: "integer"
    description: ""

  - name: "File"
    type: "integer"
    description: ""

  - name: "Url"
    type: "string"
    description: ""

  - name: "ConfirmText"
    type: "string"
    description: ""

  - name: "Keyword"
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