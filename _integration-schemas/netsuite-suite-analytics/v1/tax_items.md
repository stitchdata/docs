---
tap: "netsuite-suite-analytics"
version: "1"
key: "tax-item"

name: "tax_items"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/tax_items.html"
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

  - name: "description"
    type: "string"
    description: ""

  - name: "full_name"
    type: "string"
    description: ""

  - name: "income_account_id"
    type: "integer"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "item_extid"
    type: "string"
    description: ""

  - name: "item_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "tax-item-id"

  - name: "name"
    type: "string"
    description: ""

  - name: "parent_id"
    type: "integer"
    description: ""

  - name: "rate"
    type: "string"
    description: ""

  - name: "tax_city"
    type: "string"
    description: ""

  - name: "tax_county"
    type: "string"
    description: ""

  - name: "tax_state"
    type: "string"
    description: ""

  - name: "tax_type_id"
    type: "integer"
    description: ""

  - name: "tax_zipcode"
    type: "string"
    description: ""

  - name: "vendor_id"
    type: "integer"
    description: ""

  - name: "vendorname"
    type: "string"
    description: ""
---