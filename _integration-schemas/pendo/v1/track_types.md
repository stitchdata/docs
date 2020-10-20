---
tap: "pendo"
version: "1"
key: ""

name: "track_types"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-pendo/blob/master/tap_pendo/schemas/track_types.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: "Key-based Incremental"

api-method:
  name: "Aggregation"
  doc-link: "https://api/v1/aggregation"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "track-type-id"

  - name: "color"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "created_by_user"
    type: "object"
    description: ""
    subattributes: &user-attributes
      - name: "first"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "user-id"

      - name: "last"
        type: "string"
        description: ""

      - name: "role"
        type: "integer"
        description: ""

      - name: "username"
        type: "string"
        description: ""

  - name: "dirty"
    type: "boolean"
    description: ""

  - name: "group"
    type: "object"
    description: ""
    subattributes:
      - name: "color"
        type: "string"
        description: ""

      - name: "description"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "group-id"

      - name: "length"
        type: "integer"
        description: ""

      - name: "name"
        type: "string"
        description: ""

  - name: "kind"
    type: "string"
    description: ""

  - name: "last_updated_at"
    type: "date-time"
    description: ""

  - name: "last_updated_by_user"
    type: "object"
    description: ""
    subattributes: *user-attributes

  - name: "name"
    type: "string"
    description: ""

  - name: "root_version_id"
    type: "string"
    description: ""

  - name: "stable_version_id"
    type: "string"
    description: ""

  - name: "track_type_name"
    type: "boolean"
    description: ""

  - name: "track_type_rules"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "integer"
        description: ""
---