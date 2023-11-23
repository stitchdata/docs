---
tap: "netsuite-suite-analytics"
version: "1"
key: "payment-method"

name: "payment_methods"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/paymentmethod.html"
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

  - name: "default_account_id"
    type: "integer"
    description: ""

  - name: "external_0"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "payment_method_extid"
    type: "string"
    description: ""

  - name: "payment_method_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "payment-method-id"

  - name: "payment_method_tags"
    type: "string"
    description: ""
---