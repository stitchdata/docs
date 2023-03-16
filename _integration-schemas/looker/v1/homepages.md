---
tap: "looker"
version: "1"
key: "homepage"

name: "homepages"
doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/homepage#get_all_homepages"
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/homepages.json"
description: |
  The `{{ table.name }}` table contains information about all homepages in your {{ integration.display_name }} instance.
  
replication-method: "Full Table"

api-method:
  name: "Get all homepages"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/homepage#get_all_homepages"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The homepage ID."
    foreign-key-id: "homepage-id"

  - &content-metadata-id
    name: "content_metadata_id"
    type: "string"
    description: ""
    foreign-key-id: "content-metadata-id"

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "deleted_at"
    type: "date-time"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "homepage_sections"
    type: "array"
    description: ""
    subattributes:
      - name: "created_at"
        type: "date-time"
        description: ""

      - name: "deleted_at"
        type: "date-time"
        description: ""

      - name: "description"
        type: "string"
        description: ""

      - name: "detail_url"
        type: "string"
        description: ""

      - name: "homepage_id"
        type: "string"
        description: ""
        foreign-key-id: "homepage-id"

      - name: "homepage_items"
        type: "array"
        description: ""
        subattributes:
          - name: "content_created_by"
            type: "string"
            description: ""
            foreign-key-id: "user-id"

          - name: "content_favorite_id"
            type: "string"
            description: ""
            foreign-key-id: "content-favorite-id"

          - *content-metadata-id

          - name: "content_updated_at"
            type: "string"
            description: ""

          - name: "custom_description"
            type: "string"
            description: ""

          - name: "custom_image_data_base64"
            type: "string"
            description: ""

          - name: "custom_image_url"
            type: "string"
            description: ""

          - name: "custom_title"
            type: "string"
            description: ""

          - name: "custom_url"
            type: "string"
            description: ""

          - name: "dashboard_id"
            type: "string"
            description: ""
            foreign-key-id: "dashboard-id"

          - name: "description"
            type: "string"
            description: ""

          - name: "favorite_count"
            type: "integer"
            description: ""

          - name: "homepage_section_id"
            type: "string"
            description: ""

          - name: "id"
            type: "string"
            description: ""

          - name: "image_url"
            type: "string"
            description: ""

          - name: "location"
            type: "string"
            description: ""

          - name: "look_id"
            type: "string"
            description: ""
            foreign-key-id: "look-id"

          - name: "lookml_dashboard_id"
            type: "string"
            description: ""
            foreign-key-id: "lookml-dashboard-id"

          - name: "order"
            type: "integer"
            description: ""

          - name: "section_fetch_time"
            type: "number"
            description: ""

          - name: "title"
            type: "string"
            description: ""

          - name: "url"
            type: "string"
            description: ""

          - name: "use_custom_description"
            type: "boolean"
            description: ""

          - name: "use_custom_image"
            type: "boolean"
            description: ""

          - name: "use_custom_title"
            type: "boolean"
            description: ""

          - name: "use_custom_url"
            type: "boolean"
            description: ""

          - name: "view_count"
            type: "integer"
            description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "is_header"
        type: "boolean"
        description: ""

      - name: "item_order"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "integer"
            description: ""

      - name: "title"
        type: "string"
        description: ""

      - name: "updated_at"
        type: "date-time"
        description: ""
  
  - name: "primary_homepage"
    type: "boolean"
    description: ""

  - name: "section_order"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "integer"
        description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "updated_at"
    type: "date-time"
    description: ""

  - name: "user_id"
    type: "string"
    description: ""
    foreign-key-id: "user-id"
---