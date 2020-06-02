---
tap: "netsuite-suite-analytics"
version: "1"
key: "customer-item-pricing"

name: "customer_item_pricing"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/customer_item_pricing.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "currency_id"
    type: "integer"
    description: ""

  - name: "customer_id"
    type: "integer"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""

  - name: "item_unit_price"
    type: "number"
    description: ""

  - name: "price_type_id"
    type: "integer"
    description: ""
---