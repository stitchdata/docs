---
tap: "netsuite-suite-analytics"
version: "1"
key: "project-revenue-rls-charge-rls"

name: "project_revenue_rls_charge_rls"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/project_revenue_rls_charge_rls.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "actual_amount"
    type: "number"
    description: ""

  - name: "charge_rule_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "date_amount_modified"
    type: "date-time"
    description: ""

  - name: "forecast_amount"
    type: "number"
    description: ""

  - name: "project_revenue_rule_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "project-revenue-rule-id"
---