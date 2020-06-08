---
tap: "netsuite-suite-analytics"
version: "1"
key: "transaction-link"

name: "transaction_links"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/transaction_links.html"
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

  - name: "amount_foreign_linked"
    type: "number"
    description: ""

  - name: "amount_linked"
    type: "number"
    description: ""

  - name: "applied_date_posted"
    type: "date-time"
    description: ""

  - name: "applied_transaction_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "transaction-id"

  - name: "applied_transaction_line_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "transaction-line-id"

  - name: "discount"
    type: "string"
    description: ""

  - name: "inventory_number"
    type: "string"
    netsuite-primary-key: true
    description: ""

  - name: "link_type"
    type: "string"
    description: ""

  - name: "link_type_code"
    type: "string"
    netsuite-primary-key: true
    description: ""

  - name: "original_date_posted"
    type: "date-time"
    description: ""

  - name: "original_transaction_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "transaction-id"

  - name: "original_transaction_line_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "transaction-line-id"

  - name: "quantity_linked"
    type: "integer"
    description: ""
---