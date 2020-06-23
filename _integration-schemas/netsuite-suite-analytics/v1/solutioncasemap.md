---
tap: "netsuite-suite-analytics"
version: "1"
key: "solution-case-map"

name: "solutioncasemap"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/solutioncasemap.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "date_applied"
    type: "date-time"
    description: ""

  - name: "entity_id"
    type: "integer"
    description: ""

  - name: "solution_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "supportcase_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
---