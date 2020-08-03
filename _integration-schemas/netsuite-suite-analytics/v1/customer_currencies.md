---
tap: "netsuite-suite-analytics"
version: "1"
key: "customer-currency"

name: "customer_currencies"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/customer_currencies.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "currency_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "currency-id"

  - name: "customer_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "customer-id"

  - name: "deposit_balance_foreign"
    type: "integer"
    description: ""

  - name: "openbalance_foreign"
    type: "integer"
    description: ""

  - name: "unbilled_orders_foreign"
    type: "integer"
    description: ""
---