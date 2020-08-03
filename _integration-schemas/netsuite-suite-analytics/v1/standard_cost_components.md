---
tap: "netsuite-suite-analytics"
version: "1"
key: "standard-cost-component"

name: "standard_cost_components"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/standard_cost_components.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "component_id"
    type: "integer"
    description: ""
    foreign-key-id: "item-id"

  - name: "cost_category"
    type: "string"
    description: ""

  - name: "line_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "planned_standard_cost_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "planned-standard-cost-id"

  - name: "quantity"
    type: "integer"
    description: ""

  - name: "standard_cost"
    type: "integer"
    description: ""
---