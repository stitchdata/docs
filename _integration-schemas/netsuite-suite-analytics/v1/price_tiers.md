---
tap: "netsuite-suite-analytics"
version: "1"
key: "price-tier"

name: "price_tiers"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/price_tiers.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "from_quantity"
    type: "integer"
    description: ""

  - name: "maximum_quantity"
    type: "number"
    description: ""

  - name: "minimum_quantity"
    type: "number"
    description: ""

  - name: "price_plan_id"
    type: "integer"
    description: ""
    foreign-key-id: "price-plan-id"

  - name: "price_tier"
    type: "string"
    description: ""

  - name: "price_tier_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "price_value"
    type: "integer"
    description: ""

  - name: "pricing_option"
    type: "string"
    description: ""
---