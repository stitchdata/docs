---
tap: "netsuite-suite-analytics"
version: "1"
key: "posting-account-activity-pe"

name: "posting_account_activity_pe"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/posting_account_activity_pe.html"
description: |
  From NetSuite's documentation:

  > This table includes all transactions. Note that when the ID of the `balance_from_subsidiary_id` and the `subsidiary_id` fields are different, the Period End Journal transaction represents transactions from the source subsidiary. When both fields have the same ID, the Period End Journal transaction represents transactions from the posting subsidiary.

replication-method: "Full Table"

attributes:
  - name: "account_id"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"

  - name: "accounting_book_id"
    type: "integer"
    description: ""
    foreign-key-id: "accounting-book-id"

  - name: "accounting_period_id"
    type: "integer"
    description: ""
    foreign-key-id: "accounting-period-id"

  - name: "activity_date"
    type: "date-time"
    description: ""

  - name: "amount"
    type: "number"
    description: ""

  - name: "amount_foreign"
    type: "number"
    description: ""

  - name: "balance_from_subsidiary_id"
    type: "integer"
    description: ""

  - name: "class_id"
    type: "integer"
    description: ""
    foreign-key-id: "class-id"

  - name: "department_id"
    type: "integer"
    description: ""
    foreign-key-id: "department-id"

  - name: "entity_id"
    type: "integer"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""
    foreign-key-id: "item-id"

  - name: "location_id"
    type: "integer"
    description: ""
    foreign-key-id: "location-id"

  - name: "partner_id"
    type: "integer"
    description: ""
    foreign-key-id: "partner-id"

  - name: "promotion_code_id"
    type: "integer"
    description: ""
    foreign-key-id: "promotion-code-id"

  - name: "quantity"
    type: "number"
    description: ""

  - name: "sales_rep_id"
    type: "integer"
    description: ""
    foreign-key-id: "sales-rep-id"

  - name: "subsidiary_id"
    type: "integer"
    description: ""
    foreign-key-id: "subsidiary-id"
---