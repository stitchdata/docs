---
tap: "netsuite-suite-analytics"
version: "1"
key: "plan-schedule-map"

name: "planschedulemap"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/planschedulemap.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "plan_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "schedule_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
---