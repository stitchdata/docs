---
tap: "netsuite-suite-analytics"
version: "1"
key: "promotion-code"

name: "promotion_codes"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/promotioncode.html"
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

  - name: "apply_discount"
    type: "string"
    description: ""

  - name: "code"
    type: "string"
    description: ""

  - name: "code_pattern"
    type: "string"
    description: ""
  
  - name: "descr"
    type: "string"
    description: ""

  - name: "discount"
    type: "string"
    description: ""

  - name: "discount_id"
    type: "integer"
    description: ""

  - name: "display_line_discounts"
    type: "string"
    description: ""

  - name: "end_date"
    type: "date-time"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "plugin_implementation_id"
    type: "string"
    description: ""

  - name: "promotion_code_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "promotion-code-id"

  - name: "use_type"
    type: "string"
    description: ""
---