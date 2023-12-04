---
tap: "netsuite-suite-analytics"
version: "1"
key: "unlocked-time-period"

name: "unlocked_time_periods"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/unlockedtimeperiod.html"
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

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "date_period_end"
    type: "date-time"
    description: ""

  - name: "date_period_start"
    type: "date-time"
    description: ""

  - name: "date_valid_until"
    type: "date-time"
    description: ""

  - name: "employee_id"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "last_modified_by_id"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "unlocked_time_period_extid"
    type: "string"
    description: ""

  - name: "unlocked_time_period_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
---