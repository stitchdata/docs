---
tap: "netsuite-suite-analytics"
version: "1"
key: "billing-class-rate"

name: "billing_class_rates"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/billing_class_rates.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "billing_class_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    # foreign-key-id: "billing-class-id"

  - name: "billing_rate_card_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    # foreign-key-id: "billing-rate-card-id"

  - name: "currency_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    # foreign-key-id: "currency-id"

  - name: "unit_price"
    type: "number"
    description: ""
---