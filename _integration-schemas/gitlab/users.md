---
tap: "gitlab"
# version: ""

name: "users"
doc-link: https://gitlab.com/help/api/users.md#list-users
singer-schema: https://github.com/singer-io/tap-gitlab/blob/master/tap_gitlab/schemas/users.json
description: |
  The `users` table contains info about the users in your GitLab account.

replication-method: "Full Table"
api-method:
  name: "listUsers"
  doc-link: https://gitlab.com/help/api/users.md#list-users

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The user ID."

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