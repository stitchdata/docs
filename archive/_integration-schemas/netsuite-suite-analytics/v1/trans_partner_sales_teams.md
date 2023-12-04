---
tap: "netsuite-suite-analytics"
version: "1"
key: "trans-partner-sales-team"

name: "trans_partner_sales_teams"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/trans_partner_sales_teams.html"
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

  - name: "contribution"
    type: "integer"
    description: ""

  - name: "isprimary"
    type: "string"
    description: ""

  - name: "partner_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "partner_sales_role_id"
    type: "integer"
    description: ""

  - name: "transaction_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
---