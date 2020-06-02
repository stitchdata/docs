---
tap: "netsuite-suite-analytics"
version: "1"
key: "group-test-cell"

name: "group_test_cell"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/group_test_cell.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "crm_group_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "cumulativepct"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "percentage"
    type: "integer"
    description: ""

  - name: "previouspct"
    type: "integer"
    description: ""

  - name: "test_cell_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "test-cell-id"
---