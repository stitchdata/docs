---
tap: "netsuite-suite-analytics"
version: "1"
key: "timesheet"

name: "timesheet"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/timesheet.html"
description: |
  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "employee_id"
    type: "integer"
    description: ""

  - name: "end_date"
    type: "date-time"
    description: ""

  - name: "start_date"
    type: "date-time"
    description: ""

  - name: "status_code"
    type: "string"
    description: ""

  - name: "timesheet_id"
    type: "integer"
    description: ""
---