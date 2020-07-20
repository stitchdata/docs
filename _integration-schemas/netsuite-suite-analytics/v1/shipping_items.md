---
tap: "netsuite-suite-analytics"
version: "1"
key: "shipping-item"

name: "shipping_items"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/shipping_items.html"
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

  - name: "by_per_item"
    type: "integer"
    description: ""

  - name: "by_total_amount"
    type: "integer"
    description: ""

  - name: "by_weight_amount"
    type: "integer"
    description: ""

  - name: "by_weight_unit_index"
    type: "integer"
    description: ""
  
  - name: "default_unit_price"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "display_name"
    type: "string"
    description: ""

  - name: "flat_rate_amount"
    type: "integer"
    description: ""

  - name: "free_if_over_amount"
    type: "integer"
    description: ""

  - name: "free_if_overactive"
    type: "string"
    description: ""

  - name: "full_name"
    type: "string"
    description: ""

  - name: "income_account_id"
    type: "integer"
    description: ""

  - name: "is_fedex_one_rate"
    type: "string"
    description: ""

  - name: "is_omit_packaging"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "isonline"
    type: "string"
    description: ""

  - name: "istaxable"
    type: "string"
    description: ""

  - name: "item_extid"
    type: "string"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""

  - name: "maximum_shipping_amount"
    type: "integer"
    description: ""

  - name: "minimum_shipping_amount"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "parent_id"
    type: "integer"
    description: ""

  - name: "per_item_default_price"
    type: "string"
    description: ""

  - name: "pref_purchase_tax_id"
    type: "integer"
    description: ""

  - name: "shipping_cost_function"
    type: "string"
    description: ""

  - name: "shipping_rate"
    type: "integer"
    description: ""

  - name: "tax_item_id"
    type: "integer"
    description: ""

  - name: "use_maximum_ship_cost"
    type: "string"
    description: ""

  - name: "use_minimum_ship_cost"
    type: "string"
    description: ""

  - name: "vendor_id"
    type: "integer"
    description: ""
---