---
tap: "netsuite-suite-analytics"
version: "1"
key: "pricing-group"

name: "pricing_groups"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/pricinggroup.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "name"
    type: "string"
    description: ""

  - name: "pricing_group_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
---