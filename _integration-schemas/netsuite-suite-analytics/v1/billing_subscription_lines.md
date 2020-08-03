---
tap: "netsuite-suite-analytics"
version: "1"
key: "billing-subscription-line"

name: "billing_subscription_lines"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/billing_subscription_lines.html"
description: ""

replication-method: "Key-based Incremental"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "billing_mode_id"
    type: "string"
    description: ""

  - name: "catalog_type"
    type: "string"
    description: ""

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "date_end"
    type: "date-time"
    description: ""

  - name: "date_recurrence_start"
    type: "date-time"
    description: ""

  - name: "date_start"
    type: "date-time"
    description: ""

  - name: "date_termination"
    type: "date-time"
    description: ""

  - name: "discount"
    type: "number"
    description: ""

  - name: "is_discount_percentage"
    type: "string"
    description: ""

  - name: "is_include_in_renewal"
    type: "string"
    description: ""

  - name: "is_prorate_end_date"
    type: "string"
    description: ""

  - name: "is_prorate_start_date"
    type: "string"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""
    foreign-key-id: "item-id"

  - name: "line_type"
    type: "string"
    description: ""

  - name: "period_amount"
    type: "number"
    description: ""

  - name: "price_interval_group_id"
    type: "integer"
    description: ""

  - name: "purchase_order_id"
    type: "string"
    description: ""

  - name: "quantity"
    type: "number"
    description: ""

  - name: "recurring_amount"
    type: "number"
    description: ""

  - name: "sales_order_id"
    type: "integer"
    description: ""

  - name: "sales_order_line_number"
    type: "integer"
    description: ""

  - name: "status_id"
    type: "string"
    description: ""

  - name: "subline_extid"
    type: "string"
    description: ""

  - name: "subline_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "billing-subscription-line-id"

  - name: "subline_number"
    type: "integer"
    description: ""

  - name: "subscription_id"
    type: "integer"
    description: ""
    foreign-key-id: "bililng-subscription-id"

  - name: "subscription_plan_line_id"
    type: "integer"
    description: ""
    foreign-key-id: "subscription-plan-line-id"

  - name: "usage_multiplier_line_id"
    type: "integer"
    description: ""
    foreign-key-id: "billing-subscription-line-id"
---