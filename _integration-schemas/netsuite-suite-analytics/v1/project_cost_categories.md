---
tap: "netsuite-suite-analytics"
version: "1"
key: "project-cost-category"

name: "project_cost_categories"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/project_cost_categories.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "category_name"
    type: "string"
    description: ""

  - name: "category_type"
    type: "string"
    description: ""

  - name: "expense_category_id"
    type: "integer"
    description: ""

  - name: "full_name"
    type: "string"
    description: ""

  - name: "is_other_category"
    type: "string"
    description: ""

  - name: "is_selected"
    type: "string"
    description: ""

  - name: "project_cost_category_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "service_item_id"
    type: "integer"
    description: ""

  - name: "supplier_category_id"
    type: "string"
    description: ""

  - name: "use_subcategories"
    type: "string"
    description: ""
---