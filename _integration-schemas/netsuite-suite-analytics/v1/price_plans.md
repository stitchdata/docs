---
tap: "netsuite-suite-analytics"
version: "1"
key: "price-plan"

name: "price_plans"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/priceplan.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "currency"
    type: "string"
    description: ""

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "included_quantity"
    type: "number"
    description: ""

  - name: "price_plan_extid"
    type: "string"
    description: ""

  - name: "price_plan_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "price-plan-id"

  - name: "price_plan_type"
    type: "string"
    description: ""
---