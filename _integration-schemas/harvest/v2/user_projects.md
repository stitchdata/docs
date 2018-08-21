---
tap: "harvest"
version: "2.0"

name: "user_projects"
doc-link: https://help.getharvest.com/api-v2/users-api/users/project-assignments/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/user_projects.json
description: |
  The `{{ table.name }}` table contains info about the project assignments users are assigned to.

replication-method: "Key-based Incremental"

api-method:
  name: 
  doc-link: https://help.getharvest.com/api-v2/users-api/users/project-assignments/

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The project assignment ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The date and time when the project assignment was last updated."

  - name: "budget"
    type: "number"
    description: "The budget used when the project's `budget_by` is `Person`."

  - name: "client_id"
    type: "integer"
    description: "The ID of the associated client."
    foreign-key-id: "client-id"

  - name: "created_at"
    type: "string"
    description: "The date and time when the project assignment was created."

  - name: "is_active"
    type: "boolean"
    description: "If `true`, the project assignment is active."

  - name: "is_project_manager"
    type: "boolean"
    description: "If `true`, the user has project manager permissions for the project."

  - name: "hourly_rate"
    type: "number"
    description: "The rate used when the project's `bill_by` is `People`."

  - name: "project_id"
    type: "integer"
    description: "The ID of the associated project."
    foreign-key-id: "project-id"

  - name: "user_id"
    type: "integer"
    description: "The ID of the user associated with the project assignment."
    foreign-key-id: "user-id"
---