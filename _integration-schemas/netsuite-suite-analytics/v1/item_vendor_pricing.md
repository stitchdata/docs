---
tap: "netsuite-suite-analytics"
version: "1"
key: "item-vendor-pricing"

name: "item_vendor_pricing"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/item_vendor_pricing.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "cost_0"
    type: "number"
    description: ""

  - name: "cost_is_percentage"
    type: "string"
    description: ""

  - name: "currency_id"
    type: "integer"
    description: ""
    foreign-key-id: "currency-id"

  - name: "item_id"
    type: "integer"
    description: ""
    foreign-key-id: "item-id"

  - name: "subsidiary_id"
    type: "integer"
    description: ""
    foreign-key-id: "subsidiary-id"

  - name: "vendor_id"
    type: "integer"
    description: ""
    foreign-key-id: "vendor-id"
---