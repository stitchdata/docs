---
tap: "netsuite-suite-analytics"
version: "1"
key: "project-expense-type"

name: "project_expense_types"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/projectexpensetype.html"
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

  - name: "description"
    type: "string"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "project_expense_type_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "project-expense-type-id"
---