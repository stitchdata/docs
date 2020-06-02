---
tap: "netsuite-suite-analytics"
version: "1"
key: "transaction-address"

name: "transaction_address"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/transaction_address.html"
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

  - name: "bill_address_line_1"
    type: "string"
    description: ""

  - name: "bill_address_line_2"
    type: "string"
    description: ""

  - name: "bill_address_line_3"
    type: "string"
    description: ""

  - name: "bill_city"
    type: "string"
    description: ""

  - name: "bill_company"
    type: "string"
    description: ""

  - name: "bill_country"
    type: "string"
    description: ""

  - name: "bill_name"
    type: "string"
    description: ""

  - name: "bill_phone_number"
    type: "string"
    description: ""

  - name: "bill_state"
    type: "string"
    description: ""

  - name: "bill_zip"
    type: "string"
    description: ""

  - name: "created_by_id"
    type: "integer"
    description: ""
    foreign-key-id: "entity-id"

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "last_modified_by_id"
    type: "integer"
    description: ""
    foreign-key-id: "entity-id"

  - name: "return_address_line_1"
    type: "string"
    description: ""

  - name: "return_address_line_2"
    type: "string"
    description: ""

  - name: "return_city"
    type: "string"
    description: ""

  - name: "return_country"
    type: "string"
    description: ""

  - name: "return_state"
    type: "string"
    description: ""

  - name: "return_zipcode"
    type: "string"
    description: ""

  - name: "ship_address_line_1"
    type: "string"
    description: ""

  - name: "ship_address_line_2"
    type: "string"
    description: ""

  - name: "ship_address_line_3"
    type: "string"
    description: ""

  - name: "ship_attention"
    type: "string"
    description: ""

  - name: "ship_city"
    type: "string"
    description: ""

  - name: "ship_company"
    type: "string"
    description: ""

  - name: "ship_country"
    type: "string"
    description: ""

  - name: "ship_name"
    type: "string"
    description: ""

  - name: "ship_phone_number"
    type: "string"
    description: ""

  - name: "ship_state"
    type: "string"
    description: ""

  - name: "ship_zip"
    type: "string"
    description: ""

  - name: "transaction_address_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "transaction_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "transaction-id"
---