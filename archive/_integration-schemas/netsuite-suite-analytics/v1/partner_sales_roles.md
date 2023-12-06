---
tap: "netsuite-suite-analytics"
version: "1"
key: "partner-sale-role"

name: "partner_sales_roles"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/partner_sales_roles.html"
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

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "parent_id"
    type: "integer"
    description: ""

  - name: "partner_sales_role_extid"
    type: "string"
    description: ""

  - name: "partner_sales_role_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
---