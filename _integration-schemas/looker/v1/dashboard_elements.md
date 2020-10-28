---
tap: "looker"
version: "1"
key: "dashboard-element"

name: "dashboard_elements"
doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/dashboard#get_all_dashboardelements"
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/dashboard_elements.json"
description: |
  The `{{ table.name }}` table contains information about all dashboard elements in your {{ integration.display_name }} instance.
  
replication-method: "Full Table"

api-method:
  name: "Get all dashboard elements"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/dashboard#get_all_dashboardelements"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The dashboard element ID."
    foreign-key-id: "dashboard-element-id"
    
  - name: "alert_count"
    type: "integer"
    description: ""

  - name: "body_text"
    type: "string"
    description: ""

  - name: "body_text_as_html"
    type: "string"
    description: ""

  - name: "dashboard_id"
    type: "string"
    description: ""
    foreign-key-id: "dashboard-id"

  - name: "edit_uri"
    type: "string"
    description: ""
  
  - name: "look"
    type: "object"
    description: ""
    subattributes:
      - name: "content_favorite_id"
        type: "string"
        description: ""
        foreign-key-id: "content-favorite-id"

      - &content-metadata-id
        name: "content_metadata_id"
        type: "string"
        description: ""
        foreign-key-id: "content-metadata-id"

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

          - *content-metadata-id

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

      - name: "folder_id"
        type: "string"
        description: ""
        foreign-key-id: "folder-id"

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

      - name: "query"
        type: "object"
        description: ""
        anchor-id: 1
        subattributes:
          - name: "client_id"
            type: "string"
            description: ""

          - name: "column_limit"
            type: "string"
            description: ""

          - name: "dynamic_fields"
            type: "string"
            description: ""

          - name: "expanded_share_url"
            type: "string"
            description: ""

          - name: "fields"
            type: "array"
            description: ""
            anchor-id: 1
            subattributes:
              - name: "value"
                type: "string"
                description: ""

          - name: "fill_fields"
            type: "array"
            description: ""
            anchor-id: 1
            subattributes:
              - name: "value"
                type: "string"
                description: ""

          - name: "filter_config"
            type: "object"
            description: ""

          - name: "filter_expression"
            type: "string"
            description: ""

          - name: "filters"
            type: "object"
            description: ""

          - name: "has_table_calculations"
            type: "boolean"
            description: ""

          - name: "id"
            type: "string"
            description: ""
            foreign-key-id: "query-id"

          - name: "limit"
            type: "string"
            description: ""

          - name: "model"
            type: "string"
            description: ""

          - name: "pivots"
            type: "array"
            description: ""
            anchor-id: 1
            subattributes:
              - name: "value"
                type: "string"
                description: ""

          - name: "query_timezone"
            type: "string"
            description: ""

          - name: "row_total"
            type: "string"
            description: ""

          - name: "runtime"
            type: "number"
            description: ""

          - name: "share_url"
            type: "string"
            description: ""

          - name: "slug"
            type: "string"
            description: ""

          - name: "sorts"
            type: "array"
            description: ""
            anchor-id: 1
            subattributes:
              - name: "value"
                type: "anything"
                description: ""

          - name: "subtotals"
            type: "array"
            description: ""
            anchor-id: 1
            subattributes:
              - name: "value"
                type: "string"
                description: ""

          - name: "total"
            type: "boolean"
            description: ""

          - name: "url"
            type: "string"
            description: ""

          - name: "view"
            type: "string"
            description: ""

          - name: "vis_config"
            type: "object"
            description: ""

          - name: "visible_ui_sections"
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

          - *content-metadata-id

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

      - name: "url"
        type: "string"
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

  - name: "look_id"
    type: "string"
    description: ""
    foreign-key-id: "look-id"

  - name: "lookml_link_id"
    type: "string"
    description: ""

  - name: "merge_result_id"
    type: "string"
    description: ""

  - name: "note_display"
    type: "string"
    description: ""

  - name: "note_state"
    type: "string"
    description: ""

  - name: "note_text"
    type: "string"
    description: ""

  - name: "note_text_as_html"
    type: "string"
    description: ""

  - name: "query"
    type: "object"
    description: ""
    anchor-id: 2
    subattributes:
      - name: "client_id"
        type: "string"
        description: ""

      - name: "column_limit"
        type: "string"
        description: ""

      - name: "dynamic_fields"
        type: "string"
        description: ""

      - name: "expanded_share_url"
        type: "string"
        description: ""

      - name: "fields"
        type: "array"
        description: ""
        anchor-id: 2
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "fill_fields"
        type: "array"
        description: ""
        anchor-id: 2
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "filter_config"
        type: "object"
        description: ""

      - name: "filter_expression"
        type: "string"
        description: ""

      - name: "filters"
        type: "object"
        description: ""

      - name: "has_table_calculations"
        type: "boolean"
        description: ""

      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "query-id"

      - name: "limit"
        type: "string"
        description: ""

      - name: "model"
        type: "string"
        description: ""

      - name: "pivots"
        type: "array"
        description: ""
        anchor-id: 2
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "query_timezone"
        type: "string"
        description: ""

      - name: "row_total"
        type: "string"
        description: ""

      - name: "runtime"
        type: "number"
        description: ""

      - name: "share_url"
        type: "string"
        description: ""

      - name: "slug"
        type: "string"
        description: ""

      - name: "sorts"
        type: "array"
        description: ""
        anchor-id: 2
        subattributes:
          - name: "value"
            type: "anything"
            description: ""

      - name: "subtotals"
        type: "array"
        description: ""
        anchor-id: 2
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "total"
        type: "boolean"
        description: ""

      - name: "url"
        type: "string"
        description: ""

      - name: "view"
        type: "string"
        description: ""

      - name: "vis_config"
        type: "object"
        description: ""

      - name: "visible_ui_sections"
        type: "string"
        description: ""

  - name: "query_id"
    type: "string"
    description: ""
    foreign-key-id: "query-id"

  - name: "refresh_interval"
    type: "string"
    description: ""

  - name: "refresh_interval_to_i"
    type: "integer"
    description: ""

  - name: "result_maker"
    type: "object"
    description: ""
    subattributes:
      - name: "dynamic_fields"
        type: "string"
        description: ""

      - name: "filterables"
        type: "array"
        description: ""
        subattributes:
          - name: "listen"
            type: "array"
            description: ""
            subattributes:
              - name: "dashboard_filter_name"
                type: "string"
                description: ""

              - name: "field"
                type: "string"
                description: ""

          - name: "model"
            type: "string"
            description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "view"
            type: "string"
            description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "merge_result_id"
        type: "string"
        description: ""

      - name: "query"
        type: "object"
        description: ""
        anchor-id: 3
        subattributes:
          - name: "client_id"
            type: "string"
            description: ""

          - name: "column_limit"
            type: "string"
            description: ""

          - name: "dynamic_fields"
            type: "string"
            description: ""

          - name: "expanded_share_url"
            type: "string"
            description: ""

          - name: "fields"
            type: "array"
            description: ""
            anchor-id: 3
            subattributes:
              - name: "value"
                type: "string"
                description: ""

          - name: "fill_fields"
            type: "array"
            description: ""
            anchor-id: 3
            subattributes:
              - name: "value"
                type: "string"
                description: ""

          - name: "filter_config"
            type: "object"
            description: ""

          - name: "filter_expression"
            type: "string"
            description: ""

          - name: "filters"
            type: "object"
            description: ""

          - name: "has_table_calculations"
            type: "boolean"
            description: ""

          - name: "id"
            type: "string"
            description: ""
            foreign-key-id: "query-id"

          - name: "limit"
            type: "string"
            description: ""

          - name: "model"
            type: "string"
            description: ""

          - name: "pivots"
            type: "array"
            description: ""
            anchor-id: 3
            subattributes:
              - name: "value"
                type: "string"
                description: ""

          - name: "query_timezone"
            type: "string"
            description: ""

          - name: "row_total"
            type: "string"
            description: ""

          - name: "runtime"
            type: "number"
            description: ""

          - name: "share_url"
            type: "string"
            description: ""

          - name: "slug"
            type: "string"
            description: ""

          - name: "sorts"
            type: "array"
            description: ""
            anchor-id: 3
            subattributes:
              - name: "value"
                type: "anything"
                description: ""

          - name: "subtotals"
            type: "array"
            description: ""
            anchor-id: 3
            subattributes:
              - name: "value"
                type: "string"
                description: ""

          - name: "total"
            type: "boolean"
            description: ""

          - name: "url"
            type: "string"
            description: ""

          - name: "view"
            type: "string"
            description: ""

          - name: "vis_config"
            type: "object"
            description: ""

          - name: "visible_ui_sections"
            type: "string"
            description: ""

      - name: "query_id"
        type: "string"
        description: ""
        foreign-key-id: "query-id"

      - name: "sorts"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "anything"
            description: ""

      - name: "total"
        type: "boolean"
        description: ""

      - name: "vis_config"
        type: "object"
        description: ""

  - name: "result_maker_id"
    type: "string"
    description: ""

  - name: "subtitle_text"
    type: "string"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "title_hidden"
    type: "boolean"
    description: ""

  - name: "title_text"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""
---