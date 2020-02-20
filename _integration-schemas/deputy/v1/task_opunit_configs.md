---
tap: "deputy"
version: "1"
key: "task-opunit-config"

name: "task_opunit_configs"
doc-link: "https://www.deputy.com/api-doc/Resources/TaskOpunitConfig"

description: |
  The `{{ table.name }}` table contains info about task operational unit configurations.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The task operational unit configuration ID."
    #foreign-key-id: "task-opunit-config-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the task operational unit configuration was last modified."

  - name: "TaskSetupId"
    type: "integer"
    description: ""
    foreign-key-id: "task-setup-id"

  - name: "TaskGroupId"
    type: "integer"
    description: ""
    foreign-key-id: "task-group-id"

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "SortOrder"
    type: "integer"
    description: ""

  - name: "OpUnitId"
    type: "integer"
    description: ""
    foreign-key-id: "operational-unit-id"

  - name: "Schedule"
    type: "integer"
    description: ""
    foreign-key-id: "schedule-id"

  - name: "Type"
    type: "integer"
    description: ""

  - name: "AvailableAfter"
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