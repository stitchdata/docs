---
tap: "deputy"
version: "1"
key: "task-group"

name: "task_groups"
doc-link: "https://www.deputy.com/api-doc/Resources/TaskGroup"

description: |
  The `{{ table.name }}` table contains info about task groups.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The task group ID."
    foreign-key-id: "task-group-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the task group was last modified."

  - name: "GroupSetupId"
    type: "integer"
    description: ""
    foreign-key-id: "task-group-setup-id"

  - name: "Key"
    type: "string"
    description: ""

  - name: "Name"
    type: "string"
    description: ""

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

  - name: "OpUnitId"
    type: "integer"
    description: ""
    foreign-key-id: "operational-unit-id"

  - name: "SortOrder"
    type: "integer"
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