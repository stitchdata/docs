---
tap: "netsuite-suite-analytics"
version: "1"
key: "revenue-plan-line"

name: "revenue_plan_lines"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/revenue_plan_lines.html"
description: |
  From NetSuite's documentation:

  > This table’s data is available only to NetSuite accounts that have Advanced Revenue Management enabled.

  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"
loading-behavior: "Append-Only"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "accounting_period_id"
    type: "integer"
    description: ""
    foreign-key-id: "accounting-period-id"

  - name: "amount"
    type: "number"
    description: ""

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "deferral_account_id"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"

  - name: "is_recognized"
    type: "string"
    description: ""

  - name: "journal_id"
    type: "integer"
    description: ""
    foreign-key-id: "transaction-id"

  - name: "plan_id"
    type: "integer"
    description: ""
    foreign-key-id: "revenue-plan-id"

  - name: "planned_revenue_type"
    type: "string"
    description: ""

  - name: "recognition_account_id"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"
---