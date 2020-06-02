---
tap: "netsuite-suite-analytics"
version: "1"
key: "transaction-tax-detail"

name: "transaction_tax_detail"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/transaction_tax_detail.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "account_id"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"

  - name: "amount"
    type: "number"
    description: ""

  - name: "amount_foreign"
    type: "number"
    description: ""

  - name: "amount_net"
    type: "number"
    description: ""

  - name: "calculation_comment"
    type: "string"
    description: ""

  - name: "tax_basis_amount"
    type: "integer"
    description: ""

  - name: "tax_item_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "tax-item-id"

  - name: "tax_rate"
    type: "number"
    description: ""

  - name: "tax_type"
    type: "string"
    description: ""

  - name: "transaction_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "transaction-id"

  - name: "transaction_line_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "transaction-line-id"
---