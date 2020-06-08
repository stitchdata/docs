---
tap: "netsuite-suite-analytics"
version: "1"
key: "quota"

name: "quota1"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/quota1.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "amount"
    type: "number"
    description: ""

  - name: "class_0"
    type: "integer"
    description: ""

  - name: "date_0"
    type: "date-time"
    description: ""

  - name: "department"
    type: "integer"
    description: ""

  - name: "entity_id"
    type: "integer"
    description: ""

  - name: "is_alt_sales"
    type: "string"
    description: ""

  - name: "item"
    type: "integer"
    description: ""

  - name: "location_0"
    type: "integer"
    description: ""

  - name: "period"
    type: "integer"
    description: ""

  - name: "quarterly_amount"
    type: "number"
    description: ""

  - name: "quota_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "subsidiary"
    type: "integer"
    description: ""

  - name: "team_quota"
    type: "string"
    description: ""
---