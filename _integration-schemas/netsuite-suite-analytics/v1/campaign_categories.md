---
tap: "netsuite-suite-analytics"
version: "1"
key: "campaign-category"

name: "campaign_categories"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/campaign_categories.html"
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

  - name: "campaigncategory_extid"
    type: "string"
    description: ""

  - name: "campaigncategory_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "campaign-category-id"

  - name: "default_campaign_id"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-id"

  - name: "description"
    type: "string"
    description: ""

  - name: "is_available_externally"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "parent_id"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-category-id"
---