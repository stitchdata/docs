---
tap: "asana"
version: "1"
key: "task"

name: "tasks"
doc-link: "https://asana.com/developers/api-reference/tasks"
singer-schema: "https://github.com/singer-io/tap-asana/blob/master/tap_asana/schemas/tasks.json"
description: |
  The `{{ table.name }}` table contains info about the tasks in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The task ID."
    #foreign-key-id: "task-id"

  - name: "modified_at"
    type: "date-time"
    replication-key: true
    description: "The time the task was last modified."

  - name: "assignees"
    type: "array"
    description: "A list of users assigned to the task."
    subattributes:
      - name: "gid"
        type: "string"
        description: "The assignee's GID."

      - name: "id"
        type: "integer"
        description: "The assignee's ID."
        foreign-key-id: "user-id"

      - name: "resource_type"
        type: "string"
        description: "This will be `user`."

  - name: "assignee_status"
    type: "string"
    description: "The scheduling status of the task for the user it is assigned to."

  - name: "completed"
    type: "boolean"
    description: "Indicates if the task has been completed or not."

  - name: "completed_at"
    type: "date-time"
    description: "The time at which the task was completed. This will be `null` until `completed: true`."

  - name: "created_at"
    type: "date-time"
    description: "The time the task was created."

  - name: "due_at"
    type: "date-time"
    description: "The date and time on which the task is due. This will be `null` if the task has no due time."

  - name: "due_on"
    type: "date-time"
    description: "The date on which the task is due. This will be `null` if the task has no due date."

  - name: "external"
    type: "string"
    description: ""

  - name: "followers"
    type: "array"
    description: "A list of users following the task."
    subattributes:
      - name: "gid"
        type: "string"
        description: "The follower's GID."

      - name: "id"
        type: "integer"
        description: "The follower's ID."
        foreign-key-id: "user-id"

      - name: "resource_type"
        type: "string"
        description: "This will be `user`."

  - name: "gid"
    type: "string"
    description: "The task's GID."

  - name: "hearted"
    type: "boolean"
    description: ""

  - name: "hearts"
    type: "string"
    description: ""

  - name: "memberships"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: "The name of the task."

  - name: "notes"
    type: "string"
    description: "Any notes associated with the task."

  - name: "num_hearts"
    type: "integer"
    description: "The number of users who have hearted this task."

  - name: "parent"
    type: "string"
    description: "The parent of the task, or `null` if this is not a subtask."
    foreign-key-id: "task-id"

  - name: "projects"
    type: "array"
    description: "A list of projects the task is associated with."
    subattributes:
      - name: "gid"
        type: "string"
        description: "The project's GID."

      - name: "id"
        type: "integer"
        description: "The project ID."
        foreign-key-id: "project-id"

      - name: "resource_type"
        type: "string"
        description: "This will be `project`."

  - name: "workspace"
    type: "object"
    description: "Details about the workspace or organization the task is associated with."
    subattributes:
      - name: "gid"
        type: "string"
        description: "The workspace's GID."

      - name: "id"
        type: "integer"
        description: "The workspace's ID."
        foreign-key-id: "workspace-id"

      - name: "resource_type"
        type: "string"
        description: "This will be `workspace`."
---