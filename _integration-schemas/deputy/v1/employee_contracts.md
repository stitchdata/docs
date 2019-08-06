---
tap: "deputy"
version: "1.0"
key: "employee-contracts"

name: "employee_contracts"
doc-link: ""

description: |
  The `{{ table.name }}` table contains info about employee contracts.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The employee contract ID."
    foreign-key-id: "employee-contract-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the employee contract was last modified."

  - name: "Code"
    type: "string"
    description: ""

  - name: "Name"
    type: "string"
    description: ""

  - name: "Description"
    type: "string"
    description: ""

  - name: "EmploymentBasis"
    type: "integer" 
    description: ""

  - name: "EmploymentCategory"
    type: "integer"
    description: ""
    foreign-key-id: "category-id"

  - name: "EmploymentStatus"
    type: "integer"
    description: ""

  - name: "EmploymentCondition"
    type: "integer"
    description: ""
    foreign-key-id: "employment-condition-id"

  - name: "BasePayRule"
    type: "integer"
    description: ""
    foreign-key-id: "pay-rule-id"

  - name: "StartDate"
    type: "date"
    description: ""

  - name: "EndDate"
    type: "date"
    description: ""

  - name: "PeriodType"
    type: "integer"
    description: ""

  - name: "File"
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