---
tap: "netsuite-suite-analytics"
version: "1"
key: "sales-role"

name: "sales_roles"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/salesrole.html"
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

  - name: "description"
    type: "string"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "is_sales_rep_role"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "sales_role_extid"
    type: "string"
    description: ""

  - name: "sales_role_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
---