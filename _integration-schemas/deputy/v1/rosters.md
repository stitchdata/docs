---
tap: "deputy"
version: "1.0"
key: "roster"

name: "rosters"
doc-link: "https://www.deputy.com/api-doc/Resources/Roster"

description: |
  The `{{ table.name }}` table contains info about rosters.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The roster ID."
    foreign-key-id: "roster-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the roster was last modified."

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
    type: "string"
    description: ""

  - name: "TotalTime"
    type: "number"
    description: ""

  - name: "Cost"
    type: "number"
    description: ""

  - name: "OperationalUnit"
    type: "integer"
    description: ""
    foreign-key-id: "operational-unit-id"

  - name: "Employee"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Comment"
    type: "string"
    description: ""

  - name: "Warning"
    type: "string"
    description: ""

  - name: "WarningOverrideComment"
    type: "string"
    description: ""

  - name: "Published"
    type: "boolean"
    description: ""

  - name: "MatchedByTimesheet"
    type: "integer"
    description: ""
    foreign-key-id: "timesheet-id"

  - name: "Open"
    type: "boolean"
    description: ""

  - name: "ConfirmStatus"
    type: "integer"
    description: ""

  - name: "ConfirmComment"
    type: "string"
    description: ""

  - name: "ConfirmBy"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "ConfirmTime"
    type: "integer"
    description: ""

  - name: "SwapStatus"
    type: "integer"
    description: ""

  - name: "SwapManageBy"
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