---
tap: "toggl"
version: "1.0"

name: "groups"
doc-link: "https://github.com/toggl/toggl_api_docs/blob/master/chapters/groups.md"
singer-schema: "https://github.com/singer-io/tap-toggl/blob/master/tap_toggl/schemas/groups.json"
description: |
  The `{{ table.name }}` table contains info about the groups in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"
api-method:
    name: "Get workspace groups"
    doc-link: "https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspaces.md#get-workspace-groups"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The group ID."
    foreign-key-id: "group-id"

  - name: "at"
    type: "date-time"
    replication-key: true
    description: "The date and time the group was last updated."

  - name: "name"
    type: "string"
    description: "The name of the group."

  - name: "wid"
    type: "integer"
    description: "The workspace ID where the group is used."
    foreign-key-id: "workspace-id"
---