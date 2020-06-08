---
tap: "netsuite-suite-analytics"
version: "1"
key: "expense-plan-line"

name: "expense_plan_lines"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/expense_plan_lines.html"
description: |
  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"

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

  - name: "deferred_expense_account_id"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"

  - name: "expense_account_id"
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
    foreign-key-id: "expense-plan-id"

  - name: "planned_expense_type"
    type: "string"
    description: ""
---