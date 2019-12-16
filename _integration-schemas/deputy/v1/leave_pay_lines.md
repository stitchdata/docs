---
tap: "deputy"
version: "1.0"
key: "leave-pay-line"

name: "leave_pay_lines"
doc-link: "https://www.deputy.com/api-doc/Resources/LeavePayLine"

description: |
  The `{{ table.name }}` table contains info about employee leave pay lines.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The leave pay line ID."
    #foreign-key-id: "leave-pay-line-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the leave pay line was last modified."

  - name: "LeaveId"
    type: "integer"
    description: ""
    foreign-key-id: "leave-id"

  - name: "LeaveRule"
    type: "integer"
    description: ""
    foreign-key-id: "leave-rule-id"

  - name: "EmployeeAgreement"
    type: "integer"
    description: ""
    foreign-key-id: "employee-agreement-id"

  - name: "Date"
    type: "date"
    description: ""

  - name: "StartTime"
    type: "string"
    description: ""

  - name: "EndTime"
    type: "string"
    description: ""

  - name: "Hours"
    type: "string"
    description: ""

  - name: "Comment"
    type: "string"
    description: ""

  - name: "TimesheetId"
    type: "integer"
    description: ""
    foreign-key-id: "timesheet-id"

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---