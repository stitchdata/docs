---
tap: "deputy"
version: "1"
key: "category"

name: "categories"
doc-link: "https://www.deputy.com/api-doc/Resources/Category"

description: |
  The `{{ table.name }}` table contains info about categories.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The category ID."
    foreign-key-id: "category-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the category was last modified."

  - name: "category"
    type: "string"
    description: ""

  - name: "group"
    type: "string"
    description: ""

  - name: "SortOrder"
    type: "integer"
    description: ""

  - name: "Stafflog"
    type: "boolean"
    description: ""

  - name: "System"
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