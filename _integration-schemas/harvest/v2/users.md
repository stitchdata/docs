---
tap: "harvest"
version: "2.0"

name: "users"
doc-link: https://help.getharvest.com/api-v2/users-api/users/users/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/users.json
description: |
  The `{{ table.name }}` table contains info about the users in your Harvest account.

replication-method: "Key-based Incremental"

api-method:
  name: List all users
  doc-link: https://help.getharvest.com/api-v2/users-api/users/users#list-all-users

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The user ID."
    foreign-key-id: "user-id"

  - name: "updated_at"
    type: "string"
    replication-key: true
    description: "The date and time when the user was last updated."

  - name: "first_name"
    type: "string"
    description: "The first name of the user."

  - name: "last_name"
    type: "string"
    description: "The last name of the user."

  - name: "email"
    type: "string"
    description: "The email address of the user."

  - name: "telephone"
    type: "string"
    description: "The telephone number of the user."

  - name: "timezone"
    type: "string"
    description: "The user's timezone."

  - name: "has_access_to_all_future_projects"
    type: "boolean"
    description: "If `true`, the user will be automatically added to future projects."

  - name: "is_contractor"
    type: "boolean"
    description: "If `true`, the user is a contractor."

  - name: "is_admin"
    type: "boolean"
    description: "If `true`, the user has admin permissions in {{ integration.display_name }}."

  - name: "is_project_manager"
    type: "boolean"
    description: "If `true`, the user has project manager permissions."

  - name: "can_see_rates"
    type: "boolean"
    description: "If `true`, the user can see billable rates on projects."

  - name: "can_create_projects"
    type: "boolean"
    description: "If `true`, the user can create projects."

  - name: "can_create_invoices"
    type: "boolean"
    description: "If `true`, the user can create invoices."

  - name: "is_active"
    type: "boolean"
    description: "If `true`, the user is an active user."

  - name: "weekly_capacity"
    type: "integer"
    description: |
      The number of hours the user is available to work, in seconds.

      For example: If a user is available for 35 hours, the value of this field will be `126000`. (`(60 seconds * 60 minutes) * 35 hours = 126000 seconds`)

  - name: "default_hourly_rate"
    type: "number"
    description: "The billable rate to use for this user when they're added to a project."

  - name: "cost_rate"
    type: "number"
    description: "The cost rate to use for this user when calculating a project's cost versus billable amount."

  - name: "avatar_url"
    type: "string"
    description: "The URL to the user's avatar image."

  - name: "created_at"
    type: "string"
    description: "The date and time when the user was created."
---