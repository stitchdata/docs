---
tap: "netsuite-suite-analytics"
version: "1"
key: "case-type"

name: "case_types"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/case_types.html"
description: |
  **Note**: This table contains the same data as the [`casetype`](#casetype) table.

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

  - name: "case_type_extid"
    type: "string"
    description: ""

  - name: "case_type_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "case-type-id"

  - name: "description"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""
---