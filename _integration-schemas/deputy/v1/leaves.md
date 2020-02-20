---
tap: "deputy"
version: "1"
key: "leave"

name: "leaves"
doc-link: "https://www.deputy.com/api-doc/Resources/Leave"

description: |
  The `{{ table.name }}` table contains info about employee leave.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The leave ID."
    foreign-key-id: "leave-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the leave was last modified."

  - name: "Employee"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "EmployeeHistory"
    type: "integer"
    description: ""
    foreign-key-id: "employee-history-id"

  - name: "Company"
    type: "integer"
    description: ""
    foreign-key-id: "company-id"

  - name: "Start"
    type: "integer"
    description: ""

  - name: "End"
    type: "integer"
    description: ""

  - name: "DateEnd"
    type: "date"
    description: ""

  - name: "Days"
    type: "number"
    description: ""

  - name: "ApproverTime"
    type: "integer"
    description: ""

  - name: "ApproverPay"
    type: "integer"
    description: ""

  - name: "Comment"
    type: "string"
    description: ""

  - name: "Status"
    type: "integer"
    description: ""

  - name: "ApprovalComment"
    type: "string"
    description: ""

  - name: "TotalHours"
    type: "number"
    description: ""

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---