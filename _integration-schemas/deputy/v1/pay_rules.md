---
tap: "deputy"
version: "1"
key: "pay-rule"

name: "pay_rules"
doc-link: "https://www.deputy.com/api-doc/Resources/PayRules"

description: |
  The `{{ table.name }}` table contains info about pay rules.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The pay rule ID."
    foreign-key-id: "pay-rule-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the pay rule was last modified."

  - name: "PayTitle"
    type: "string"
    description: ""

  - name: "RenumerationType"
    type: "integer"
    description: ""

  - name: "RenumerationBy"
    type: "integer"
    description: ""

  - name: "AnnualSalary"
    type: "number"
    description: ""

  - name: "HourlyRate"
    type: "number"
    description: ""

  - name: "IsMultiplier"
    type: "boolean"
    description: ""

  - name: "MultiplierValue"
    type: "number"
    description: ""

  - name: "MultiplierBaseRate"
    type: "integer"
    description: ""

  - name: "MinimumType"
    type: "integer"
    description: ""

  - name: "MaximumType"
    type: "integer"
    description: ""

  - name: "MinimumValue"
    type: "integer"
    description: ""

  - name: "MaximumValue"
    type: "integer"
    description: ""

  - name: "MinimumShiftLength"
    type: "string"
    description: ""

  - name: "MaximumShiftLength"
    type: "string"
    description: ""

  - name: "AdvancedCalculation"
    type: "string"
    description: ""

  - name: "IsExported"
    type: "boolean"
    description: ""

  - name: "UnitValue"
    type: "number"
    description: ""

  - name: "Schedule"
    type: "integer"
    description: ""
    foreign-key-id: "schedule-id"

  - name: "RecommendWith"
    type: "integer"
    description: ""

  - name: "DexmlScript"
    type: "integer"
    description: ""

  - name: "DexmlScriptParam"
    type: "string"
    description: ""

  - name: "PeriodType"
    type: "integer"
    description: ""

  - name: "PayPortionRule"
    type: "integer"
    description: ""

  - name: "PayrollCategory"
    type: "string"
    description: ""

  - name: "Comment"
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