---
tap: "netsuite-suite-analytics"
version: "1"
key: "customer-group-pricing"

name: "customer_group_pricing"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/customer_group_pricing.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "customer_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "price_type_id"
    type: "integer"
    description: ""

  - name: "pricing_group_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
---