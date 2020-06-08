---
tap: "netsuite-suite-analytics"
version: "1"
key: "expense-account"

name: "expense_accounts"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/expense_accounts.html"
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

  - name: "account_number"
    type: "string"
    description: ""

  - name: "comments"
    type: "string"
    description: ""

  - name: "current_balance"
    type: "integer"
    description: ""

  - name: "desription"
    type: "string"
    description: ""

  - name: "expense_account_extid"
    type: "string"
    description: ""

  - name: "expense_account_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "account-id"

  - name: "full_name"
    type: "string"
    description: ""

  - name: "is_including_child_subs"
    type: "string"
    description: ""

  - name: "is_summary"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "legal_name"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "parent_id"
    type: "integer"
    description: ""
---