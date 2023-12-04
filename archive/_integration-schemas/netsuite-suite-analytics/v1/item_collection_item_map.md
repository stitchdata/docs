---
tap: "netsuite-suite-analytics"
version: "1"
key: "item-collection-item-map"

name: "item_collection_item_map"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/itemcollectionitemmap.html"
description: ""
replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}
  - name: "item_collection_id"
    type: "integer"
    description: ""
    foreign-key-id: "item-collection-id"

  - name: "item_collection_item_map_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""
    foreign-key-id: "item-id"
    
  - name: "item_map_extid"
    type: "string"
    description: ""
---
