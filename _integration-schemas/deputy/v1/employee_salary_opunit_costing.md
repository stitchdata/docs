---
tap: "deputy"
version: "1"
key: "employee-salary-opunit-costing"

name: "employee_salary_opunit_costing"
doc-link: "https://www.deputy.com/api-doc/Resources/EmployeeSalaryOpunitCosting"

description: |
  The `{{ table.name }}` table contains info about employee salary operational unit costs.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The employee salary operational unit costing ID."
    #foreign-key-id: "employee-salary-opunit-costing-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the employee salary operational unit costing was last modified."

  - name: "Employee"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "EmployeeAgreement"
    type: "integer"
    description: ""
    foreign-key-id: "employee-agreement-id"

  - name: "AgreementHistory"
    type: "integer"
    description: ""
    foreign-key-id: "employee-agreement-history-id"

  - name: "DayTimestamp"
    type: "string"
    description: ""

  - name: "Date"
    type: "date"
    description: ""

  - name: "OpUnit"
    type: "integer"
    description: ""
    foreign-key-id: "operational-unit-id"

  - name: "Cost"
    type: "number"
    description: ""

  - name: "Final"
    type: "boolean"
    description: ""

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---