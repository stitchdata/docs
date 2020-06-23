---
tap: "netsuite-suite-analytics"
version: "1"
key: "notes-user"

name: "notes_user"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/notes_user.html"
description: ""

replication-method: "Key-based Incremental"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

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
    foreign-key-id: "company-id"

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

  - name: "name"
    type: "string"
    description: ""

  - name: "note_extid"
    type: "string"
    description: ""

  - name: "note_id"
    type: "integer"
    netsuite-primary-key: true
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