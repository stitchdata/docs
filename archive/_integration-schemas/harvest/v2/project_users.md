---
tap: "harvest"
version: "2"

name: "project_users"
doc-link: https://help.getharvest.com/api-v2/projects-api/projects/user-assignments/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/project_users.json
description: |
  The `{{ table.name }}` table contains info about the users assigned to projects.

replication-method: "Key-based Incremental"

api-method:
  name: List all user assignments
  doc-link: https://help.getharvest.com/api-v2/projects-api/projects/user-assignments/

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The project user ID."
    foreign-key-id: "project-user-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the project user was updated."

  - name: "budget"
    type: "number"
    description: "If applicable, the budget of the project user."

  - name: "created_at"
    type: "string"
    description: "The time the project user was created."

  - name: "hourly_rate"
    type: "number"
    description: "The hourly rate of the project user."

  - name: "is_active"
    type: "boolean"
    description: "If `true`, the project user is active."

  - name: "is_project_manager"
    type: "boolean"
    description: "If `true`, the project user is a project manager."

  - name: "project_id"
    type: "integer"
    description: "The ID of the project the user is assigned to."
    foreign-key-id: "project-id"

  - name: "user_id"
    type: "integer"
    description: "The user ID of the project user."
    foreign-key-id: "user-id"
---