---
tap: "pendo"
version: "1"
key: "page"

name: "pages"
doc-link: "https://developers.pendo.io/docs/?bash#page"
singer-schema: "https://github.com/singer-io/tap-pendo/blob/master/tap_pendo/schemas/pages.json"
description: |
  The `{{ table.name }}` table contains info about specific pages in your {{ integration.display_name }} app.

replication-method: "Key-based Incremental"

api-method:
  name: "Aggregation"
  doc-link: "https://api/v1/aggregation"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The page ID."
    foreign-key-id: "page-id"

  - name: "last_updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the page was last updated."

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

      - name: "created_at"
        type: "date-time"
        description: ""

      - name: "created_by_user"
        type: "object"
        description: ""
        subattributes: *user-attributes

      - name: "description"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "group-id"

      - name: "last_updated_at"
        type: "date-time"
        description: ""

      - name: "last_updated_by_user"
        type: "object"
        description: ""
        subattributes: *user-attributes

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
    subattributes: *user-attributes

  - name: "name"
    type: "string"
    description: ""

  - name: "root_version_id"
    type: "string"
    description: ""

  - name: "rules"
    type: "array"
    description: ""
    subattributes:
      - name: "designer_hint"
        type: "string"
        description: ""

      - name: "parsed_rule"
        type: "string"
        description: ""

      - name: "rule"
        type: "string"
        description: ""

  - name: "stable_version_id"
    type: "string"
    description: ""
---