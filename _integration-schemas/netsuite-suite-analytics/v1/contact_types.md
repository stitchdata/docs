---
tap: "netsuite-suite-analytics"
version: "1"
key: "contact-type"

name: "contact_types"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/contact_types.html"
description: ""

replication-method: "Key-based Incremental"
loading-behavior: "Append-Only"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "contact_id"
    type: "integer"
    description: ""
    foreign-key-id: "entity-id"

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "owner_id"
    type: "integer"
    description: ""
    foreign-key-id: "entity-id"

  - name: "parent_id"
    type: "integer"
    description: ""

  - name: "shared_0"
    type: "string"
    description: ""
---