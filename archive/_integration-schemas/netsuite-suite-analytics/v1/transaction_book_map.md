---
tap: "netsuite-suite-analytics"
version: "1"
key: "transaction-book-map"

name: "transaction_book_map"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/transaction_book_map.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "accounting_book_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "accounting-book-id"

  - name: "date_revenue_committed"
    type: "date-time"
    description: ""

  - name: "exchange_rate"
    type: "number"
    description: ""

  - name: "is_vsoe_bundle"
    type: "string"
    description: ""

  - name: "needs_revenue_commitment"
    type: "string"
    description: ""

  - name: "revenue_commitment_status"
    type: "string"
    description: ""

  - name: "revenue_status"
    type: "string"
    description: ""

  - name: "transaction_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "transaction-id"
---