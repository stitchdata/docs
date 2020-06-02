---
tap: "netsuite-suite-analytics"
version: "1"
key: "item-price"

name: "item_prices"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/item_prices.html"
description: ""

replication-method: "Key-based Incremental"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.
      
  - name: "currency_id"
    type: "integer"
    description: ""

  - name: "discount_pct"
    type: "number"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "isonline"
    type: "string"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""

  - name: "item_price_extid"
    type: "string"
    description: ""

  - name: "item_price_id"
    type: "integer"
    description: ""

  - name: "item_quantity_id"
    type: "integer"
    description: ""

  - name: "item_unit_price"
    type: "number"
    description: ""

  - name: "name"
    type: "string"
    description: ""
---