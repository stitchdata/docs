---
tap: "netsuite-suite-analytics"
version: "1"
key: "job-resource"

name: "job_resources"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/job_resources.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "job_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "resource_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "resource_role_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
---