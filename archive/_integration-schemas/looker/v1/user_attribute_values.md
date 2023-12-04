---
tap: "looker"
version: "1"
key: "user-attribute-values"

name: "user_attribute_values"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/user_attribute_values.json"
description: |
  The `{{ table.name }}` table contains info about the values for user attributes defined in your {{ integration.display_name }} instance.

replication-method: "Full Table"

api-method:
  name: "Get user attribute values"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/user#get_user_attribute_values"

attributes:
  - name: "user_attribute_id"
    type: "string"
    primary-key: true
    description: "The user attribute ID."
    foreign-key-id: "user-attribute-id"

  - name: "user_id"
    type: "string"
    primary-key: true
    description: "The user ID."
    foreign-key-id: "user-id"

  - name: "hidden_value_domain_whitelist"
    type: "string"
    description: ""

  - name: "label"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "rank"
    type: "integer"
    description: ""

  - name: "source"
    type: "string"
    description: ""

  - name: "user_can_edit"
    type: "boolean"
    description: ""

  - name: "value"
    type: "string"
    description: ""

  - name: "value_is_hidden"
    type: "boolean"
    description: ""
---