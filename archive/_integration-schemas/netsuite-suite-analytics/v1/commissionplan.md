---
tap: "netsuite-suite-analytics"
version: "1"
key: "commission-plan"

name: "commissionplan"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/commissionplan.html"
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

  - name: "commission_plan"
    type: "string"
    description: ""

  - name: "commission_plan_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "date_modified"
    type: "date-time"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""
---