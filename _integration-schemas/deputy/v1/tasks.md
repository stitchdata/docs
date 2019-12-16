---
tap: "deputy"
version: "1.0"
key: "task"

name: "tasks"
doc-link: "https://www.deputy.com/api-doc/Resources/Task"

description: |
  The `{{ table.name }}` table contains info about tasks.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The task ID."
    #foreign-key-id: "task-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the task was last modified."

  - name: "TaskSetupId"
    type: "integer"
    description: ""
    foreign-key-id: "task-setup-id"

  - name: "OpUnitId"
    type: "integer"
    description: ""
    foreign-key-id: "operational-unit-id"

  - name: "GroupId"
    type: "integer"
    description: ""
    foreign-key-id: "task-group-id"

  - name: "DayTimestamp"
    type: "integer"
    description: ""

  - name: "Date"
    type: "date"
    description: ""

  - name: "OrigDayTimestamp"
    type: "integer"
    description: ""

  - name: "OrigDate"
    type: "date"
    description: ""

  - name: "AvailableAfterTimestamp"
    type: "integer"
    description: ""

  - name: "DueDate"
    type: "date"
    description: ""

  - name: "DueTimestamp"
    type: "integer"
    description: ""

  - name: "RepeatIfNotCompleted"
    type: "boolean"
    description: ""

  - name: "SortOrder"
    type: "integer"
    description: ""

  - name: "Type"
    type: "integer"
    description: ""

  - name: "Question"
    type: "string"
    description: ""

  - name: "Answer"
    type: "string"
    description: ""

  - name: "Comment"
    type: "string"
    description: ""

  - name: "UserEntry"
    type: "integer"
    description: ""

  - name: "UserPerformTask"
    type: "integer"
    description: ""

  - name: "UserResponsible"
    type: "integer"
    description: ""

  - name: "TsCompleted"
    type: "integer"
    description: ""

  - name: "Start"
    type: "integer"
    description: ""

  - name: "End"
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