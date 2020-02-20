---
tap: "deputy"
version: "1"
key: "employee-paycycle"

name: "employee_paycycles"
doc-link: "https://www.deputy.com/api-doc/Resources/EmployeePaycycle"

description: |
  The `{{ table.name }}` table contains info about employee paycycles.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The employee paycycle ID."
    foreign-key-id: "employee-paycycle-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the employee paycycle was last modified."

  - name: "EmployeeId"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "EmployeeAgreementId"
    type: "integer"
    description: ""
    foreign-key-id: "employee-agreement-id"

  - name: "PeriodId"
    type: "integer"
    description: ""
    foreign-key-id: "company-period-id"

  - name: "RecommendedLoadings"
    type: "boolean"
    description: ""

  - name: "Timesheets"
    type: "integer"
    description: ""

  - name: "TimesheetsTimeApproved"
    type: "integer"
    description: ""

  - name: "TimesheetsPayApproved"
    type: "string"
    description: ""

  - name: "PaycycleRules"
    type: "integer"
    description: ""

  - name: "PaycycleRulesApproved"
    type: "integer"
    description: ""

  - name: "Exported"
    type: "boolean"
    description: ""

  - name: "ExportId"
    type: "integer"
    description: ""

  - name: "Paid"
    type: "boolean"
    description: ""

  - name: "TimeTotal"
    type: "number"
    description: ""

  - name: "CostTotal"
    type: "number"
    description: ""

  - name: "EmployeeAgreementHistoryId"
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