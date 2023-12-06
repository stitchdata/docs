---
tap: "netsuite-suite-analytics"
version: "1"
key: "distribution-category"

name: "distribution_categories"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/distribution_categories.html"
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

  - name: "category_name"
    type: "string"
    description: ""

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "distribution_category_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""
---