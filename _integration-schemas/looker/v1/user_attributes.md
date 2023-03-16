---
tap: "looker"
version: "1"
key: "user-attribute"

name: "user_attributes"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/user_attributes.json"
description: |
  The `{{ table.name }}` table contains info about user attributes in your {{ integration.display_name }} instance.

replication-method: "Full Table"

api-method:
  name: "Get all user attributes"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/user-attribute#get_all_user_attributes"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The user attribute ID."
    foreign-key-id: "user-attribute-id"

  - name: "default_value"
    type: "string"
    description: ""

  - name: "hidden_value_domain_whitelist"
    type: "string"
    description: ""

  - name: "is_permanent"
    type: "boolean"
    description: ""

  - name: "is_system"
    type: "boolean"
    description: ""

  - name: "label"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "user_can_edit"
    type: "boolean"
    description: ""

  - name: "user_can_view"
    type: "boolean"
    description: ""

  - name: "value_is_hidden"
    type: "boolean"
    description: ""
---