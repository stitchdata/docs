---
tap: "netsuite-suite-analytics"
version: "1"
key: "inventory-number"

name: "inventory_number"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/inventorynumber.html"
description: |
  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"
loading-behavior: "Append-Only"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.
      
  - name: "available_count"
    type: "integer"
    description: ""

  - name: "expiration_date"
    type: "date-time"
    description: ""

  - name: "in_transit_count"
    type: "integer"
    description: ""

  - name: "inventory_number"
    type: "string"
    description: ""

  - name: "inventory_number_id"
    type: "integer"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""

  - name: "location_id"
    type: "integer"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "number_type"
    type: "string"
    description: ""

  - name: "on_hand_count"
    type: "integer"
    description: ""

  - name: "on_order_count"
    type: "integer"
    description: ""
---