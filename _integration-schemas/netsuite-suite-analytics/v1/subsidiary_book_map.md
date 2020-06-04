---
tap: "netsuite-suite-analytics"
version: "1"
key: "subsidiary-book-map"

name: "subsidiary_book_map"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/subsidiary_book_map.html"
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
  - name: "contract_defer_expense_acct_id"
    type: "integer"
    description: ""
  - name: "contract_expense_acct_id"
    type: "integer"
    description: ""
  - name: "currency_id"
    type: "integer"
    description: ""
  - name: "exchange_rate"
    type: "number"
    description: ""
  - name: "status"
    type: "string"
    description: ""
  - name: "subsidiary_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
---