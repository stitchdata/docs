---
tap: "netsuite-suite-analytics"
version: "1"
key: "address-book"

name: "address_book"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/address_book.html"
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

  - name: "address"
    type: "string"
    description: ""

  - name: "address_book_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "address-book-id"

  - name: "address_id"
    type: "integer"
    description: ""
    foreign-key-id: "address-id"

  - name: "address_line_1"
    type: "string"
    description: ""

  - name: "address_line_2"
    type: "string"
    description: ""

  - name: "address_line_3"
    type: "string"
    description: ""

  - name: "attention"
    type: "string"
    description: ""

  - name: "city"
    type: "string"
    description: ""

  - name: "company"
    type: "string"
    description: ""

  - name: "country"
    type: "string"
    description: ""

  - name: "entity_id"
    type: "integer"
    description: ""

  - name: "is_default_bill_address"
    type: "string"
    description: ""

  - name: "is_default_ship_address"
    type: "string"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "phone"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "zip"
    type: "string"
    description: ""
---