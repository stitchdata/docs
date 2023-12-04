---
tap: "looker"
version: "1"
key: "user-attribute-group-value"

name: "user_attribute_group_values"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/user_attribute_group_values.json"
description: |
  The `{{ table.name }}` table contains info about the values of user attributes defined by user groups in your {{ integration.display_name }} instance.

replication-method: "Full Table"

api-method:
  name: "Get user attribute group values"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/user-attribute#get_user_attribute_group_values"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The user attribute group value ID."
    foreign-key-id: "user-attribute-group-value-id"

  - name: "group_id"
    type: "string"
    description: ""
    foreign-key-id: "group-id"

  - name: "rank"
    type: "integer"
    description: ""

  - name: "user_attribute_id"
    type: "string"
    description: ""
    foreign-key-id: "user-attribute-id"

  - name: "value"
    type: "string"
    description: ""

  - name: "value_is_hidden"
    type: "boolean"
    description: ""
---