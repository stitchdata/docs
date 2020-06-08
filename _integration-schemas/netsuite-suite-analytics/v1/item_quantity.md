---
tap: "netsuite-suite-analytics"
version: "1"
key: "item-quantity"

name: "item_quantity"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/item_quantity.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "item_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "item_quantity_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "max_count"
    type: "number"
    description: ""

  - name: "min_count"
    type: "number"
    description: ""
---