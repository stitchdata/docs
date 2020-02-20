---
tap: "deputy"
version: "1"
key: "timesheet"

name: "timesheets"
doc-link: "https://www.deputy.com/api-doc/Resources/Timesheet"

description: |
  The `{{ table.name }}` table contains info about timesheets.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The timesheet ID."
    foreign-key-id: "timesheet-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the timesheet was last modified."

  - name: "Employee"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "EmployeeHistory"
    type: "integer"
    description: ""
    foreign-key-id: "employee-history-id"

  - name: "EmployeeAgreement"
    type: "integer"
    description: ""
    foreign-key-id: "employee-agreement-id"

  - name: "Date"
    type: "date"
    description: ""

  - name: "StartTime"
    type: "integer"
    description: ""

  - name: "EndTime"
    type: "integer"
    description: ""

  - name: "Mealbreak"
    type: "time"
    description: ""

  - name: "MealbreakSlots"
    type: "string"
    description: ""

  - name: "TotalTime"
    type: "number"
    description: ""

  - name: "TotalTimeInv"
    type: "number"
    description: ""

  - name: "Cost"
    type: "number"
    description: ""

  - name: "Roster"
    type: "integer"
    description: ""
    foreign-key-id: "roster-id"

  - name: "EmployeeComment"
    type: "string"
    description: ""

  - name: "SupervisorComment"
    type: "string"
    description: ""

  - name: "Supervisor"
    type: "integer"
    description: ""

  - name: "Disputed"
    type: "boolean"
    description: ""

  - name: "ValidationFlag"
    type: "integer"
    description: ""

  - name: "OperationalUnit"
    type: "integer"
    description: ""
    foreign-key-id: "operational-unit-id"

  - name: "IsInProgress"
    type: "boolean"
    description: ""

  - name: "IsLeave"
    type: "boolean"
    description: ""

  - name: "LeaveId"
    type: "integer"
    description: ""
    foreign-key-id: "leave-id"

  - name: "LeaveRule"
    type: "integer"
    description: ""
    foreign-key-id: "leave-rule-id"

  - name: "Invoiced"
    type: "boolean"
    description: ""

  - name: "InvoiceComment"
    type: "string"
    description: ""

  - name: "PayRuleApproved"
    type: "boolean"
    description: ""

  - name: "Exported"
    type: "boolean"
    description: ""

  - name: "StagingId"
    type: "integer"
    description: ""

  - name: "PayStaged"
    type: "boolean"
    description: ""

  - name: "PaycycleId"
    type: "integer"
    description: ""
    foreign-key-id: "employee-paycycle-id"

  - name: "File"
    type: "integer"
    description: ""

  - name: "CustomFieldData"
    type: "integer"
    description: ""
    foreign-key-id: "custom-field-data-id"

  - name: "RealTime"
    type: "boolean"
    description: ""

  - name: "AutoProcessed"
    type: "boolean"
    description: ""

  - name: "AutoRounded"
    type: "boolean"
    description: ""

  - name: "AutoTimeApproved"
    type: "boolean"
    description: ""

  - name: "AutoPayRuleApproved"
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