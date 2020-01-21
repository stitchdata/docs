---
tap: "deputy"
version: "1"
key: "timesheet-pay-return"

name: "timesheet_pay_returns"
doc-link: "https://www.deputy.com/api-doc/Resources/TimesheetPayReturn"

description: |
  The `{{ table.name }}` table contains info about timesheet pay returns.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The timesheet pay return ID."
    #foreign-key-id: "timesheet-pay-return-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the timesheet pay return was last modified."

  - name: "Timesheet"
    type: "integer"
    description: ""
    foreign-key-id: "timesheet-id"

  - name: "PayRule"
    type: "integer"
    description: ""
    foreign-key-id: "pay-rule-id"

  - name: "Overridden"
    type: "boolean"
    description: ""

  - name: "Value"
    type: "number"
    description: ""

  - name: "Cost"
    type: "number"
    description: ""

  - name: "OverrideComment"
    type: "string"
    description: ""

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---