---
tap: "harvest"
version: "2.0"

name: "tasks"
doc-link: https://help.getharvest.com/api-v2/tasks-api/tasks/tasks/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/tasks.json
description: |
  The `{{ table.name }}` table contains info about the tasks in your Harvest account.

replication-method: "Key-based Incremental"

api-method:
  name: List all tasks
  doc-link: https://help.getharvest.com/api-v2/tasks-api/tasks/tasks#list-all-tasks

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The task ID."
    foreign-key-id: "task-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The date and time the task was last updated."

  - name: "name"
    type: "string"
    description: "The name of the task."

  - name: "billable_by_default"
    type: "boolean"
    description: "If `true`, default tasks should be marked as billable when creating a new project."

  - name: "default_hourly_rate"
    type: "number"
    description: "The hourly rate to use for the task when it is added to a project."

  - name: "is_default"
    type: "boolean"
    description: "If `true`, the task should be automatically added to new projects."

  - name: "is_active"
    type: "boolean"
    description: "If `true`, the task is active."

  - name: "created_at"
    type: "string"
    description: "The date and time the task was created."
---