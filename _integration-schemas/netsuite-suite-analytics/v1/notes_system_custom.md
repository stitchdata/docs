---
tap: "netsuite-suite-analytics"
version: "1"
key: "notes-system-custom"

name: "notes_system_custom"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/notes_system_custom.html"
description: |
  From NetSuite's documentation:

  > As of NetSuite 2017.1, the `notes_system_custom` table is obsolete. Use the [`system_notes_custom` table](#system-notes-custom) instead.

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
    foreign-key-id: "entity-id"

  - name: "comments"
    type: "string"
    description: ""

  - name: "company_id"
    type: "integer"
    description: ""
    foreign-key-id: "entity-id"

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
    foreign-key-id: "item-id"

  - name: "line_id"
    type: "integer"
    description: ""
    foreign-key-id: "transaction-line-id"

  - name: "line_transaction_id"
    type: "integer"
    description: ""
    foreign-key-id: "transaction-id"

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
    foreign-key-id: "note-type-id"

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
    foreign-key-id: "transaction-id"
---