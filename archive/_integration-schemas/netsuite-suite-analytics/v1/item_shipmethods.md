---
tap: "netsuite-suite-analytics"
version: "1"
key: "item-shipmethod"

name: "item_shipmethods"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/item_shipmethods.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "is_default"
    type: "string"
    description: ""

  - name: "item_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "shipmethod_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
---