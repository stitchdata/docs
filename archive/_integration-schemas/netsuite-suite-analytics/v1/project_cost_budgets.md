---
tap: "netsuite-suite-analytics"
version: "1"
key: "project-cost-budget"

name: "project_cost_budgets"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/project_cost_budgets.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "duration"
    type: "integer"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "term_extid"
    type: "string"
    description: ""

  - name: "term_id"
    type: "integer"
    description: ""

  - name: "term_type_id"
    type: "string"
    description: ""

  - name: "unit_id"
    type: "string"
    description: ""
---