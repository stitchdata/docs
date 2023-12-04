---
tap: "netsuite-suite-analytics"
version: "1"
key: "item-site-category"

name: "item_site_categories"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/item_site_categories.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "category_id"
    type: "integer"
    description: ""

  - name: "category_sequence"
    type: "integer"
    description: ""

  - name: "category_type"
    type: "string"
    description: ""

  - name: "default_name"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "full_name"
    type: "string"
    description: ""

  - name: "ishidden"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "ispreferred"
    type: "string"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""

  - name: "long_description"
    type: "string"
    description: ""

  - name: "parent_category_id"
    type: "integer"
    description: ""

  - name: "section_created_by"
    type: "integer"
    description: ""

  - name: "section_created_date"
    type: "date-time"
    description: ""

  - name: "section_modified_by"
    type: "integer"
    description: ""

  - name: "section_modified_date"
    type: "date-time"
    description: ""
---