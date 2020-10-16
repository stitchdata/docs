---
tap: "looker"
version: "1"
key: "space"

name: "spaces"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/spaces.json"
description: |
  The `{{ table.name }}` table contains info about the spaces in your {{ integration.display_name }} instance.

replication-method: "Full Table"

api-method:
  name: "Get all spaces"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/space#get_all_spaces"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The space ID."
    foreign-key-id: "space-id"

  - name: "child_count"
    type: "integer"
    description: ""

  - &content-metadata-id
    name: "content_metadata_id"
    type: "string"
    description: ""
    foreign-key-id: "content-metadata-id"

  - &creator-id
    name: "creator_id"
    type: "string"
    description: ""
    foreign-key-id: "user-id"

  - name: "dashboards"
    type: "array"
    description: ""
    subattributes:
      - &content-favorite-id
        name: "content_favorite_id"
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
        anchor-id: 1
        subattributes: &folder
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
        anchor-id: 1
        subattributes: &model
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
        anchor-id: 1
        subattributes: &space
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

  - name: "external_id"
    type: "string"
    description: ""

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

  - name: "looks"
    type: "array"
    description: ""
    subattributes:
      - *content-favorite-id

      - *content-metadata-id

      - name: "created_at"
        type: "date-time"
        description: ""

      - name: "dashboards"
        type: "array"
        description: ""
        anchor-id: 2
        subattributes:
          - *content-favorite-id

          - *content-metadata-id

          - name: "description"
            type: "string"
            description: ""

          - name: "folder"
            type: "object"
            description: ""
            anchor-id: 2
            subattributes: *folder

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
            anchor-id: 2
            subattributes: *model

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
            anchor-id: 2
            subattributes: *space

          - name: "title"
            type: "string"
            description: ""

          - name: "user_id"
            type: "string"
            description: ""
            foreign-key-id: "user-id"

      - name: "deleted"
        type: "boolean"
        description: ""

      - name: "deleted_at"
        type: "date-time"
        description: ""

      - name: "deleter_id"
        type: "string"
        description: ""
        foreign-key-id: "user-id"

      - name: "description"
        type: "string"
        description: ""

      - name: "embed_url"
        type: "string"
        description: ""

      - name: "excel_file_url"
        type: "string"
        description: ""

      - name: "favorite_count"
        type: "integer"
        description: ""

      - name: "folder"
        type: "object"
        description: ""
        anchor-id: 3
        subattributes: *folder

      - name: "folder_id"
        type: "string"
        description: ""

      - name: "google_spreadsheet_formula"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "look-id"

      - name: "image_embed_url"
        type: "string"
        description: ""

      - name: "is_run_on_load"
        type: "boolean"
        description: ""

      - name: "last_accessed_at"
        type: "date-time"
        description: ""

      - name: "last_updater_id"
        type: "string"
        description: ""

      - name: "last_viewed_at"
        type: "date-time"
        description: ""

      - name: "model"
        type: "object"
        description: ""
        anchor-id: 3
        subattributes: *model

      - name: "public"
        type: "boolean"
        description: ""

      - name: "public_slug"
        type: "string"
        description: ""

      - name: "public_url"
        type: "string"
        description: ""

      - name: "query_id"
        type: "string"
        description: ""
        foreign-key-id: "query-id"

      - name: "short_url"
        type: "string"
        description: ""

      - name: "space"
        type: "object"
        description: ""
        anchor-id: 3
        subattributes: *space

      - name: "space_id"
        type: "string"
        description: ""
        foreign-key-id: "space-id"

      - name: "title"
        type: "string"
        description: ""

      - name: "updated_at"
        type: "date-time"
        description: ""

      - name: "user"
        type: "object"
        description: ""
        subattributes:
          - name: "id"
            type: "string"
            description: ""
            foreign-key-id: "user-id"

      - name: "user_id"
        type: "string"
        description: ""
        foreign-key-id: "user-id"

      - name: "view_count"
        type: "integer"
        description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "parent_id"
    type: "string"
    description: ""
    foreign-key-id: "space-id"
---