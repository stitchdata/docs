---
tap: "netsuite-suite-analytics"
version: "1"
key: "crm-group"

name: "crmgroup"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/crmgroup.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "group_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "crm-group-id"

  - name: "group_type"
    type: "string"
    description: ""

  - name: "is_mfg_work_center"
    type: "string"
    description: ""

  - name: "is_private"
    type: "string"
    description: ""

  - name: "is_sales_group"
    type: "string"
    description: ""

  - name: "is_support_group"
    type: "string"
    description: ""

  - name: "labor_resources"
    type: "integer"
    description: ""

  - name: "machine_resources"
    type: "integer"
    description: ""

  - name: "owner"
    type: "integer"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "work_calendar_id"
    type: "integer"
    description: ""
---