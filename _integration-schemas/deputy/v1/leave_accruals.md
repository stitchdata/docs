---
tap: "deputy"
version: "1"
key: "leave-accrual"

name: "leave_accruals"
doc-link: "https://www.deputy.com/api-doc/Resources/LeaveAccrual"

description: |
  The `{{ table.name }}` table contains info about employee leave balances.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The leave accrual ID."
    foreign-key-id: "leave-accrual-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the leave accrual was last modified."

  - name: "Employee"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "EmployeeHistory"
    type: "integer"
    description: ""
    foreign-key-id: "employee-history-id"

  - name: "TransactionDate"
    type: "date"
    description: ""

  - name: "Type"
    type: "integer"
    description: ""

  - name: "LeaveRule"
    type: "integer"
    description: ""
    foreign-key-id: "leave-rule-id"

  - name: "Hours"
    type: "number"
    description: ""

  - name: "Days"
    type: "number"
    description: ""

  - name: "Comment"
    type: "string"
    description: ""

  - name: "FkId"
    type: "integer"
    description: ""

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---