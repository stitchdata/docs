---
tap: "netsuite-suite-analytics"
version: "1"
key: "fair-value-price"

name: "fair_value_prices"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/fairvalueprice.html"
description: |
  {{ integration.append-only-loading | flatify }}

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

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "end_date"
    type: "date-time"
    description: ""

  - name: "fair_value_formula"
    type: "string"
    description: ""

  - name: "fair_value_price_extid"
    type: "string"
    description: ""

  - name: "fair_value_price_id"
    type: "integer"
    description: ""

  - name: "fair_value_range_policy"
    type: "string"
    description: ""

  - name: "high_value"
    type: "string"
    description: ""

  - name: "is_vsoe"
    type: "string"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""

  - name: "item_revenue_category"
    type: "string"
    description: ""

  - name: "low_value"
    type: "string"
    description: ""

  - name: "start_date"
    type: "date-time"
    description: ""

  - name: "unit_id"
    type: "integer"
    description: ""

  - name: "unit_price"
    type: "number"
    description: ""

  - name: "units_type_id"
    type: "integer"
    description: ""
---