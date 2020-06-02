---
tap: "netsuite-suite-analytics"
version: "1"
key: "job-type"

name: "job_types"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/jobtype.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "job_type_extid"
    type: "string"
    description: ""

  - name: "job_type_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "parent_id"
    type: "integer"
    description: ""
---