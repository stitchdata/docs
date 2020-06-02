---
tap: "netsuite-suite-analytics"
version: "1"
key: "last-sales-activity-record"

name: "last_sales_activity_record"
doc-link: ""
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "entityopp_id"
    type: "string"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "last_modified_date"
    type: "date-time"
    description: ""

  - name: "last_sales_activity"
    type: "date-time"
    description: ""

  - name: "last_sales_activity_record_ext"
    type: "string"
    description: ""

  - name: "last_sales_activity_record_id"
    type: "integer"
    description: ""

  - name: "lsa_link"
    type: "string"
    description: ""

  - name: "lsa_link_name"
    type: "string"
    description: ""

  - name: "mode_0"
    type: "string"
    description: ""

  - name: "parent_id"
    type: "integer"
    description: ""
---