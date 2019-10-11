---
tap: "deputy"
version: "1.0"
key: "schedule"

name: "schedules"
doc-link: "https://www.deputy.com/api-doc/Resources/Schedule"

description: |
  The `{{ table.name }}` table contains info about schedules.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The schedule ID."
    foreign-key-id: "schedule-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the schedule was last modified."

  - name: "Name"
    type: "string"
    description: ""

  - name: "StartDate"
    type: "date"
    description: ""

  - name: "EndDate"
    type: "date"
    description: ""

  - name: "StartTime"
    type: "string"
    description: ""

  - name: "EndTime"
    type: "string"
    description: ""

  - name: "RepeatType"
    type: "integer"
    description: ""

  - name: "RepeatEvery"
    type: "integer"
    description: ""

  - name: "WeeklyOnDays"
    type: "string"
    description: ""

  - name: "MonthlyOnDates"
    type: "string"
    description: ""

  - name: "MonthlyOnDays"
    type: "string"
    description: ""

  - name: "Exception"
    type: "string"
    description: ""

  - name: "Saved"
    type: "boolean"
    description: ""

  - name: "Orm"
    type: "string"
    description: ""

  - name: "Template"
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