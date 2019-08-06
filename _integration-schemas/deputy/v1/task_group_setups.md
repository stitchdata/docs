---
tap: "deputy"
version: "1.0"
key: "task-group-setup"

name: "task_group_setups"
doc-link: "https://www.deputy.com/api-doc/Resources/TaskGroupSetup"

description: |
  The `{{ table.name }}` table contains info about task group setups.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The task group setup ID."
    foreign-key-id: "task-group-setup-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the task group setup was last modified."

  - name: "Key"
    type: "string"
    description: ""

  - name: "Name"
    type: "string"
    description: ""

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "Compulsory"
    type: "boolean"
    description: ""

  - name: "Notification"
    type: "string"
    description: ""

  - name: "Deadline"
    type: "number"
    description: ""

  - name: "Plugins"
    type: "string"
    description: ""

  - name: "Oncreate"
    type: "string"
    description: ""

  - name: "Onsubmit"
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