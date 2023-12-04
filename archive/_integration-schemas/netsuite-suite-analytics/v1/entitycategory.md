---
tap: "netsuite-suite-analytics"
version: "1"
key: "entity-category"

name: "entitycategory"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/entitycategory.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "entity_category_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "entity_type"
    type: "string"
    netsuite-primary-key: true
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "parent_0"
    type: "integer"
    description: ""
---