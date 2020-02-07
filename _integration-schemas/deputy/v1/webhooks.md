 ---
tap: "deputy"
version: "1"
key: "webhook"

name: "webhooks"
doc-link: "https://www.deputy.com/api-doc/Resources/Webhook"

description: |
  The `{{ table.name }}` table contains info about webhooks.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The webhook ID."
    #foreign-key-id: "webhook-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the webhook was last modified."

  - name: "Topic"
    type: "string"
    description: ""

  - name: "Address"
    type: "string"
    description: ""

  - name: "Headers"
    type: "string"
    description: ""

  - name: "Filters"
    type: "string"
    description: ""

  - name: "Type"
    type: "string"
    description: ""

  - name: "Enabled"
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