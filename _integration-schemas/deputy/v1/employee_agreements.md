---
tap: "deputy"
version: "1.0"
key: "employee-agreement"

name: "employee_agreements"
doc-link: "https://www.deputy.com/api-doc/Resources/EmployeeAgreement"

description: |
  The `{{ table.name }}` table contains info about employee agreements.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The employee agreement ID."
    foreign-key-id: "employee-agreement-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the employee agreement was last modified."

  - name: "EmployeeId"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "PayPoint"
    type: "integer"
    description: ""

  - name: "EmpType"
    type: "integer"
    description: ""

  - name: "CompanyName"
    type: "string"
    description: ""

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "StartDate"
    type: "date"
    description: ""

  - name: "Contract"
    type: "integer"
    description: ""
    foreign-key-id: "employee-contract-id"

  - name: "SalaryPayRule"
    type: "integer"
    description: ""
    foreign-key-id: "pay-rule-id"

  - name: "ContractFile"
    type: "integer"
    description: ""

  - name: "PayrollId"
    type: "integer"
    description: ""

  - name: "PayPeriod"
    type: "integer"
    description: ""
    foreign-key-id: "pay-period-id"

  - name: "HistoryId"
    type: "integer"
    description: ""
    foreign-key-id: "employee-agreement-history-id"

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---