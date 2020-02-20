---
tap: "deputy"
version: "1"
key: "employee-workplace"

name: "employee_workplaces"
doc-link: "https://www.deputy.com/api-doc/Resources/EmployeeWorkplace"

description: |
  The `{{ table.name }}` table contains info about employee workplaces.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The employee workplace ID."
    #foreign-key-id: "employee-workplace-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the employee workplace was last modified."

  - name: "EmployeeId"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Company"
    type: "integer"
    description: ""
    foreign-key-id: "company-id"

  - name: "SortOrder"
    type: "integer"
    description: ""

  - name: "Agreement1"
    type: "integer"
    description: ""
    foreign-key-id: "employee-agreement-id"

  - name: "Agreement2"
    type: "integer"
    description: ""
    foreign-key-id: "employee-agreement-id"

  - name: "Agreement3"
    type: "integer"
    description: ""
    foreign-key-id: "employee-agreement-id"

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---