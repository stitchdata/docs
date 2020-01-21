---
tap: "deputy"
version: "1"
key: "employee-paycycle-return"

name: "employee_paycycle_returns"
doc-link: "https://www.deputy.com/api-doc/Resources/EmployeePaycycleReturn"

description: |
  The `{{ table.name }}` table contains info about employee paycycle returns.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The employee paycycle return ID."
    #foreign-key-id: "employee-paycycle-return-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the employee paycycle return was last modified."

  - name: "PaycycleId"
    type: "integer"
    description: ""
    foreign-key-id: "employee-paycycle-id"

  - name: "PayRule"
    type: "integer"
    description: ""
    foreign-key-id: "pay-rule-id"

  - name: "Approved"
    type: "boolean"
    description: ""

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