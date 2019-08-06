---
tap: "deputy"
version: "1.0"
key: "comment"

name: "comments"
doc-link: "https://www.deputy.com/api-doc/Resources/Comment"

description: |
  The `{{ table.name }}` table contains info about comments.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The comment ID."
    #foreign-key-id: "comment-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the comment was last modified."

  - name: "Orm"
    type: "string"
    description: ""

  - name: "RecId"
    type: "integer"
    description: ""

  - name: "InFeed"
    type: "boolean"
    description: ""

  - name: "IgnorePermission"
    type: "boolean"
    description: ""
  
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