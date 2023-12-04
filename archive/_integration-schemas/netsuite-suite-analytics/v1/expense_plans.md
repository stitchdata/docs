---
tap: "netsuite-suite-analytics"
version: "1"
key: "expense-plan"

name: "expense_plans"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/expenseplan.html"
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

  - name: "accounting_period_id"
    type: "integer"
    description: ""
    foreign-key-id: "accounting-period-id"

  - name: "comments"
    type: "string"
    description: ""

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "end_date"
    type: "date-time"
    description: ""

  - name: "expense_plan_status"
    type: "string"
    description: ""

  - name: "expense_plan_type"
    type: "string"
    description: ""

  - name: "expense_rule_id"
    type: "integer"
    description: ""
    foreign-key-id: "expense-rule-id"

  - name: "is_hold_expense"
    type: "string"
    description: ""

  - name: "plan_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "expense-plan-id"

  - name: "plan_number"
    type: "string"
    description: ""

  - name: "reforecast_method"
    type: "string"
    description: ""

  - name: "related_revenue_arrangement_id"
    type: "integer"
    description: ""
    foreign-key-id: "transaction-id"

  - name: "related_revenue_element_id"
    type: "integer"
    description: ""
    foreign-key-id: "revenue-element-id"

  - name: "residual"
    type: "number"
    description: ""

  - name: "start_date"
    type: "date-time"
    description: ""

  - name: "transaction_book_id"
    type: "integer"
    description: ""
    foreign-key-id: "accounting-book-id"

  - name: "transaction_doc_id"
    type: "integer"
    description: ""
    foreign-key-id: "transaction-id"

  - name: "transaction_line_id"
    type: "integer"
    description: ""
    foreign-key-id: "transaction-line-id"
---