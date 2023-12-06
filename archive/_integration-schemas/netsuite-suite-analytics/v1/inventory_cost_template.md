---
tap: "netsuite-suite-analytics"
version: "1"
key: "inventory-cost-template"

name: "inventory_cost_template"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/inventory_cost_template.html"
description: ""

replication-method: "Key-based Incremental"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "create_date"
    type: "date-time"
    description: ""

  - name: "inv_cost_template_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "inv_cost_template_memo"
    type: "string"
    description: ""

  - name: "inv_cost_template_name"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "subsidiary_id"
    type: "integer"
    description: ""
---