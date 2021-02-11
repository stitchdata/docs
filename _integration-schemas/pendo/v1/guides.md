---
tap: "pendo"
version: "1"
key: "guide"

name: "guides"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-pendo/blob/master/tap_pendo/schemas/guides.json"
description: |
  The `{{ table.name }}` table contains info about the guides in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"
replication-key:
  name: "browserTime"

api-method:
  name: "Aggregation"
  doc-link: "https://api/v1/aggregation"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The guide ID."
    foreign-key-id: "guide-id"

  - name: "last_updated_at"
    type: "date-time"
    description: ""

  - name: "attributes"
    type: "object"
    description: ""
    subattributes:
      - name: "badge"
        type: "object"
        description: ""
        subattributes:
          - name: "can_change_badge_color"
            type: "boolean"
            description: ""

          - name: "color"
            type: "string"
            description: ""

          - name: "height"
            type: "integer"
            description: ""

          - name: "image_url"
            type: "string"
            description: ""

          - name: "is_only_show_once"
            type: "boolean"
            description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "offsets"
            type: "object"
            description: ""
            subattributes:
              - name: "left"
                type: "integer"
                description: ""

              - name: "right"
                type: "integer"
                description: ""

              - name: "top"
                type: "integer"
                description: ""

          - name: "position"
            type: "string"
            description: ""

          - name: "show_on_event"
            type: "string"
            description: ""

          - name: "use_hover"
            type: "string"
            description: ""

          - name: "width"
            type: "integer"
            description: ""

      - name: "device"
        type: "object"
        description: ""
        subattributes:
          - name: "type"
            type: "string"
            description: ""

      - name: "priority"
        type: "integer"
        description: ""

      - name: "type"
        type: "string"
        description: ""

  - name: "audience"
    type: "array"
    description: ""
    subattributes:
      - name: "identified"
        type: "string"
        description: ""

      - name: "select"
        type: "object"
        description: ""
        subattributes:
          - name: "visitor_id"
            type: "string"
            description: ""
            foreign-key-id: "visitor-id"

      - name: "source"
        type: "object"
        description: ""
        subattributes:
          - name: "visitors"
            type: "null"
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

  - name: "is_multi_step"
    type: "boolean"
    description: ""

  - name: "kind"
    type: "string"
    description: ""

  - name: "lastUpdated_by_user"
    type: "object"
    description: ""
    subattributes: *user-attributes

  - name: "launch_method"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "published_at"
    type: "date-time"
    description: ""

  - name: "reset_at"
    type: "date-time"
    description: ""

  - name: "root_version_id"
    type: "string"
    description: ""

  - name: "stable_version_id"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "steps"
    type: "array"
    description: ""
    subattributes:
      - name: "advance_method"
        type: "string"
        description: ""

      - name: "attributes"
        type: "object"
        description: ""
        subattributes:
          - name: "auto_height"
            type: "boolean"
            description: ""

          - name: "css"
            type: "string"
            description: ""

          - name: "height"
            type: "integer"
            description: ""

          - name: "width"
            type: "integer"
            description: ""

      - name: "content_type"
        type: "string"
        description: ""

      - name: "content_url"
        type: "string"
        description: ""

      - name: "content_url_css"
        type: "string"
        description: ""

      - name: "content_url_js"
        type: "string"
        description: ""

      - name: "element_path_rule"
        type: "string"
        description: ""

      - name: "guide_id"
        type: "string"
        description: ""
        foreign-key-id: "guide-id"

      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "guide-step-id"

      - name: "last_updated_at"
        type: "date-time"
        description: ""

      - name: "page_id"
        type: "string"
        description: ""
        foreign-key-id: "page-id"

      - name: "rank"
        type: "integer"
        description: ""

      - name: "regex_url_rule"
        type: "string"
        description: ""

      - name: "reset_at"
        type: "date-time"
        description: ""

      - name: "type"
        type: "string"
        description: ""
---