---
tap: "netsuite-suite-analytics"
version: "1"
key: "subscription-line-price-interval"

name: "subscript_line_price_intervals"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/subscript_line_price_intervals.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "charge_frequency_id"
    type: "string"
    description: ""

  - name: "date_end_exclusive"
    type: "date-time"
    description: ""

  - name: "date_start_inclusive"
    type: "date-time"
    description: ""

  - name: "discount"
    type: "integer"
    description: ""

  - name: "included_quantity"
    type: "integer"
    description: ""

  - name: "is_discount_percentage"
    type: "string"
    description: ""

  - name: "plan_line_id"
    type: "integer"
    description: ""
    foreign-key-id: "subscription-plan-line-id"

  - name: "plan_line_number"
    type: "integer"
    description: ""

  - name: "price_plan_id"
    type: "integer"
    description: ""
    foreign-key-id: "price-plan-id"

  - name: "prorate_by"
    type: "string"
    description: ""

  - name: "quantity"
    type: "number"
    description: ""

  - name: "repeat_every"
    type: "integer"
    description: ""

  - name: "status_id"
    type: "string"
    description: ""

  - name: "subscription_line_id"
    type: "integer"
    description: ""
    foreign-key-id: "billing-subscription-line-id"
---