---
tap: "netsuite-suite-analytics"
version: "1"
key: "billing-rate-card-price"

name: "billing_rate_cards_prices"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/billing_rate_cards_prices.html"
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
    foreign-key-id: "billing-class-id"

  - name: "billing_rate_card_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "billing-rate-card-id"

  - name: "currency_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "currency-id"

  - name: "sales_unit_id"
    type: "integer"
    description: ""
    foreign-key-id: "uom-id"

  - name: "service_item_id"
    type: "integer"
    description: ""
    foreign-key-id: "item_id"

  - name: "unit_price"
    type: "integer"
    description: ""

  - name: "units_type_id"
    type: "integer"
    description: ""
    foreign-key-id: "unit-type-id"

  - name: "version0"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "billing-rate-card-version-id"
---