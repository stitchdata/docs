---
tap: "netsuite-suite-analytics"
version: "1"
key: "unit-type"

name: "units_type"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/unitstype.html"
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

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "units_type_extid"
    type: "string"
    description: ""

  - name: "units_type_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "unit-type-id"
---