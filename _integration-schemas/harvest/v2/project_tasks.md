---
tap: "harvest"
version: "2.0"

name: "project_tasks"
doc-link: https://help.getharvest.com/api-v2/projects-api/projects/task-assignments/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/project_tasks.json
description: |
  The `{{ table.name }}` table contains info about the tasks assigned to projects.

replication-method: "Key-based Incremental"
api-method:
  name: List all task assignments
  doc-link: https://help.getharvest.com/api-v2/projects-api/projects/task-assignments#list-all-task-assignments

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The project task ID."
    foreign-key-id: "project-task-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the project task was updated."

  - name: "billable"
    type: "boolean"
    description: "If `true`, the project task is billable."

  - name: "budget"
    type: "number"
    description: "The budget associated with the project task."

  - name: "created_at"
    type: "date-time"
    description: "The time the project task was created."

  - name: "hourly_rate"
    type: "number"
    description: "The hourly rate of the project task."

  - name: "is_active"
    type: "boolean"
    description: "If `true`, the project task is active."

  - name: "project_id"
    type: "integer"
    description: "The ID of the project the task is associated with."
    foreign-key-id: "project-id"

  - name: "task_id"
    type: "integer"
    description: "The task ID."
    foreign-key-id: "task-id"
---