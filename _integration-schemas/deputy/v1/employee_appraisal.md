---
tap: "deputy"
version: "1"
key: "employee-appraisal"

name: "employee_appraisal"
doc-link: "https://www.deputy.com/api-doc/Resources/EmployeeAppraisal"

description: |
  The `{{ table.name }}` table contains info about employee appraisals.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The employee appraisal ID."
    #foreign-key-id: "employee-appraisal-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the employee appraisal was last modified."

  - name: "Employee"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "DayTimestamp"
    type: "integer"
    description: ""

  - name: "Date"
    type: "date"
    description: ""

  - name: "Mark01"
    type: "number"
    description: ""

  - name: "Mark02"
    type: "number"
    description: ""

  - name: "Mark03"
    type: "number"
    description: ""

  - name: "Mark04"
    type: "number"
    description: ""

  - name: "Mark05"
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