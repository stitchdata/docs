---
tap: "netsuite-suite-analytics"
version: "1"
key: "inventory-cost-template-items"

name: "inventory_cost_template_items"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/inventory_cost_template_items.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "inv_cost_template_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "inv_cost_template_line_order"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""
---