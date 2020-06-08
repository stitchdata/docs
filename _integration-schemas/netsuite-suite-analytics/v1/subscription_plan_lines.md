---
tap: "netsuite-suite-analytics"
version: "1"
key: "subscription-plan-line"

name: "subscription_plan_lines"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/subscription_plan_lines.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "billing_mode_id"
    type: "string"
    description: ""

  - name: "is_prorate_end_date"
    type: "string"
    description: ""

  - name: "is_prorate_start_date"
    type: "string"
    description: ""

  - name: "is_required"
    type: "string"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""
    foreign-key-id: "item-id"

  - name: "parent_id"
    type: "integer"
    description: ""
    foreign-key-id: "subscription-plan-id"

  - name: "plan_line_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "subscription-plan-line-id"

  - name: "plan_line_number"
    type: "integer"
    description: ""

  - name: "plan_line_type"
    type: "string"
    description: ""

  - name: "renewal_option"
    type: "string"
    description: ""

  - name: "revenue_recognition_option_id"
    type: "string"
    description: ""

  - name: "usage_multiplier_line_id"
    type: "integer"
    description: ""
    foreign-key-id: "subscription-plan-line-id"
---