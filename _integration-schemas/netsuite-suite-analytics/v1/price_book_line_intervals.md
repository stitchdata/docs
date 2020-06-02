---
tap: "netsuite-suite-analytics"
version: "1"
key: "price-book-line-interval"

name: "price_book_line_intervals"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/price_book_line_intervals.html"
description: |
  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "charge_frequency_id"
    type: "string"
    description: ""

  - name: "discount"
    type: "integer"
    description: ""

  - name: "is_discount_percentage"
    type: "string"
    description: ""

  - name: "is_overage_discount_percentage"
    type: "string"
    description: ""

  - name: "overage_charge_frequency_id"
    type: "string"
    description: ""

  - name: "overage_discount"
    type: "integer"
    description: ""

  - name: "overage_price_plan_id"
    type: "integer"
    description: ""
    foreign-key-id: "price-plan-id"

  - name: "overage_repeat_every"
    type: "integer"
    description: ""

  - name: "pbli_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "plan_line_id"
    type: "integer"
    description: ""
    foreign-key-id: "subscription-plan-line-id"

  - name: "plan_line_number"
    type: "integer"
    description: ""

  - name: "price_book_id"
    type: "integer"
    description: ""
    foreign-key-id: "price-book-id"

  - name: "price_plan_id"
    type: "integer"
    description: ""
    foreign-key-id: "price-plan-id"

  - name: "prorate_by"
    type: "string"
    description: ""

  - name: "repeat_every"
    type: "integer"
    description: ""

  - name: "start_offset"
    type: "string"
    description: ""

  - name: "usage_multiplier_line_id"
    type: "integer"
    description: ""
    foreign-key-id: "subscription-plan-line-id"
---