---
tap: "looker"
version: "1"
key: "groups-in-group"

name: "groups_in_group"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/groups_in_group.json"
description: |
  The `{{ table.name }}` table contains info about the groups contained within groups in your {{ integration.display_name }} instance.

replication-method: "Full Table"

api-method:
  name: "Get all groups in group"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/group#get_all_groups_in_group"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The group ID."
    foreign-key-id: "group-id"

  - name: "can_add_to_content_metadata"
    type: "boolean"
    description: ""

  - name: "contains_current_user"
    type: "boolean"
    description: ""

  - name: "external_group_id"
    type: "string"
    description: ""

  - name: "externally_managed"
    type: "boolean"
    description: ""

  - name: "include_by_default"
    type: "boolean"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "parent_group_id"
    type: "string"
    description: ""
    foreign-key-id: "group-id"

  - name: "user_count"
    type: "integer"
    description: ""
---