---
tap: "netsuite-suite-analytics"
version: "1"
key: "subscription-line-revision"

name: "subscription_line_revisions"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/subscription_line_revisions.html"
description: |
  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "change_order_id"
    type: "integer"
    description: ""
    foreign-key-id: "subscription-change-order-id"

  - name: "created_by"
    type: "string"
    description: ""

  - name: "date_change_order_effective"
    type: "date-time"
    description: ""

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "delta_amount"
    type: "number"
    description: ""

  - name: "delta_quantity"
    type: "number"
    description: ""

  - name: "discount"
    type: "integer"
    description: ""

  - name: "is_applied_to_change_order"
    type: "string"
    description: ""

  - name: "is_created_from_void"
    type: "string"
    description: ""

  - name: "is_discount_percentage"
    type: "string"
    description: ""

  - name: "is_overage_discount_percentage"
    type: "string"
    description: ""

  - name: "overage_discount"
    type: "integer"
    description: ""

  - name: "overage_price_plan_id"
    type: "integer"
    description: ""
    foreign-key-id: "price-plan-id"

  - name: "price_plan_id"
    type: "integer"
    description: ""
    foreign-key-id: "price-plan-id"

  - name: "quantity"
    type: "integer"
    description: ""

  - name: "recurring_amount"
    type: "integer"
    description: ""

  - name: "revenue_element_id"
    type: "integer"
    description: ""
    foreign-key-id: "revenue-element-id"

  - name: "subscription_line_id"
    type: "integer"
    description: ""
    foreign-key-id: "billing-subscription-line-id"

  - name: "subscription_revision"
    type: "integer"
    description: ""

  - name: "total_contract_value"
    type: "number"
    description: ""
---