---
tap: "toggl"
version: "1.0"

name: "tasks"
doc-link: "https://github.com/toggl/toggl_api_docs/blob/master/chapters/tasks.md"
singer-schema: "https://github.com/singer-io/tap-toggl/blob/master/tap_toggl/schemas/tasks.json"
description: |
  The `{{ table.name }}` table contains info about the tasks in your {{ integration.display_name }} account.

  **Note**: Tasks are only available for {{ integration.display_name }} starter and other paid workspaces.

replication-method: "Key-based Incremental"
api-method:
    name: "Get workspace tasks"
    doc-link: "https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspaces.md#get-workspace-tasks"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The task ID."
    foreign-key-id: "task-id"

  - name: "at"
    type: "date-time"
    replication-key: true
    description: "The date and time the task was last updated."

  - name: "active"
    type: "boolean"
    description: "Indicates if the task is completed or not."

  - name: "estimated_seconds"
    type: "integer"
    description: "The estimated duration of the task, in seconds."

  - name: "name"
    type: "string"
    description: "The name of the task."

  - name: "pid"
    type: "integer"
    description: "The ID of the project associated with the task."
    foreign-key-id: "project-id"

  - name: "uid"
    type: "integer"
    description: "The ID of the user who is assigned to the task."
    foreign-key-id: "uid"

  - name: "wid"
    type: "integer"
    description: "The ID of the workspace associated with the task."
    foreign-key-id: "wid"
---