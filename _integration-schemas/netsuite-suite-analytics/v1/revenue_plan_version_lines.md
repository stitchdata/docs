---
tap: "netsuite-suite-analytics"
version: "1"
key: "revenue-plan-version-line"

name: "revenue_plan_version_lines"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/revenue_plan_version_lines.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "accounting_period_id"
    type: "integer"
    description: ""
    foreign-key-id: "accounting-period-id"

  - name: "amount"
    type: "number"
    description: ""

  - name: "comments"
    type: "string"
    description: ""

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "deferral_account_id"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"

  - name: "journal_id"
    type: "integer"
    description: ""
    foreign-key-id: "transaction-id"

  - name: "plan_version_id"
    type: "integer"
    description: ""
    foreign-key-id: "revenue-plan-version-id"

  - name: "planned_revenue_type"
    type: "string"
    description: ""

  - name: "recognition_account_id"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"
---