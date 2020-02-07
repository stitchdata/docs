---
tap: "deputy"
version: "1"
key: "employee-contract-leave-rule"

name: "employee_contract_leave_rules"
doc-link: "https://www.deputy.com/api-doc/Resources/EmploymentContractLeaveRules"

description: |
  The `{{ table.name }}` table contains info about employment contract leave rules.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The employment contract leave rule ID."
    #foreign-key-id: "employee-contract-leave-rule-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the employment contract leave rule was last modified."

  - name: "ContractId"
    type: "integer"
    description: ""
    foreign-key-id: "employee-contract-id"

  - name: "LeaveRuleId"
    type: "integer"
    description: ""
    foreign-key-id: "leave-rule-id"

  - name: "LoadingPayRule1"
    type: "integer"
    description: ""
    foreign-key-id: "pay-rule-id"

  - name: "LoadingPayRule2"
    type: "integer"
    description: ""
    foreign-key-id: "pay-rule-id"

  - name: "LoadingPayRule3"
    type: "integer"
    description: ""
    foreign-key-id: "pay-rule-id"

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---