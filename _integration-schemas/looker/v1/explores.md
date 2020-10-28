---
tap: "looker"
version: "1"
key: ""

name: "explores"
doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/lookml-model#get_lookml_model_explore"
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/explores.json"
description: |
  The `{{ table.name }}` table contains information about LookML model explores in your {{ integration.display_name }} instance.
  
replication-method: "Full Table"

api-method:
    name: "Get LookML Model Explore"
    doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/lookml-model#get_lookml_model_explore"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The explore ID."
    # foreign-key-id: "explore-id"

  - name: "access_filter_fields"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "access_filters"
    type: "array"
    description: ""
    subattributes:
      - name: "field"
        type: "string"
        description: ""

      - name: "user_attribute"
        type: "string"
        description: ""

  - name: "aliases"
    type: "array"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "always_filter"
    type: "array"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "can_explain"
    type: "boolean"
    description: ""

  - name: "can_pivot_in_db"
    type: "boolean"
    description: ""

  - name: "can_save"
    type: "boolean"
    description: ""

  - name: "can_subtotal"
    type: "boolean"
    description: ""

  - name: "can_total"
    type: "boolean"
    description: ""

  - name: "conditionally_filter"
    type: "array"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "connection_name"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "errors"
    type: "array"
    description: ""
    subattributes:
      - name: "details"
        type: "any"
        description: ""

      - name: "error_pos"
        type: "string"
        description: ""

      - name: "field_error"
        type: "boolean"
        description: ""

      - name: "message"
        type: "string"
        description: ""

  - name: "fields"
    type: "object"
    description: ""
    subattributes:
      - name: "dimensions"
        type: "array"
        description: ""
        subattributes:
          - name: "align"
            type: "string"
            description: ""

          - name: "can_filter"
            type: "boolean"
            description: ""

          - name: "can_time_filter"
            type: "boolean"
            description: ""

          - name: "category"
            type: "string"
            description: ""

          - name: "default_filter_value"
            type: "string"
            description: ""

          - name: "description"
            type: "string"
            description: ""

          - name: "dynamic"
            type: "boolean"
            description: ""

          - name: "enumerations"
            type: "array"
            description: ""
            anchor-id: 1
            subattributes: &enumerations
              - name: "label"
                type: "string"
                description: ""

              - name: "value"
                type: "string"
                description: ""

          - name: "error"
            type: "string"
            description: ""

          - name: "field_group_label"
            type: "string"
            description: ""

          - name: "field_group_variant"
            type: "string"
            description: ""

          - name: "fill_style"
            type: "string"
            description: ""

          - name: "fiscal_month_offset"
            type: "integer"
            description: ""

          - name: "has_allowed_values"
            type: "boolean"
            description: ""

          - name: "hidden"
            type: "boolean"
            description: ""

          - name: "is_filter"
            type: "boolean"
            description: ""

          - name: "is_fiscal"
            type: "boolean"
            description: ""

          - name: "is_numeric"
            type: "boolean"
            description: ""

          - name: "is_timeframe"
            type: "boolean"
            description: ""

          - name: "label"
            type: "string"
            description: ""

          - name: "label_from_parameter"
            type: "string"
            description: ""

          - name: "label_short"
            type: "string"
            description: ""

          - name: "lookml_link"
            type: "string"
            description: ""

          - name: "map_layer"
            type: "object"
            description: ""
            anchor-id: 1
            subattributes: &map-layer
              - name: "extents_json_url"
                type: "string"
                description: ""

              - name: "feature_key"
                type: "string"
                description: ""

              - name: "format"
                type: "string"
                description: ""

              - name: "max_zoom_level"
                type: "integer"
                description: ""

              - name: "min_zoom_level"
                type: "integer"
                description: ""

              - name: "name"
                type: "string"
                description: ""

              - name: "projection"
                type: "string"
                description: ""

              - name: "property_key"
                type: "string"
                description: ""

              - name: "property_label_key"
                type: "string"
                description: ""

              - name: "url"
                type: "string"
                description: ""

          - name: "measure"
            type: "boolean"
            description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "parameter"
            type: "boolean"
            description: ""

          - name: "permanent"
            type: "boolean"
            description: ""

          - name: "primary_key"
            type: "boolean"
            description: ""

          - name: "project_name"
            type: "string"
            description: ""

          - name: "requires_refresh_on_sort"
            type: "boolean"
            description: ""

          - name: "scope"
            type: "string"
            description: ""

          - name: "sortable"
            type: "boolean"
            description: ""

          - name: "source_file"
            type: "string"
            description: ""

          - name: "source_file_path"
            type: "string"
            description: ""

          - name: "sql"
            type: "string"
            description: ""

          - name: "sql_case"
            type: "array"
            description: ""
            anchor-id: 1
            subattributes: &sql-case
              - name: "condition"
                type: "string"
                description: ""

              - name: "value"
                type: "string"
                description: ""

          - name: "strict_value_format"
            type: "boolean"
            description: ""

          - name: "suggest_dimension"
            type: "string"
            description: ""

          - name: "suggest_explore"
            type: "string"
            description: ""

          - name: "suggestable"
            type: "boolean"
            description: ""

          - name: "suggestions"
            type: "array"
            description: ""
            anchor-id: 1
            subattributes: &suggestions
              - name: "value"
                type: "string"
                description: ""

          - name: "tags"
            type: "array"
            description: ""
            anchor-id: 1
            subattributes: &tags
              - name: "value"
                type: "string"
                description: ""

          - name: "time_interval"
            type: "object"
            description: ""
            anchor-id: 1
            subattributes: &time-interval
              - name: "count"
                type: "string"
                description: ""

              - name: "name"
                type: "string"
                description: ""

          - name: "type"
            type: "string"
            description: ""

          - name: "user_attribute_filter_types"
            type: "array"
            description: ""
            anchor-id: 1
            subattributes: &user-attribute-filter-type
              - name: "value"
                type: "string"
                description: ""

          - name: "value_format"
            type: "string"
            description: ""

          - name: "view"
            type: "string"
            description: ""

          - name: "view_label"
            type: "string"
            description: ""

          - name: "week_start_day"
            type: "string"
            description: ""

      - name: "filters"
        type: "array"
        description: ""
        subattributes:
          - name: "align"
            type: "string"
            description: ""

          - name: "can_filter"
            type: "boolean"
            description: ""

          - name: "can_time_filter"
            type: "boolean"
            description: ""

          - name: "category"
            type: "string"
            description: ""

          - name: "default_filter_value"
            type: "string"
            description: ""

          - name: "description"
            type: "string"
            description: ""

          - name: "dynamic"
            type: "boolean"
            description: ""

          - name: "enumerations"
            type: "array"
            description: ""
            anchor-id: 2
            subattributes: *enumerations

          - name: "error"
            type: "string"
            description: ""

          - name: "field_group_label"
            type: "string"
            description: ""

          - name: "field_group_variant"
            type: "string"
            description: ""

          - name: "fill_style"
            type: "string"
            description: ""

          - name: "fiscal_month_offset"
            type: "integer"
            description: ""

          - name: "has_allowed_values"
            type: "boolean"
            description: ""

          - name: "hidden"
            type: "boolean"
            description: ""

          - name: "is_filter"
            type: "boolean"
            description: ""

          - name: "is_fiscal"
            type: "boolean"
            description: ""

          - name: "is_numeric"
            type: "boolean"
            description: ""

          - name: "is_timeframe"
            type: "boolean"
            description: ""

          - name: "label"
            type: "string"
            description: ""

          - name: "label_from_parameter"
            type: "string"
            description: ""

          - name: "label_short"
            type: "string"
            description: ""

          - name: "lookml_link"
            type: "string"
            description: ""

          - name: "map_layer"
            type: "object"
            description: ""
            anchor-id: 2
            subattributes: *anchor-id

          - name: "measure"
            type: "boolean"
            description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "parameter"
            type: "boolean"
            description: ""

          - name: "permanent"
            type: "boolean"
            description: ""

          - name: "primary_key"
            type: "boolean"
            description: ""

          - name: "project_name"
            type: "string"
            description: ""

          - name: "requires_refresh_on_sort"
            type: "boolean"
            description: ""

          - name: "scope"
            type: "string"
            description: ""

          - name: "sortable"
            type: "boolean"
            description: ""

          - name: "source_file"
            type: "string"
            description: ""

          - name: "source_file_path"
            type: "string"
            description: ""

          - name: "sql"
            type: "string"
            description: ""

          - name: "sql_case"
            type: "array"
            description: ""
            anchor-id: 2
            subattributes: *sql-case

          - name: "strict_value_format"
            type: "boolean"
            description: ""

          - name: "suggest_dimension"
            type: "string"
            description: ""

          - name: "suggest_explore"
            type: "string"
            description: ""

          - name: "suggestable"
            type: "boolean"
            description: ""

          - name: "suggestions"
            type: "array"
            description: ""
            anchor-id: 2
            subattributes: *suggestions

          - name: "tags"
            type: "array"
            description: ""
            anchor-id: 2
            subattributes: *tags

          - name: "time_interval"
            type: "object"
            description: ""
            anchor-id: 2
            subattributes: *time-interval

          - name: "type"
            type: "string"
            description: ""

          - name: "user_attribute_filter_types"
            type: "array"
            description: ""
            anchor-id: 2
            subattributes: *user-attribute-filter-type

          - name: "value_format"
            type: "string"
            description: ""

          - name: "view"
            type: "string"
            description: ""

          - name: "view_label"
            type: "string"
            description: ""

          - name: "week_start_day"
            type: "string"
            description: ""

      - name: "measures"
        type: "array"
        description: ""
        subattributes:
          - name: "align"
            type: "string"
            description: ""

          - name: "can_filter"
            type: "boolean"
            description: ""

          - name: "can_time_filter"
            type: "boolean"
            description: ""

          - name: "category"
            type: "string"
            description: ""

          - name: "default_filter_value"
            type: "string"
            description: ""

          - name: "description"
            type: "string"
            description: ""

          - name: "dynamic"
            type: "boolean"
            description: ""

          - name: "enumerations"
            type: "array"
            description: ""
            anchor-id: 3
            subattributes: *enumerations

          - name: "error"
            type: "string"
            description: ""

          - name: "field_group_label"
            type: "string"
            description: ""

          - name: "field_group_variant"
            type: "string"
            description: ""

          - name: "fill_style"
            type: "string"
            description: ""

          - name: "fiscal_month_offset"
            type: "integer"
            description: ""

          - name: "has_allowed_values"
            type: "boolean"
            description: ""

          - name: "hidden"
            type: "boolean"
            description: ""

          - name: "is_filter"
            type: "boolean"
            description: ""

          - name: "is_fiscal"
            type: "boolean"
            description: ""

          - name: "is_numeric"
            type: "boolean"
            description: ""

          - name: "is_timeframe"
            type: "boolean"
            description: ""

          - name: "label"
            type: "string"
            description: ""

          - name: "label_from_parameter"
            type: "string"
            description: ""

          - name: "label_short"
            type: "string"
            description: ""

          - name: "lookml_link"
            type: "string"
            description: ""

          - name: "map_layer"
            type: "object"
            description: ""
            anchor-id: 3
            subattributes: *anchor-id

          - name: "measure"
            type: "boolean"
            description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "parameter"
            type: "boolean"
            description: ""

          - name: "permanent"
            type: "boolean"
            description: ""

          - name: "primary_key"
            type: "boolean"
            description: ""

          - name: "project_name"
            type: "string"
            description: ""

          - name: "requires_refresh_on_sort"
            type: "boolean"
            description: ""

          - name: "scope"
            type: "string"
            description: ""

          - name: "sortable"
            type: "boolean"
            description: ""

          - name: "source_file"
            type: "string"
            description: ""

          - name: "source_file_path"
            type: "string"
            description: ""

          - name: "sql"
            type: "string"
            description: ""

          - name: "sql_case"
            type: "array"
            description: ""
            anchor-id: 3
            subattributes: *sql-case

          - name: "strict_value_format"
            type: "boolean"
            description: ""

          - name: "suggest_dimension"
            type: "string"
            description: ""

          - name: "suggest_explore"
            type: "string"
            description: ""

          - name: "suggestable"
            type: "boolean"
            description: ""

          - name: "suggestions"
            type: "array"
            description: ""
            anchor-id: 3
            subattributes: *suggestions

          - name: "tags"
            type: "array"
            description: ""
            anchor-id: 3
            subattributes: *tags

          - name: "time_interval"
            type: "object"
            description: ""
            anchor-id: 3
            subattributes: *time-interval

          - name: "type"
            type: "string"
            description: ""

          - name: "user_attribute_filter_types"
            type: "array"
            description: ""
            anchor-id: 3
            subattributes: *user-attribute-filter-type

          - name: "value_format"
            type: "string"
            description: ""

          - name: "view"
            type: "string"
            description: ""

          - name: "view_label"
            type: "string"
            description: ""

          - name: "week_start_day"
            type: "string"
            description: ""

      - name: "parameters"
        type: "array"
        description: ""
        subattributes:
          - name: "align"
            type: "string"
            description: ""

          - name: "can_filter"
            type: "boolean"
            description: ""

          - name: "can_time_filter"
            type: "boolean"
            description: ""

          - name: "category"
            type: "string"
            description: ""

          - name: "default_filter_value"
            type: "string"
            description: ""

          - name: "description"
            type: "string"
            description: ""

          - name: "dynamic"
            type: "boolean"
            description: ""

          - name: "enumerations"
            type: "array"
            description: ""
            anchor-id: 4
            subattributes: *enumerations

          - name: "error"
            type: "string"
            description: ""

          - name: "field_group_label"
            type: "string"
            description: ""

          - name: "field_group_variant"
            type: "string"
            description: ""

          - name: "fill_style"
            type: "string"
            description: ""

          - name: "fiscal_month_offset"
            type: "integer"
            description: ""

          - name: "has_allowed_values"
            type: "boolean"
            description: ""

          - name: "hidden"
            type: "boolean"
            description: ""

          - name: "is_filter"
            type: "boolean"
            description: ""

          - name: "is_fiscal"
            type: "boolean"
            description: ""

          - name: "is_numeric"
            type: "boolean"
            description: ""

          - name: "is_timeframe"
            type: "boolean"
            description: ""

          - name: "label"
            type: "string"
            description: ""

          - name: "label_from_parameter"
            type: "string"
            description: ""

          - name: "label_short"
            type: "string"
            description: ""

          - name: "lookml_link"
            type: "string"
            description: ""

          - name: "map_layer"
            type: "object"
            description: ""
            anchor-id: 4
            subattributes: *anchor-id

          - name: "measure"
            type: "boolean"
            description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "parameter"
            type: "boolean"
            description: ""

          - name: "permanent"
            type: "boolean"
            description: ""

          - name: "primary_key"
            type: "boolean"
            description: ""

          - name: "project_name"
            type: "string"
            description: ""

          - name: "requires_refresh_on_sort"
            type: "boolean"
            description: ""

          - name: "scope"
            type: "string"
            description: ""

          - name: "sortable"
            type: "boolean"
            description: ""

          - name: "source_file"
            type: "string"
            description: ""

          - name: "source_file_path"
            type: "string"
            description: ""

          - name: "sql"
            type: "string"
            description: ""

          - name: "sql_case"
            type: "array"
            description: ""
            anchor-id: 4
            subattributes: *sql-case

          - name: "strict_value_format"
            type: "boolean"
            description: ""

          - name: "suggest_dimension"
            type: "string"
            description: ""

          - name: "suggest_explore"
            type: "string"
            description: ""

          - name: "suggestable"
            type: "boolean"
            description: ""

          - name: "suggestions"
            type: "array"
            description: ""
            anchor-id: 4
            subattributes: *suggestions

          - name: "tags"
            type: "array"
            description: ""
            anchor-id: 4
            subattributes: *tags

          - name: "time_interval"
            type: "object"
            description: ""
            anchor-id: 4
            subattributes: *time-interval

          - name: "type"
            type: "string"
            description: ""

          - name: "user_attribute_filter_types"
            type: "array"
            description: ""
            anchor-id: 4
            subattributes: *user-attribute-filter-type

          - name: "value_format"
            type: "string"
            description: ""

          - name: "view"
            type: "string"
            description: ""

          - name: "view_label"
            type: "string"
            description: ""

          - name: "week_start_day"
            type: "string"
            description: ""

  - name: "files"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "group_label"
    type: "string"
    description: ""

  - name: "has_timezone_support"
    type: "boolean"
    description: ""

  - name: "hidden"
    type: "boolean"
    description: ""
  
  - name: "index_fields"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "joins"
    type: "array"
    description: ""
    subattributes:
      - name: "dependent_fields"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "fields"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "foreign_key"
        type: "string"
        description: ""

      - name: "from"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "outer_only"
        type: "boolean"
        description: ""

      - name: "relationship"
        type: "string"
        description: ""

      - name: "required_joins"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "sql_foreign_key"
        type: "string"
        description: ""

      - name: "sql_on"
        type: "string"
        description: ""

      - name: "sql_table_name"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "view_label"
        type: "string"
        description: ""

  - name: "label"
    type: "string"
    description: ""

  - name: "model_name"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "null_sort_treatment"
    type: "string"
    description: ""

  - name: "project_name"
    type: "string"
    description: ""

  - name: "scopes"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "sets"
    type: "array"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

  - name: "source_file"
    type: "string"
    description: ""

  - name: "sql_table_name"
    type: "string"
    description: ""

  - name: "supported_measure_types"
    type: "array"
    description: ""
    subattributes:
      - name: "dimension_type"
        type: "string"
        description: ""

      - name: "measure_types"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

  - name: "supports_cost_estimate"
    type: "boolean"
    description: ""

  - name: "tags"
    type: "array"
    description: ""
    anchor-id: 5
    subattributes: *tags

  - name: "view_name"
    type: "string"
    description: ""
---