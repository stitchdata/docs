---
tap: "netsuite-suite-analytics"
version: "1"
key: "bom-revision-component"

name: "bom_revision_components"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/bom_revision_components.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "bom_revision_component_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    # foreign-key-id: "bom-revision-component-id"

  - name: "bom_revision_id"
    type: "integer"
    description: ""
    foreign-key-id: "bom-revision-id"

  - name: "component_yield"
    type: "integer"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""
    foreign-key-id: "item-id"

  - name: "item_source"
    type: "string"
    description: ""

  - name: "quantity"
    type: "number"
    description: ""

  - name: "seq_num"
    type: "integer"
    description: ""

  - name: "unit_of_measure_id"
    type: "integer"
    description: ""
    foreign-key-id: "uom-id"
---