---
tap: "netsuite-suite-analytics"
version: "1"
key: "payroll-item"

name: "payroll_items"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/payrollitem.html"
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

  - name: "derived_from_payroll_item_id"
    type: "integer"
    description: ""

  - name: "derived_rate_multiplier"
    type: "number"
    description: ""

  - name: "expense_account"
    type: "integer"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "liability_account"
    type: "integer"
    description: ""

  - name: "limit_0"
    type: "number"
    description: ""

  - name: "locality"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "payroll_item_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "payroll-item-id"

  - name: "payroll_item_type_id"
    type: "integer"
    description: ""

  - name: "rate"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "tax_number"
    type: "string"
    description: ""

  - name: "vendor_id"
    type: "integer"
    description: ""

  - name: "w2_code"
    type: "string"
    description: ""
---