---
tap: "netsuite-suite-analytics"
version: "1"
key: "item-collection"

name: "item_collections"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/itemcollection.html"
description: ""
replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}
  - name: "description"
    type: "string"
    description: ""
  - name: "is_inactive"
    type: "string"
    description: ""
  - name: "item_collection_extid"
    type: "string"
    description: ""
  - name: "item_collection_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "item-collection-id"
  - name: "name"
    type: "string"
    description: ""
---
