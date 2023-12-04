---
tap: "netsuite-suite-analytics"
version: "1"
key: "item-group"

name: "item_group"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/itemgroup.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "bom_quantity"
    type: "number"
    description: ""

  - name: "component_yield"
    type: "integer"
    description: ""

  - name: "effective_date"
    type: "date-time"
    description: ""

  - name: "effective_revision"
    type: "integer"
    description: ""

  - name: "item_group_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "item_source"
    type: "string"
    description: ""

  - name: "line_id"
    type: "integer"
    description: ""

  - name: "member_id"
    type: "integer"
    description: ""

  - name: "obsolete_date"
    type: "date-time"
    description: ""

  - name: "obsolete_revision"
    type: "integer"
    description: ""

  - name: "parent_id"
    type: "integer"
    description: ""

  - name: "quantity"
    type: "number"
    description: ""

  - name: "rate_plan_id"
    type: "integer"
    description: ""

  - name: "unit_of_measure_id"
    type: "integer"
    description: ""
    foreign-key-id: "uom-id"
---