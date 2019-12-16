---
tap: "deputy"
version: "1.0"
key: "employee-agreement-history"

name: "employee_agreement_history"
doc-link: "https://www.deputy.com/api-doc/Resources/EmployeeAgreementHistory"

description: |
  The `{{ table.name }}` table contains info about 

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The employee agreement history ID."
    foreign-key-id: "employee-agreement-history-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the employee agreement history was last modified."

  - name: "AgreementId"
    type: "integer"
    description: ""
    foreign-key-id: "employee-agreement-id"

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

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---