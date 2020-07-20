---
tap: "netsuite-suite-analytics"
version: "1"
key: "posting-account-activity"

name: "posting_account_activity"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/posting_account_activity.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

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