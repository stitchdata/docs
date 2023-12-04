---
tap: "netsuite-suite-analytics"
version: "1"
key: "revenue-plan"

name: "revenue_plans"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/revenueplan.html"
description: |
  From NetSuite's documentation:

  >  This table’s data is available only to NetSuite accounts that have Advanced Revenue Management enabled.

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

  - name: "accounting_period_id"
    type: "integer"
    description: ""
    foreign-key-id: "accounting-period-id"

  - name: "comments"
    type: "string"
    description: ""

  - name: "created_from"
    type: "string"
    description: ""

  - name: "creation_triggered_by"
    type: "string"
    description: ""

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "end_date"
    type: "date-time"
    description: ""

  - name: "is_hold_rev_rec"
    type: "string"
    description: ""

  - name: "plan_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "revenue-plan-id"

  - name: "plan_number"
    type: "string"
    description: ""

  - name: "reforecast_method"
    type: "string"
    description: ""

  - name: "rev_rec_rule_id"
    type: "integer"
    description: ""
    foreign-key-id: "revenue-recognition-rule-id"

  - name: "revenue_element_id"
    type: "integer"
    description: ""
    foreign-key-id: "revenue-element-id"

  - name: "revenue_plan_status"
    type: "string"
    description: ""

  - name: "revenue_plan_type"
    type: "string"
    description: ""

  - name: "start_date"
    type: "date-time"
    description: ""
---