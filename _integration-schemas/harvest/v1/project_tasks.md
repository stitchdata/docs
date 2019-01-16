---
tap: "harvest"
version: "1.0"

name: "project_tasks"
doc-link: http://help.getharvest.com/api-v1/tasks-api/tasks/task-assignments#all-assigned-tasks-to-project
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/project_tasks.json
description: |
  The `project_tasks` table contains info about the tasks assigned to projects.

replication-method: "Key-based Incremental"
api-method:
  name: allAssignedTasksToProject
  doc-link: http://help.getharvest.com/api-v1/tasks-api/tasks/task-assignments/#all-assigned-tasks-to-project

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The project task ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the project task was updated."

  - name: "project_id"
    type: "integer"
    description: "The ID of the project the task is associated with."
    # foreign-keys:
    #   - table: "projects"
    #     attribute: "id"

  - name: "task_id"
    type: "integer"
    description: "The task ID."

  - name: "billable"
    type: "boolean"
    description: "Indicates if the task is billable."

  - name: "deactivated"
    type: "boolean"
    description: "Indicates if the project task has been deactivated."

  - name: "hourly_rate"
    type: "number"
    description: "The hourly rate of the project task."

  - name: "budget"
    type: "number"
    description: "The budget associated with the project task."

  - name: "created_at"
    type: "date-time"
    description: "The time the project task was created."

  - name: "estimate"
    type: "number"
    description: "The estimate associated with the project task."
---