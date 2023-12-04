---
tap: "netsuite-suite-analytics"
version: "1"
key: "payment-term"

name: "payment_terms"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/payment_terms.html"
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

  - name: "date_driven"
    type: "string"
    description: ""
  
  - name: "days_till_1st_payment"
    type: "integer"
    description: ""

  - name: "days_until_due"
    type: "integer"
    description: ""

  - name: "discount_days"
    type: "integer"
    description: ""

  - name: "frequency_id"
    type: "string"
    description: ""

  - name: "installment_count"
    type: "integer"
    description: ""

  - name: "is_installment"
    type: "string"
    description: ""

  - name: "is_preferred"
    type: "string"
    description: ""

  - name: "is_split_evenly"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "minimum_days"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "payment_terms_extid"
    type: "string"
    description: ""

  - name: "payment_terms_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "payment-term-id"

  - name: "percentage_discount"
    type: "number"
    description: ""

  - name: "repeat_every"
    type: "integer"
    description: ""
---