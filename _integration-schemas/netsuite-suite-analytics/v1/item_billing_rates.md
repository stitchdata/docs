---
tap: "netsuite-suite-analytics"
version: "1"
key: "item-billing-rate"

name: "item_billing_rates"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/item_billing_rates.html"
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

  - name: "billing_class_id"
    type: "integer"
    description: ""
    foreign-key-id: "billing-class-id"

  - name: "currency_id"
    type: "integer"
    description: ""
    foreign-key-id: "currency-id"

  - name: "discount_pct"
    type: "number"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "isonline"
    type: "string"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""
    foreign-key-id: "service-item-id"

  - name: "item_price_extid"
    type: "string"
    description: ""

  - name: "item_price_id"
    type: "integer"
    description: ""
    foreign-key-id: "price-type-id"

  - name: "item_unit_price"
    type: "number"
    description: ""

  - name: "name"
    type: "string"
    description: ""
---