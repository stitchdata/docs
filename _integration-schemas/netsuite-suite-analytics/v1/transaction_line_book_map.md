---
tap: "netsuite-suite-analytics"
version: "1"
key: "transaction-line-book-map"

name: "transaction_line_book_map"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/transaction_line_book_map.html"
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

  - name: "account_id"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"

  - name: "accounting_book_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "accounting-book-id"

  - name: "alt_sales_amount"
    type: "number"
    description: ""

  - name: "amortization_residual"
    type: "string"
    description: ""

  - name: "amount"
    type: "number"
    description: ""

  - name: "amount_linked"
    type: "number"
    description: ""

  - name: "bill_variance_status"
    type: "string"
    description: ""

  - name: "catch_up_period_id"
    type: "integer"
    description: ""

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "date_rev_rec_end"
    type: "date-time"
    description: ""

  - name: "date_rev_rec_start"
    type: "date-time"
    description: ""

  - name: "date_revenue_committed"
    type: "date-time"
    description: ""

  - name: "gl_number"
    type: "string"
    description: ""

  - name: "gl_sequence"
    type: "string"
    description: ""

  - name: "gl_sequence_id"
    type: "integer"
    description: ""

  - name: "gross_amount"
    type: "integer"
    description: ""

  - name: "is_hold_rev_rec"
    type: "string"
    description: ""

  - name: "quantity_committed"
    type: "number"
    description: ""

  - name: "schedule_id"
    type: "integer"
    description: ""
    foreign-key-id: "revenue-recognition-schedule-id"

  - name: "transaction_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "transaction-id"

  - name: "transaction_line_id"
    type: "integer"
    description: ""
    foreign-key-id: "transaction-line-id"

  - name: "vsoe_allocation"
    type: "number"
    description: ""
---