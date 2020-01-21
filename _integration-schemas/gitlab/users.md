---
tap: "gitlab"
version: "1"

name: "users"
doc-link: https://gitlab.com/help/api/users.md#list-users
singer-schema: https://github.com/singer-io/tap-gitlab/blob/master/tap_gitlab/schemas/users.json
description: |
  The `{{ table.name }}` table contains info about the users in your {{ integration.display_name }} account.

replication-method: "Full Table"
api-method:
  name: "listUsers"
  doc-link: https://gitlab.com/help/api/users.md#list-users

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The user ID."
    foreign-key-id: "user-id"

  - name: "username"
    type: "string"
    description: "The user's username."

  - name: "name"
    type: "string"
    description: "The user's name."

  - name: "state"
    type: "string"
    description: "The user's current state. Ex: `active`"

  - name: "avatar_url"
    type: "string"
    description: "The URL of the user's avatar."

  - name: "web_url"
    type: "string"
    description: "The URL of the user's profile."
---