---
tap: "helpscout"
version: "1.0"

key: "user"
name: "users"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-helpscout/blob/master/tap_helpscout/schemas/users.json"
description: |
  The `{{ table.name }}` table contains info about the users in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List users"
    doc-link: "https://developer.helpscout.com/mailbox-api/endpoints/users/list/"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The user ID."
    foreign-key-id: "user-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The UTC time the user was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The UTC time the user was created."

  - name: "email"
    type: "string"
    description: "The user's email address."

  - name: "first_name"
    type: "string"
    description: "The user's first name."

  - name: "last_name"
    type: "string"
    description: "The user's last name."

  - name: "photo_url"
    type: "string"
    description: "The URL of the user's photo."

  - name: "role"
    type: "string"
    description: |
      The role of the user. Possible values are:

      - `owner`
      - `admin`
      - `user`

  - name: "timezone"
    type: "string"
    description: "The user's timezone."

  - name: "type"
    type: "string"
    description: |
      The type of the user. Possible values are:

      - `user`
      - `team`
---