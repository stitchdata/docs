---
tap: "deputy"
version: "1.0"
key: "task-setup"

name: "task_setups"
doc-link: "https://www.deputy.com/api-doc/Resources/TaskSetup"

description: |
  The `{{ table.name }}` table contains info about task setups.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The task setup ID."
    foreign-key-id: "task-setup-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the task setup was last modified."

  - name: "GroupId"
    type: "integer"
    description: ""
    foreign-key-id: "task-group-setup-id"

  - name: "Type"
    type: "integer"
    description: ""

  - name: "Parent"
    type: "integer"
    description: ""

  - name: "Question"
    type: "string"
    description: ""

  - name: "Default"
    type: "string"
    description: ""

  - name: "SortOrder"
    type: "integer"
    description: ""

  - name: "Schedule"
    type: "integer"
    description: ""
    foreign-key-id: "schedule-id"

  - name: "OnYes"
    type: "string"
    description: ""

  - name: "OnNo"
    type: "string"
    description: ""

  - name: "RenderFunc"
    type: "string"
    description: ""

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "AvailableAfter"
    type: "string"
    description: ""

  - name: "RepeatIfNotCompleted"
    type: "boolean"
    description: ""

  - name: "Time"
    type: "string"
    description: ""

  - name: "Section"
    type: "string"
    description: ""

  - name: "Priority"
    type: "string"
    description: ""

  - name: "Helptext"
    type: "string"
    description: ""

  - name: "SupercedePrev"
    type: "boolean"
    description: ""

  - name: "Colour"
    type: "string"
    description: ""

  - name: "OnStart"
    type: "string"
    description: ""

  - name: "OnSubmit"
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