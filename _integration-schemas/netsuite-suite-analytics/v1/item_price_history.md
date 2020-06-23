---
tap: "netsuite-suite-analytics"
version: "1"
key: "item-price-history"

name: "item_price_history"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/item_price_history.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "currency_id"
    type: "integer"
    description: ""
    foreign-key-id: "currency-id"

  - name: "item_id"
    type: "integer"
    description: ""
    foreign-key-id: "item-id"

  - name: "item_quantity_id"
    type: "integer"
    description: ""

  - name: "min_count"
    type: "number"
    description: ""

  - name: "price_type_id"
    type: "integer"
    description: ""
    foreign-key-id: "price-type-id"

  - name: "unit_price"
    type: "number"
    description: ""

  - name: "version_0"
    type: "integer"
    description: ""
---