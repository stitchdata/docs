---
tap: "deputy"
version: "1.0"
key: "employee-availability"

name: "employee_availability"
doc-link: "https://www.deputy.com/api-doc/Resources/EmployeeAvailability"

description: |
  The `{{ table.name }}` table contains info about employee availability.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The employee availability ID."
    #foreign-key-id: "employee-availability-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the employee availability was last modified."

  - name: "Employee"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Type"
    type: "integer"
    description: ""

  - name: "MaxDateRecurringGenerated"
    type: "date"
    description: ""

  - name: "StartTime"
    type: "integer"
    description: ""

  - name: "EndTime"
    type: "integer"
    description: ""

  - name: "Date"
    type: "date"
    description: ""

  - name: "Comment"
    type: "integer"
    description: ""

  - name: "Schedule"
    type: "integer"
    description: ""
    foreign-key-id: "schedule-id"

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---