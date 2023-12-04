---
tap: "netsuite-suite-analytics"
version: "1"
key: "transaction-shipping-group"

name: "transaction_shipping_groups"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/transaction_shipping_groups.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "handling_line_id"
    type: "integer"
    description: ""

  - name: "shipping_group_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "transaction-shipping-group-id"

  - name: "shipping_item_id"
    type: "integer"
    description: ""

  - name: "shipping_line_id"
    type: "integer"
    description: ""

  - name: "transaction_address_id"
    type: "integer"
    description: ""

  - name: "transaction_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "transaction-id"
---