---
tap: "asana"
version: "2"
key: "workspace"

name: "workspaces"
doc-link: "https://asana.com/developers/api-reference/workspaces"
singer-schema: "https://github.com/singer-io/tap-asana/blob/master/tap_asana/schemas/workspaces.json"
description: |
  The `{{ table.name }}` table contains info about the workspaces associated with your {{ integration.display_name }} account.

replication-method: "Full Table"

attributes:
  - name: "gid"
    type: "integer"
    primary-key: true
    description: "The workspace's GID."
    foreign-key-id: "workspace-id"

  - name: "is_organization"
    type: "boolean"
    description: "Indicates if the workspace is an organization or not."

  - name: "name"
    type: "string"
    description: "The name of the workspace."

  - name: "resource_type"
    type: "string"
    description: "This will be `workspace`."
---
