---
tap: "netsuite-suite-analytics"
version: "1"
key: "budget-category"

name: "budget_category"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/budgetcategory.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "budget_category_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "budget-category-id"

  - name: "is_global"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""
---