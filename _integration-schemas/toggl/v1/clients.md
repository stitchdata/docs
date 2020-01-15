---
tap: "toggl"
version: "1"

name: "clients"
doc-link: "https://github.com/toggl/toggl_api_docs/blob/master/chapters/clients.md"
singer-schema: "https://github.com/singer-io/tap-toggl/blob/master/tap_toggl/schemas/clients.json"
description: |
  The `{{ table.name }}` table contains info about the clients in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"
api-method:
    name: "Get workspace clients"
    doc-link: "https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspaces.md#get-workspace-clients"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The client ID."
    foreign-key-id: "client-id"

  - name: "at"
    type: "date-time"
    replication-key: true
    description: "The date and time the client was last updated."

  - name: "cur"
    type: "string"
    description: ""

  - name: "hrate"
    type: "integer"
    description: "The hourly rate for the client."

  - name: "name"
    type: "string"
    description: "The name of the client."

  - name: "notes"
    type: "string"
    description: "Notes for the client."

  - name: "wid"
    type: "integer"
    description: "The workspace ID where the client is used."
    foreign-key-id: "workspace-id"
---