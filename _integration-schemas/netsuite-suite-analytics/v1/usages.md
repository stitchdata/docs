---
tap: "netsuite-suite-analytics"
version: "1"
key: "usage"

name: "usages"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/usage.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "date_usage"
    type: "date-time"
    description: ""

  - name: "usage_customer_id"
    type: "integer"
    description: ""

  - name: "usage_extid"
    type: "string"
    description: ""

  - name: "usage_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "usage_item_id"
    type: "integer"
    description: ""

  - name: "usage_memo"
    type: "string"
    description: ""

  - name: "usage_quantity"
    type: "number"
    description: ""

  - name: "usage_subscription_id"
    type: "integer"
    description: ""

  - name: "usage_subscription_line_id"
    type: "integer"
    description: ""

  - name: "usage_subscription_plan_id"
    type: "integer"
    description: ""
---