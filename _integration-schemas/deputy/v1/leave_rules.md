---
tap: "deputy"
version: "1"
key: "leave-rule"

name: "leave_rules"
doc-link: "https://www.deputy.com/api-doc/Resources/LeaveRules"

description: |
  The `{{ table.name }}` table contains info about employee leave rules.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The leave rule ID."
    foreign-key-id: "leave-rule-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the leave rule was last modified."

  - name: "Name"
    type: "string"
    description: ""

  - name: "Type"
    type: "string"
    description: ""

  - name: "Description"
    type: "string"
    description: ""

  - name: "MaxAllowedAnnually"
    type: "number"
    description: ""

  - name: "PaidLeave"
    type: "boolean"
    description: ""

  - name: "AnnualRollOver"
    type: "boolean"
    description: ""

  - name: "Visible"
    type: "boolean"
    description: ""

  - name: "UnitType"
    type: "integer"
    description: ""

  - name: "ExportType"
    type: "integer"
    description: ""

  - name: "ResetType"
    type: "integer"
    description: ""

  - name: "PayrollCategory"
    type: "string"
    description: ""

  - name: "CalcType"
    type: "integer"
    description: ""

  - name: "PayoutOnTermination"
    type: "boolean"
    description: ""

  - name: "EntitlementAfterMonth"
    type: "integer"
    description: ""

  - name: "Calc"
    type: "string"
    description: ""

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---