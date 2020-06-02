---
tap: "netsuite-suite-analytics"
version: "1"
key: "notes-system-custom"

name: "notes_system_custom"
doc-link: ""
description: |
  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "author_id"
    type: "integer"
    description: ""

  - name: "comments"
    type: "string"
    description: ""

  - name: "company_id"
    type: "integer"
    description: ""

  - name: "custom_field"
    type: "string"
    description: ""

  - name: "customfield_created_by"
    type: "integer"
    description: ""

  - name: "customfield_created_date"
    type: "date-time"
    description: ""

  - name: "customfield_modified_by"
    type: "integer"
    description: ""

  - name: "customfield_modified_date"
    type: "date-time"
    description: ""

  - name: "direction"
    type: "string"
    description: ""

  - name: "event_id"
    type: "integer"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""

  - name: "line_id"
    type: "integer"
    description: ""

  - name: "line_transaction_id"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "note_id"
    type: "string"
    description: ""

  - name: "note_type"
    type: "string"
    description: ""

  - name: "note_type_description"
    type: "string"
    description: ""

  - name: "note_type_extid"
    type: "string"
    description: ""

  - name: "note_type_id"
    type: "integer"
    description: ""

  - name: "record_id"
    type: "integer"
    description: ""

  - name: "record_type_id"
    type: "integer"
    description: ""

  - name: "role_id"
    type: "integer"
    description: ""

  - name: "standard_field"
    type: "string"
    description: ""

  - name: "system_use"
    type: "string"
    description: ""

  - name: "time_entered"
    type: "date-time"
    description: ""

  - name: "transaction_id"
    type: "integer"
    description: ""
---