---
tap: "netsuite-suite-analytics"
version: "1"
key: "fixed-fee-charge-rule"

name: "fixed_fee_charge_rules"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/fixed_fee_charge_rules.html"
description: |
  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "amount"
    type: "number"
    description: ""

  - name: "billing_item"
    type: "integer"
    description: ""

  - name: "charge_rule_id"
    type: "integer"
    description: ""

  - name: "charge_rule_type"
    type: "string"
    description: ""

  - name: "charge_stage"
    type: "string"
    description: ""

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "end_date"
    type: "date-time"
    description: ""

  - name: "external_id"
    type: "string"
    description: ""

  - name: "fixed_fee_charge_rule_id"
    type: "integer"
    description: ""

  - name: "form_template"
    type: "integer"
    description: ""

  - name: "frequency"
    type: "string"
    description: ""

  - name: "period"
    type: "integer"
    description: ""

  - name: "project_id"
    type: "integer"
    description: ""

  - name: "project_task"
    type: "integer"
    description: ""

  - name: "rule_name"
    type: "string"
    description: ""

  - name: "start_date"
    type: "date-time"
    description: ""
---