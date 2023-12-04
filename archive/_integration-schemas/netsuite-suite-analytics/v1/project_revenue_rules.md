---
tap: "netsuite-suite-analytics"
version: "1"
key: "project-revenue-rule"

name: "project_revenue_rules"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/project_revenue_rules.html"
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

  - name: "billing_rate_card_id"
    type: "integer"
    description: ""
    foreign-key-id: "billing-rate-card-id"

  - name: "created_by"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "date_created"
    type: "date-time"
    description: ""
  
  - name: "description"
    type: "string"
    description: ""

  - name: "fixed_amount_type"
    type: "string"
    description: ""

  - name: "fixed_schedule_type"
    type: "string"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "is_revenue_reconciled"
    type: "string"
    description: ""

  - name: "last_modified_by"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "project_id"
    type: "integer"
    description: ""
    foreign-key-id: "customer-id"

  - name: "project_revenue_rule_extid"
    type: "string"
    description: ""

  - name: "project_revenue_rule_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "project-revenue-rule-id"

  - name: "rate_multiplier"
    type: "number"
    description: ""

  - name: "rate_source_type_id"
    type: "string"
    description: ""

  - name: "recurrence_end_date"
    type: "date-time"
    description: ""

  - name: "recurrence_frequency"
    type: "string"
    description: ""

  - name: "recurrence_period"
    type: "integer"
    description: ""

  - name: "recurrence_start_date"
    type: "date-time"
    description: ""

  - name: "rounding_type_id"
    type: "string"
    description: ""

  - name: "rule_name"
    type: "string"
    description: ""

  - name: "rule_type_id"
    type: "string"
    description: ""

  - name: "saved_search_id"
    type: "integer"
    description: ""

  - name: "service_item_id"
    type: "integer"
    description: ""
    foreign-key-id: "service-item-id"
---