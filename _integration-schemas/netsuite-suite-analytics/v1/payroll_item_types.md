---
tap: "netsuite-suite-analytics"
version: "1"
key: "payroll-item-type"

name: "payroll_item_types"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/payroll_item_types.html"
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
  - name: "parent_id"
    type: "integer"
    description: ""
  - name: "payroll_item_type_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
---