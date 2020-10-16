---
tap: "looker"
version: "1"
key: "content-favorite"

name: "content_favorites"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/content_favorites.json"
description: |
  The `{{ table.name }}` table contains info about users' favorite content in your {{ integration.display_name }} instance.

replication-method: "Full Table"

api-method:
  name: "Search favorite contents"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/content#search_favorite_contents"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The content favorite ID."
    foreign-key-id: "content-favorite-id"

  - &content-metadata-id
    name: "content_metadata_id"
    type: "string"
    description: ""
    foreign-key-id: "content-metadata-id"

  - name: "dashboard"
    type: "object"
    description: ""
    subattributes:
      - name: "content_favorite_id"
        type: "string"
        description: ""
        foreign-key-id: "content-favorite-id"

      - *content-metadata-id

      - name: "description"
        type: "string"
        description: ""

      - name: "folder"
        type: "object"
        description: ""
        subattributes:
          - name: "child_count"
            type: "integer"
            description: ""

          - name: "content_metadata_id"
            type: "string"
            description: ""
            foreign-key-id: "content-metadata-id"

          - &creator-id
            name: "creator_id"
            type: "string"
            description: ""
            foreign-key-id: "user-id"

          - name: "external_id"
            type: "string"
            description: ""

          - name: "id"
            type: "string"
            description: ""
            foreign-key-id: "folder-id"

          - name: "is_embed"
            type: "boolean"
            description: ""

          - name: "is_embed_shared_root"
            type: "boolean"
            description: ""

          - name: "is_embed_users_root"
            type: "boolean"
            description: ""

          - name: "is_personal"
            type: "boolean"
            description: ""

          - name: "is_personal_descendant"
            type: "boolean"
            description: ""

          - name: "is_shared_root"
            type: "boolean"
            description: ""

          - name: "is_users_root"
            type: "boolean"
            description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "parent_id"
            type: "string"
            description: ""
            foreign-key-id: "folder-id"

      - name: "hidden"
        type: "boolean"
        description: ""

      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "dashboard-id"

      - name: "model"
        type: "object"
        description: ""
        subattributes:
          - name: "id"
            type: "string"
            description: ""
            foreign-key-id: "model-id"

          - name: "label"
            type: "string"
            description: ""

      - name: "query_timezone"
        type: "string"
        description: ""

      - name: "readonly"
        type: "boolean"
        description: ""

      - name: "refresh_interval"
        type: "string"
        description: ""

      - name: "refresh_interval_to_i"
        type: "integer"
        description: ""

      - name: "space"
        type: "object"
        description: ""
        subattributes:
          - name: "child_count"
            type: "integer"
            description: ""

          - *content-metadata-id

          - *creator-id

          - name: "external_id"
            type: "string"
            description: ""

          - name: "id"
            type: "string"
            description: ""
            foreign-key-id: "space-id"

          - name: "is_embed"
            type: "boolean"
            description: ""

          - name: "is_embed_shared_root"
            type: "boolean"
            description: ""

          - name: "is_embed_users_root"
            type: "boolean"
            description: ""

          - name: "is_personal"
            type: "boolean"
            description: ""

          - name: "is_personal_descendant"
            type: "boolean"
            description: ""

          - name: "is_shared_root"
            type: "boolean"
            description: ""

          - name: "is_users_root"
            type: "boolean"
            description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "parent_id"
            type: "string"
            description: ""
            foreign-key-id: "space-id"

      - name: "title"
        type: "string"
        description: ""

      - name: "user_id"
        type: "string"
        description: ""
        foreign-key-id: "user-id"

  - name: "dashboard_id"
    type: "string"
    description: ""
    foreign-key-id: "dashboard-id"

  - name: "look"
    type: "object"
    description: ""
    subattributes:
      - *content-metadata-id

      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "look-id"

      - name: "title"
        type: "string"
        description: ""

  - name: "look_id"
    type: "string"
    description: ""
    foreign-key-id: "look-id"

  - name: "user_id"
    type: "string"
    description: ""
    foreign-key-id: "user-id"
---