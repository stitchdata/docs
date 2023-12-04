---
tap: "netsuite-suite-analytics"
version: "1"
key: "revenue-plan-version"

name: "revenue_plan_versions"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/revenue_plan_versions.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "created_by_id"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "plan_id"
    type: "integer"
    description: ""
    foreign-key-id: "revenue-plan-id"

  - name: "plan_version"
    type: "integer"
    description: ""

  - name: "plan_version_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "revenue-plan-version-id"
---