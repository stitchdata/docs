---
tap: "netsuite-suite-analytics"
version: "1"
key: "subscription-change-order-line"

name: "subscription_co_lines"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/subscription_co_lines.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "change_order_action_id"
    type: "string"
    description: ""

  - name: "change_order_id"
    type: "integer"
    description: ""
    foreign-key-id: "subscription-change-order-id"

  - name: "discount"
    type: "integer"
    description: ""

  - name: "is_discount_percentage"
    type: "string"
    description: ""

  - name: "plan_item_id"
    type: "integer"
    description: ""
    foreign-key-id: "item-id"

  - name: "price_plan_id"
    type: "integer"
    description: ""

  - name: "quantity"
    type: "number"
    description: ""

  - name: "recurring_amount"
    type: "number"
    description: ""

  - name: "status_id"
    type: "string"
    description: ""

  - name: "subscription_id"
    type: "integer"
    description: ""
    foreign-key-id: "billing-subscription-id"

  - name: "subscription_line_id"
    type: "integer"
    description: ""
    foreign-key-id: "billing-subscription-line-id"
---