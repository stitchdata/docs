---
tap: "looker"
version: "1"
key: "theme"

name: "themes"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/themes.json"
description: |
  The `{{ table.name }}` table contains info about the themes in your {{ integration.display_name }} instance.

replication-method: "Full Table"

api-method:
  name: "Get all themes"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/theme#get_all_themes"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The theme ID."
    # foreign-key-id: "theme-id"

  - name: "begin_at"
    type: "date-time"
    description: ""

  - name: "end_at"
    type: "date-time"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "settings"
    type: "object"
    description: ""
    subattributes:
      - name: "background_color"
        type: "string"
        description: ""

      - name: "base_font_size"
        type: "string"
        description: ""

      - name: "color_collection_id"
        type: "string"
        description: ""
        foreign-key-id: "color-collection-id"

      - name: "font_color"
        type: "string"
        description: ""

      - name: "font_family"
        type: "string"
        description: ""

      - name: "font_source"
        type: "string"
        description: ""

      - name: "info_button_color"
        type: "string"
        description: ""

      - name: "primary_button_color"
        type: "string"
        description: ""

      - name: "show_filters_bar"
        type: "boolean"
        description: ""

      - name: "show_title"
        type: "boolean"
        description: ""

      - name: "text_tile_text_color"
        type: "string"
        description: ""

      - name: "tile_background_color"
        type: "string"
        description: ""

      - name: "tile_text_color"
        type: "string"
        description: ""

      - name: "title_color"
        type: "string"
        description: ""

      - name: "warn_button_color"
        type: "string"
        description: ""
---