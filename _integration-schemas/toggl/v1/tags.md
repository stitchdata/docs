---
tap: "toggl"
version: "1.0"

name: "tags"
doc-link: "https://github.com/toggl/toggl_api_docs/blob/master/chapters/tags.md"
singer-schema: "https://github.com/singer-io/tap-toggl/blob/master/tap_toggl/schemas/tags.json"
description: |
  The `{{ table.name }}` table contains info about the tags in your {{ integration.display_name }} account.

replication-method: "Full Table"
api-method:
    name: "Get workspace tags"
    doc-link: "https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspaces.md#get-workspace-tags"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The tag ID."
    foreign-key-id: "tag-id"

  - name: "name"
    type: "string"
    description: "The name of the tag."

  - name: "wid"
    type: "integer"
    description: "The workspace ID where the tag is used."
    foreign-key-id: "workspace-id"
---