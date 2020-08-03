---
tap: "toggl"
version: "1"

name: "projects"
doc-link: "https://github.com/toggl/toggl_api_docs/blob/master/chapters/projects.md"
singer-schema: "https://github.com/singer-io/tap-toggl/blob/master/tap_toggl/schemas/projects.json"
description: |
  The `{{ table.name }}` table contains info about the projects in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"
api-method:
    name: "Get workspace projects"
    doc-link: "https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspaces.md#get-workspace-projects"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The project ID."
    foreign-key-id: "project-id"

  - name: "at"
    type: "date-time"
    replication-key: true
    description: "The date and time the project was last updated."

  - name: "active"
    type: "boolean"
    description: "Indicates whether the project is archived or not."

  - name: "billable"
    type: "boolean"
    description: "Indicates whether the project is billable or not. **Note**: This is only applicable to pro workspaces."

  - name: "cid"
    type: "integer"
    description: "The client ID."
    foreign-key-id: "client-id"

  - name: "is_private"
    type: "boolean"
    description: "Indicates whether the project is accessible only by project users or for all workspace users."

  - name: "name"
    type: "string"
    description: "The name of the project."

  - name: "wid"
    type: "integer"
    description: "The workspace ID where the project is saved."
    foreign-key-id: "workspace-id"
---