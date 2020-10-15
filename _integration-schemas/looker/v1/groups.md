---
tap: "looker"
version: "1"
key: ""

name: "groups"
doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/group#get_all_groups"
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/groups.json"
description: |
  The `{{ table.name }}` table contains information about all groups in your {{ integration.display_name }} account.
  
replication-method: "Full Table"

api-method:
    name: "Get All Groups"
    doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/group#get_all_groups"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The group ID."

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
  - name: "user_count"
    type: "integer"
    description: ""
---
