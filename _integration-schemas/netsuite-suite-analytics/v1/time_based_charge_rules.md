---
tap: "netsuite-suite-analytics"
version: "1"
key: "time-based-charge-rule"

name: "time_based_charge_rules"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/time_based_charge_rules.html"
description: |
  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "adjust_time_to_fit_under_cap"
    type: "string"
    description: ""

  - name: "billing_rate_card_id"
    type: "integer"
    description: ""
    foreign-key-id: "billing-rate-card-id"

  - name: "cap_hours"
    type: "number"
    description: ""

  - name: "cap_money"
    type: "number"
    description: ""

  - name: "cap_type"
    type: "string"
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

  - name: "dont_bill_entry_exceeding_cap"
    type: "string"
    description: ""

  - name: "end_date"
    type: "date-time"
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

  - name: "rate_multiplier"
    type: "number"
    description: ""

  - name: "rate_source"
    type: "string"
    description: ""

  - name: "rounding"
    type: "string"
    description: ""

  - name: "rule_name"
    type: "string"
    description: ""

  - name: "rule_order"
    type: "integer"
    description: ""

  - name: "sale_unit_id"
    type: "integer"
    description: ""

  - name: "saved_search"
    type: "integer"
    description: ""

  - name: "start_date"
    type: "date-time"
    description: ""

  - name: "time_based_charge_rule_id"
    type: "integer"
    description: ""

  - name: "units_type_id"
    type: "integer"
    description: ""
---