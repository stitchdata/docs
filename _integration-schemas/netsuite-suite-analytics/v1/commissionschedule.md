---
tap: "netsuite-suite-analytics"
version: "1"
key: "commission-schedule"

name: "commissionschedule"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/commissionschedule.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "author"
    type: "integer"
    description: ""

  - name: "category_0"
    type: "string"
    description: ""

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "manager_"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "period_type"
    type: "string"
    description: ""

  - name: "schedule_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "target_amount"
    type: "integer"
    description: ""

  - name: "type_id"
    type: "string"
    description: ""
---