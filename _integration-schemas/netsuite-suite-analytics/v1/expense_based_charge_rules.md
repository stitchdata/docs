---
tap: "netsuite-suite-analytics"
version: "1"
key: "expense-based-charge-rules"

name: "expense_based_charge_rules"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/expense_based_charge_rules.html"
description: |
  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"
loading-behavior: "Append-Only"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

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

  - name: "expense_amount_multiplier"
    type: "number"
    description: ""

  - name: "expense_based_charge_rule_id"
    type: "integer"
    description: ""

  - name: "expense_saved_search"
    type: "integer"
    description: ""

  - name: "external_id"
    type: "string"
    description: ""

  - name: "form_template"
    type: "integer"
    description: ""

  - name: "project_id"
    type: "integer"
    description: ""

  - name: "rule_name"
    type: "string"
    description: ""

  - name: "rule_order"
    type: "integer"
    description: ""
---