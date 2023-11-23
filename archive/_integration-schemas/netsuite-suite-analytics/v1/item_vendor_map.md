---
tap: "netsuite-suite-analytics"
version: "1"
key: "item-vendor-map"

name: "item_vendor_map"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/item_vendor_map.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "is_preferred"
    type: "string"
    description: ""

  - name: "item_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "item-id"

  - name: "subsidiary_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "subsidiary-id"

  - name: "vendor_code"
    type: "string"
    description: ""

  - name: "vendor_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "vendor-id"
---