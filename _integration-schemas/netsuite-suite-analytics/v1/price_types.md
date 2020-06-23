---
tap: "netsuite-suite-analytics"
version: "1"
key: "price-type"

name: "price_types"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/price_tiers.html"
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

  - name: "discount_percentage"
    type: "number"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "isonline"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "price_type_extid"
    type: "string"
    description: ""

  - name: "price_type_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "price-type-id"
---