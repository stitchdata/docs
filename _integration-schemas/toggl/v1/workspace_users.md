---
tap: "toggl"
version: "1.0"

name: "workspace_users"
doc-link: "https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspace_users.md"
singer-schema: "https://github.com/singer-io/tap-toggl/blob/master/tap_toggl/schemas/workspace_users.json"
description: |
  The `{{ table.name }}` table contains info about the users in a workspace.

replication-method: "Key-based Incremental"
api-method:
    name: "Get workspace users for a workspace"
    doc-link: "https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspace_users.md#get-workspace-users"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The workspace user ID."
    foreign-key-id: "workspace-user-id"

  - name: "at"
    type: "date-time"
    replication-key: true
    description: "The date and time the workspace user was last updated."

  - name: "active"
    type: "boolean"
    description: "Indicates if the workspace user has accepted the invitation to the workspace."

  - name: "admin"
    type: "boolean"
    description: "Indicates if the user is a workspace admin."

  - name: "email"
    type: "string"
    description: "The workspace user's email address."

  - name: "invite_url"
    type: "string"
    description: "The URL for accepting the workspace invitation, if the user hasn't yet accepted the invitation."

  - name: "name"
    type: "string"
    description: "The name of the workspace user."

  - name: "uid"
    type: "integer"
    description: "The ID of the user associated with the workspace user."
    foreign-key-id: "user-id"

  - name: "wid"
    type: "integer"
    description: "The ID of the workspace associated with the workspace user."
    foreign-key-id: "workspace-id"
---