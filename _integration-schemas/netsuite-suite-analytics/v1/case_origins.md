---
tap: "netsuite-suite-analytics"
version: "1"
key: "case-origin"

name: "case_origins"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/case_origins.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "case_origin_extid"
    type: "string"
    description: ""

  - name: "case_origin_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "case-origin-id"

  - name: "date_last_modified_"
    type: "date-time"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""
---