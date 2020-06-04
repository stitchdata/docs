---
tap: "netsuite-suite-analytics"
version: "1"
key: "partner-type"

name: "partner_types"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/partner_types.html"
description: |
  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "parent_id"
    type: "integer"
    description: ""

  - name: "partner_id"
    type: "integer"
    description: ""

  - name: "partner_type_extid"
    type: "string"
    description: ""

  - name: "partner_type_id"
    type: "integer"
    description: ""
---