---
tap: "deputy"
version: "1"
key: "employee-history"

name: "employee_history"
doc-link: "https://www.deputy.com/api-doc/Resources/EmployeeHistory"

description: |
  The `{{ table.name }}` table contains info about employee histories.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The employee history ID."
    foreign-key-id: "employee-history-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the employee history was last modified."

  - name: "Company"
    type: "integer"
    description: ""
    foreign-key-id: "company-id"

  - name: "FirstName"
    type: "string"
    description: ""

  - name: "LastName"
    type: "string"
    description: ""

  - name: "DisplayName"
    type: "string"
    description: ""

  - name: "OtherName"
    type: "string"
    description: ""

  - name: "Salutation"
    type: "string"
    description: ""

  - name: "MainAddress"
    type: "string"
    description: ""
    foreign-key-id: "address-id"

  - name: "PostalAddress"
    type: "string"
    description: ""
    foreign-key-id: "address-id"

  - name: "EmergencyAddress"
    type: "string"
    description: ""
    foreign-key-id: "address-id"

  - name: "DateOfBirth"
    type: "date"
    description: ""

  - name: "Gender"
    type: "integer"
    description: ""

  - name: "Photo"
    type: "integer"
    description: ""

  - name: "JobAppId"
    type: "integer"
    description: ""

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "StartDate"
    type: "date"
    description: ""

  - name: "TerminationDate"
    type: "date"
    description: ""

  - name: "Position"
    type: "string"
    description: ""

  - name: "Role"
    type: "integer"
    description: ""
    foreign-key-id: "employee-role-id"

  - name: "EmployeeId"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---