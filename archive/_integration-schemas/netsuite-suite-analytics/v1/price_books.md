---
tap: "netsuite-suite-analytics"
version: "1"
key: "price-book"

name: "price_books"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/pricebook.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "currency"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "plan_id"
    type: "integer"
    description: ""
    foreign-key-id: "subscription-plan-id"

  - name: "price_book_extid"
    type: "string"
    description: ""

  - name: "price_book_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "price-book-id"
---