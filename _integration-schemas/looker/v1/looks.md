---
tap: "looker"
version: "1"
key: "look"

name: "looks"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/looks.json"
description: |
  The `{{ table.name }}` table contains info about the looks in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get all looks"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/look#get_all_looks"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "look-id"

  - name: "content_favorite_id"
    type: "string"
    description: ""

  - name: "content_metadata_id"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

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
    subattributes:
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

  - name: "folder_id"
    type: "string"
    description: ""

  - name: "google_spreadsheet_formula"
    type: "string"
    description: ""

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
    foreign-key-id: "user-id"

  - name: "last_viewed_at"
    type: "date-time"
    description: ""

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
    subattributes:
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
---