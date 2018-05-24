---
tap: "harvest"
# version:

name: "project_users"
doc-link: http://help.getharvest.com/api-v1/users-api/users/user-assignments#get-users-assigned-to-projects
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/project_users.json
description: |
  The `project_users` table contains info about the users assigned to projects.

replication-method: "Key-based Incremental"
api-method:
  name: getUsersAssignedToProjects
  doc-link: http://help.getharvest.com/api-v1/users-api/users/user-assignments/#get-users-assigned-to-projects

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The project user ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the project user was updated."

  - name: "user_id"
    type: "integer"
    description: |
      The user ID of the project user.

      This is a foreign key for the `people` table (`people.id`) and can be used to retrieve other information about the user.
    # foreign-keys:
    #   - table: "people"
    #     attribute: "id"

  - name: "project_id"
    type: "integer"
    description: "The ID of the project the user is assigned to."
    # foreign-keys:
    #   - table: "projects"
    #     attribute: "id"

  - name: "is_project_manager"
    type: "boolean"
    description: "Indicates if the project user is a project manager."

  - name: "deactivated"
    type: "boolean"
    description: "Indicates if the project user has been deactivated."

  - name: "hourly_rate"
    type: "number"
    description: "The hourly rate of the project user."

  - name: "budget"
    type: "number"
    description: "If applicable, the budget of the project user."

  - name: "created_at"
    type: "date-time"
    description: "The time the project user was created."

  - name: "estimate"
    type: "number"
    description: "If applicable, the estimate associated with the project user."
---