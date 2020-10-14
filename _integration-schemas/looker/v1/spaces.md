---
tap: "looker"
version: "1"
key: "space"

name: "spaces"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/spaces.json"
description: |
  The `{{ table.name }}` table contains info about the spaces in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get all spaces"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/space#get_all_spaces"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "space-id"

  - name: "child_count"
    type: "integer"
    description: ""

  - name: "content_metadata_id"
    type: "string"
    description: ""

  - name: "creator_id"
    type: "string"
    description: ""
    foreign-key-id: "user-id"

  - name: "dashboards"
    type: "array"
    description: ""
    subattributes: &dashboard
      - name: "content_favorite_id"
        type: "string"
        description: ""

      - name: "content_metadata_id"
        type: "string"
        description: ""

      - name: "description"
        type: "string"
        description: ""

      - name: "folder"
        type: "object"
        description: ""
        subattributes: &folder
          - name: "child_count"
            type: "integer"
            description: ""

          - name: "content_metadata_id"
            type: "string"
            description: ""

          - name: "creator_id"
            type: "string"
            description: ""

          - name: "external_id"
            type: "string"
            description: ""

          - name: "id"
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

          - name: "name"
            type: "string"
            description: ""

          - name: "parent_id"
            type: "string"
            description: ""

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
        subattributes: &space
          - name: "child_count"
            type: "integer"
            description: ""

          - name: "content_metadata_id"
            type: "string"
            description: ""

          - name: "creator_id"
            type: "string"
            description: ""
            foreign-key-id: "user-id"

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
      - name: "content_favorite_id"
        type: "string"
        description: ""

      - name: "content_metadata_id"
        type: "string"
        description: ""

      - name: "created_at"
        type: "date-time"
        description: ""

        ## this might need a level id
      - name: "dashboards"
        type: "array"
        description: ""
        subattributes: *dashboards

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

## level id
      - name: "folder"
        type: "object"
        description: ""
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
## level id
      - name: "model"
        type: "object"
        description: ""
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