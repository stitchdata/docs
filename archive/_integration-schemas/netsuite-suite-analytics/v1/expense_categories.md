---
tap: "netsuite-suite-analytics"
version: "1"
key: "expense-category"

name: "expense_categories"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/expense_categories.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "description"
    type: "string"
    description: ""

  - name: "expense_account_id"
    type: "integer"
    description: ""

  - name: "expense_category_extid"
    type: "string"
    description: ""

  - name: "expense_category_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "expense-category-id"

  - name: "expense_item_id"
    type: "integer"
    description: ""

  - name: "is_personal_corp_card_expense"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "rate_required"
    type: "string"
    description: ""
---