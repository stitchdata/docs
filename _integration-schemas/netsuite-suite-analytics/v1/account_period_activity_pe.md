---
tap: "netsuite-suite-analytics"
version: "1"
key: "account-period-activity-pe"

name: "account_period_activity_pe"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/account_period_activity_pe.html"
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
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "account-id"

  - name: "accounting_book_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "accounting-book-id"

  - name: "accounting_period_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "accounting-period-id"

  - name: "amount"
    type: "integer"
    description: ""

  - name: "balance_from_subsidiary_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "subsidiary-id"

  - name: "department_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "department-id"

  - name: "is_hidden_custom_line"
    type: "string"
    description: ""

  - name: "subsidiary_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "subsidiary-id"
---