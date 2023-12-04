---
tap: "netsuite-suite-analytics"
version: "1"
key: "expense-detail"

name: "expense_detail"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/expense_detail.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "amount"
    type: "number"
    description: ""

  - name: "currency_id"
    type: "integer"
    description: ""

  - name: "exchange_rate"
    type: "number"
    description: ""

  - name: "expense_category_id"
    type: "integer"
    description: ""

  - name: "expense_date"
    type: "date-time"
    description: ""

  - name: "expense_detail_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "foreign_amount"
    type: "number"
    description: ""

  - name: "foreign_rate"
    type: "number"
    description: ""

  - name: "has_receipt"
    type: "string"
    description: ""

  - name: "is_paid_by_corp_credit_card"
    type: "string"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "quantity"
    type: "number"
    description: ""

  - name: "rate"
    type: "number"
    description: ""

  - name: "reference_number"
    type: "integer"
    description: ""

  - name: "tax_amount"
    type: "number"
    description: ""

  - name: "transaction_id"
    type: "integer"
    description: ""

  - name: "transaction_line_id"
    type: "integer"
    description: ""
---