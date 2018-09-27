---
tap: "harvest"
version: "1.0"

name: "people"
doc-link: http://help.getharvest.com/api-v1/users-api/users/managing-users/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/people.json
description: |
  The `people` table contains info about the people - or users - in your Harvest account.

  **Note**: These are **internal** users. Info about external users, or clients, is in the `clients` table.

replication-method: "Key-based Incremental"
api-method:
  name: showAllUsers
  doc-link: http://help.getharvest.com/api-v1/users-api/users/managing-users/#show-all-users

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the Harvest user."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the user was updated."

  - name: "email"
    type: "string"
    description: "The email address of the user."

  - name: "created_at"
    type: "date-time"
    description: "The time the user was created."

  - name: "is_admin"
    type: "boolean"
    description: "Indicates if the user is an Admin in your Harvest account."

  - name: "first_name"
    type: "string"
    description: "The first name of the user."

  - name: "last_name"
    type: "string"
    description: "The last name of the user."

  - name: "timezone"
    type: "string"
    description: "If the user doesn't reside in the default timezone for your Harvest account, this field will contain their timezone."

  - name: "is_contractor"
    type: "boolean"
    description: "Indicates if the user is a contractor."

  - name: "telephone"
    type: "string"
    description: "The telephone number of the user."

  - name: "is_active"
    type: "boolean"
    description: "Indicates if the user is active or archived."

  - name: "has_access_to_all_future_projects"
    type: "boolean"
    description: "Indicates if the user will automatically be assigned to all new projects."

  - name: "default_hourly_rate"
    type: "number"
    description: "The default hourly rate of the user in new projects, if no rate is specified."

  - name: "department"
    type: "string"
    description: "The department the user is a part of."

  - name: "wants_newsletter"
    type: "boolean"
    description: "Indicates if the user should receive the newsletter."

  - name: "cost_rate"
    type: "number"
    description: "The cost (internal) rate of the user."

  - name: "identity_account_id"
    type: "integer"
    description: "The identity account ID associated with the user."

  - name: "indentity_user_id"
    type: "integer"
    description: "The identity user ID associated with the user."
---