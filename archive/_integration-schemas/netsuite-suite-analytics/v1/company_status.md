---
tap: "netsuite-suite-analytics"
version: "1"
key: "company-status"

name: "company_status"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/company_status.html"
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

  - name: "company_status_extid"
    type: "string"
    description: ""

  - name: "company_status_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "company-status-id"

  - name: "description"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "probability"
    type: "number"
    description: ""

  - name: "readonly"
    type: "string"
    description: ""
---