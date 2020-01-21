---
tap: "harvest"
version: "1"

name: "tasks"
doc-link: http://help.getharvest.com/api-v1/tasks-api/tasks/create-show-tasks/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/tasks.json
description: |
  The `tasks` table contains info about the tasks in your Harvest account.

replication-method: "Key-based Incremental"
api-method:
  name: showAllTasks
  doc-link: http://help.getharvest.com/api-v1/tasks-api/tasks/create-show-tasks/#show-all-tasks

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The task ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the task was last updated."

  - name: "name"
    type: "string"
    description: "The name of the task."

  - name: "billable_by_default"
    type: "boolean"
    description: "Indicates whether default tasks should be marked as billable when creating a new project."

  - name: "created_at"
    type: "date-time"
    description: "The time the task was created."

  - name: "is_default"
    type: "boolean"
    description: "Indicates if the task should be automatically added to new projects."

  - name: "default_hourly_rate"
    type: "number"
    description: "The hourly rate to use for the task when it is added to a project."

  - name: "deactivated"
    type: "boolean"
    description: "Indicates if the task is active or archived."
---