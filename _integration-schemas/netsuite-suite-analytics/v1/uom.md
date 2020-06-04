---
tap: "netsuite-suite-analytics"
version: "1"
key: "uom"

name: "uom"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/uom.html"
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

  - name: "abbreviation"
    type: "string"
    description: ""

  - name: "conversion_rate"
    type: "number"
    description: ""

  - name: "is_base_unit"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "plural_abbreviation"
    type: "string"
    description: ""

  - name: "plural_name"
    type: "string"
    description: ""

  - name: "units_type_id"
    type: "integer"
    description: ""

  - name: "uom_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "uom-id"
---