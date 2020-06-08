---
tap: "netsuite-suite-analytics"
version: "1"
key: "project-revenue-rl-plan"

name: "project_revenue_rl_plans"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/project_revenue_rl_plans.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}
  - name: "date_recognized"
    type: "date-time"
    description: ""
  - name: "fixed_amount"
    type: "number"
    description: ""
  - name: "percent_from_total"
    type: "number"
    description: ""
  - name: "project_revenue_rl_plan_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
  - name: "project_revenue_rule_id"
    type: "integer"
    description: ""
    foreign-key-id: "project-revenue-rule-id"
  - name: "project_task_id"
    type: "integer"
    description: ""
---