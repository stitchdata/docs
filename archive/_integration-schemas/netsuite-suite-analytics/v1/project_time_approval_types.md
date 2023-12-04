---
tap: "netsuite-suite-analytics"
version: "1"
key: "project-time-approval-type"

name: "project_time_approval_types"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/project_time_approval_types.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "description"
    type: "string"
    description: ""

  - name: "project_time_approval_type_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "project-time-approval-type-id"
---