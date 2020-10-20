---
tap: "pendo"
version: "1"
key: "feature"

name: "features"
doc-link: "https://developers.pendo.io/docs/?bash#feature"
singer-schema: "https://github.com/singer-io/tap-pendo/blob/master/tap_pendo/schemas/features.json"
description: |
  The `{{ table.name }}` table contains info about app features listed in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Aggregation"
  doc-link: "https://api/v1/aggregation"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The feature ID."
    foreign-key-id: "feature-id"

  - name: "last_updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the feature was updated."

  - name: "color"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "created_by_user"
    type: "object"
    description: ""
    subattributes:
      - name: "app_id"
        type: "string"
        description: ""
        foreign-key-id: "app-id"

      - name: "app_wide"
        type: "boolean"
        description: ""

      - name: "event_property_configurations"
        type: "null"
        description: ""

      - name: "first"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "user-id"

      - name: "is_core_event"
        type: "boolean"
        description: ""

      - name: "last"
        type: "string"
        description: ""

      - name: "role"
        type: "integer"
        description: ""

      - name: "user_type"
        type: "string"
        description: ""

      - name: "username"
        type: "string"
        description: ""

      - name: "valid_through"
        type: "number"
        description: ""

  - name: "dirty"
    type: "boolean"
    description: ""

  - name: "element_path_rules"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "group"
    type: "object"
    description: ""
    subattributes:
      - name: "color"
        type: "string"
        description: ""

      - name: "created_at"
        type: "date-time"
        description: ""

      - name: "created_by_user"
        type: "object"
        description: ""
        subattributes: &full-user-attributes
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

          - name: "type"
            type: "string"
            description: ""

          - name: "username"
            type: "string"
            description: ""

      - name: "description"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "items"
        type: "varies"
        description: ""

      - name: "last_updated_at"
        type: "date-time"
        description: ""

      - name: "last_updated_by_user"
        type: "object"
        description: ""
        subattributes:
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

      - name: "length"
        type: "integer"
        description: ""

      - name: "name"
        type: "string"
        description: ""

  - name: "kind"
    type: "string"
    description: ""

  - name: "last_updated_by_user"
    type: "object"
    description: ""
    subattributes: *full-user-attributes

  - name: "name"
    type: "string"
    description: ""

  - name: "pageId"
    type: "string"
    description: ""
    foreign-key-id: "page-id"

  - name: "root_version_id"
    type: "string"
    description: ""

  - name: "stable_version_id"
    type: "string"
    description: ""
---