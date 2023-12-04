---
tap: "netsuite-suite-analytics"
version: "1"
key: "currency"

name: "currencies"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/currencies.html"
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

  - name: "currency_extid"
    type: "string"
    description: ""

  - name: "currency_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "currency-id"

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "precision_0"
    type: "integer"
    description: ""

  - name: "symbol"
    type: "string"
    description: ""
---