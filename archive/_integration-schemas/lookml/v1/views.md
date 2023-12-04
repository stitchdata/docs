---
tap: "lookml"
version: "1"
key: "view"

name: "views"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-lookml/blob/master/tap_lookml/schemas/views.json"
description: |
  The `{{ table.name }}` table contains information about the view file parse items in your GitHub account using the `lkml` filter.

replication-method: "Full Table"

api-method:
  name: "Git API Search"
  doc-link: "https://docs.github.com/en/rest/reference/search#search-code"

attributes:
  - name: "git_owner"
    type: "string"
    primary-key: true
    description: "The GitHub repository owner."
  
  - name: "git_repository"
    type: "string"
    primary-key: true
    description: "The GitHub repository."

  - name: "path"
    type: "string"
    primary-key: true
    description: "The URL for the repository."

  - name: "last_modified"
    type: "date-time"
    replication-key: true
    description: ""
  
  - name: "name"
    type: "string"
    description: "The name of the repository."

  - name: "derived_table"
    type: "object"
    description: ""
    subattributes:
      - name: "cluster_keys"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "create_process"
        type: "object"
        description: ""
        subattributes:
          - name: "sql_steps"
            type: "array"
            description: ""

            subattributes:
              - name: "value"
                type: "string"
                description: ""

      - name: "datagroup_trigger"
        type: "string"
        description: ""

      - name: "distribution"
        type: "string"
        description: ""

      - name: "distribution_style"
        type: "string"
        description: ""

      - name: "explore_source"
        type: "object"
        description: ""
        subattributes:
          - name: "bind_filters"
            type: "object"
            description: ""
            subattributes:
              - name: "from_field"
                type: "string"
                description: ""

              - name: "to_field"
                type: "string"
                description: ""

          - name: "columns"
            type: "array"
            description: ""
            subattributes:
              - name: "field"
                type: "string"
                description: ""

              - name: "name"
                type: "string"
                description: ""

          - name: "derived_columns"
            type: "array"
            description: ""
            subattributes:
              - name: "name"
                type: "string"
                description: ""

              - name: "sql"
                type: "string"
                description: ""

          - name: "expression_custom_filter"
            type: "string"
            description: ""

          - name: "filters"
            type: "array"
            description: ""
            subattributes:
              - name: "field"
                type: "string"
                description: ""

              - name: "value"
                type: "string"
                description: ""

          - name: "limit"
            type: "string"
            description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "sort"
            type: "object"
            description: ""
            subattributes:
              - name: "desc"
                type: "string"
                description: ""

              - name: "field"
                type: "string"
                description: ""

          - name: "timezone"
            type: "string"
            description: ""

      - name: "indexes"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "partition_keys"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "persist_for"
        type: "string"
        description: ""

      - name: "sortkeys"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "sql"
        type: "string"
        description: ""

      - name: "sql_create"
        type: "string"
        description: ""

      - name: "sql_trigger_value"
        type: "string"
        description: ""

  - name: "dimension_groups"
    type: "array"
    description: ""
    subattributes:
      - name: "alias"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "allow_fill"
        type: "string"
        description: ""

      - name: "bypass_suggest_restrictions"
        type: "string"
        description: ""

      - name: "can_filter"
        type: "string"
        description: ""

      - name: "convert_tz"
        type: "string"
        description: ""

      - name: "datatype"
        type: "string"
        description: ""

      - name: "description"
        type: "string"
        description: ""

      - name: "drill_fields"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "fanout_on"
        type: "string"
        description: ""

      - name: "full_suggestions"
        type: "string"
        description: ""

      - name: "group_item_label"
        type: "string"
        description: ""

      - name: "group_label"
        type: "string"
        description: ""

      - name: "hidden"
        type: "string"
        description: ""

      - name: "html"
        type: "string"
        description: ""

      - name: "intervals"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "label"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "order_by_field"
        type: "string"
        description: ""

      - name: "required_access_grants"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "skip_drill_filter"
        type: "string"
        description: ""

      - name: "sql"
        type: "string"
        description: ""

      - name: "sql_end"
        type: "string"
        description: ""

      - name: "sql_start"
        type: "string"
        description: ""

      - name: "suggest_dimension"
        type: "string"
        description: ""

      - name: "suggest_explore"
        type: "string"
        description: ""

      - name: "suggestable"
        type: "string"
        description: ""

      - name: "tags"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "timeframes"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "view_label"
        type: "string"
        description: ""

  - name: "dimensions"
    type: "array"
    description: ""
    subattributes:
      - name: "actions"
        type: "array"
        description: ""
        subattributes:
          - name: "form_params"
            type: "array"
            description: ""
            subattributes:
              - name: "default"
                type: "string"
                description: ""

              - name: "label"
                type: "string"
                description: ""

              - name: "name"
                type: "string"
                description: ""

              - name: "options"
                type: "array"
                description: ""
                subattributes:
                  - name: "label"
                    type: "string"
                    description: ""

                  - name: "name"
                    type: "string"
                    description: ""

              - name: "required"
                type: "string"
                description: ""

              - name: "type"
                type: "string"
                description: ""

          - name: "form_url"
            type: "string"
            description: ""

          - name: "icon_url"
            type: "string"
            description: ""

          - name: "label"
            type: "string"
            description: ""

          - name: "params"
            type: "array"
            description: ""
            subattributes:
              - name: "name"
                type: "string"
                description: ""

              - name: "value"
                type: "string"
                description: ""

          - name: "url"
            type: "string"
            description: ""

          - name: "user_attribute_params"
            type: "array"
            description: ""
            subattributes:
              - name: "name"
                type: "string"
                description: ""

              - name: "user_attribute"
                type: "string"
                description: ""

      - name: "alias"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "alpha_sort"
        type: "string"
        description: ""

      - name: "bypass_suggest_restrictions"
        type: "string"
        description: ""

      - name: "can_filter"
        type: "string"
        description: ""

      - name: "case"
        type: "object"
        description: ""
        subattributes:
          - name: "whens"
            type: "array"
            description: ""

            subattributes:
              - name: "label"
                type: "string"
                description: ""

              - name: "sql"
                type: "string"
                description: ""

      - name: "case_sensitive"
        type: "string"
        description: ""

      - name: "convert_tz"
        type: "string"
        description: ""

      - name: "datatype"
        type: "string"
        description: ""

      - name: "description"
        type: "string"
        description: ""

      - name: "drill_fields"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "fanout_on"
        type: "string"
        description: ""

      - name: "full_suggestions"
        type: "string"
        description: ""

      - name: "group_item_label"
        type: "string"
        description: ""

      - name: "group_label"
        type: "string"
        description: ""

      - name: "hidden"
        type: "string"
        description: ""

      - name: "html"
        type: "string"
        description: ""

      - name: "label"
        type: "string"
        description: ""

      - name: "label_from_parameter"
        type: "string"
        description: ""

      - name: "links"
        type: "array"
        description: ""
        subattributes:
          - name: "icon_url"
            type: "string"
            description: ""

          - name: "label"
            type: "string"
            description: ""

          - name: "url"
            type: "string"
            description: ""

      - name: "map_layer_name"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "order_by_field"
        type: "string"
        description: ""

      - name: "primary_key"
        type: "string"
        description: ""

      - name: "required_access_grants"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "required_fields"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "skip_drill_filter"
        type: "string"
        description: ""

      - name: "sql"
        type: "string"
        description: ""

      - name: "sql_end"
        type: "string"
        description: ""

      - name: "sql_latitude"
        type: "string"
        description: ""

      - name: "sql_longitude"
        type: "string"
        description: ""

      - name: "sql_start"
        type: "string"
        description: ""

      - name: "style"
        type: "string"
        description: ""

      - name: "suggest_dimension"
        type: "string"
        description: ""

      - name: "suggest_explore"
        type: "string"
        description: ""

      - name: "suggest_persist_for"
        type: "string"
        description: ""

      - name: "suggestable"
        type: "string"
        description: ""

      - name: "suggestions"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "tags"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "tiers"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "value_format"
        type: "string"
        description: ""

      - name: "value_format_name"
        type: "string"
        description: ""

      - name: "view_label"
        type: "string"
        description: ""

  - name: "extends"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "extension"
    type: "string"
    description: ""

  - name: "filters"
    type: "array"
    description: ""
    subattributes:
      - name: "alias"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "bypass_suggest_restrictions"
        type: "string"
        description: ""

      - name: "case_sensitive"
        type: "string"
        description: ""

      - name: "convert_tz"
        type: "string"
        description: ""

      - name: "datatype"
        type: "string"
        description: ""

      - name: "default_value"
        type: "string"
        description: ""

      - name: "description"
        type: "string"
        description: ""

      - name: "full_suggestions"
        type: "string"
        description: ""

      - name: "group_item_label"
        type: "string"
        description: ""

      - name: "group_label"
        type: "string"
        description: ""

      - name: "hidden"
        type: "string"
        description: ""

      - name: "label"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "required_access_grants"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "required_fields"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "sql"
        type: "string"
        description: ""

      - name: "suggest_dimension"
        type: "string"
        description: ""

      - name: "suggest_explore"
        type: "string"
        description: ""

      - name: "suggest_persist_for"
        type: "string"
        description: ""

      - name: "suggestable"
        type: "string"
        description: ""

      - name: "suggestions"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "tags"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "view_label"
        type: "string"
        description: ""

  - name: "measures"
    type: "array"
    description: ""
    subattributes:
      - name: "actions"
        type: "array"
        description: ""
        subattributes:
          - name: "form_params"
            type: "array"
            description: ""
            subattributes:
              - name: "default"
                type: "string"
                description: ""

              - name: "label"
                type: "string"
                description: ""

              - name: "name"
                type: "string"
                description: ""

              - name: "options"
                type: "array"
                description: ""
                subattributes:
                  - name: "label"
                    type: "string"
                    description: ""

                  - name: "name"
                    type: "string"
                    description: ""

              - name: "required"
                type: "string"
                description: ""

              - name: "type"
                type: "string"
                description: ""

          - name: "form_url"
            type: "string"
            description: ""

          - name: "icon_url"
            type: "string"
            description: ""

          - name: "label"
            type: "string"
            description: ""

          - name: "params"
            type: "array"
            description: ""
            subattributes:
              - name: "name"
                type: "string"
                description: ""

              - name: "value"
                type: "string"
                description: ""

          - name: "url"
            type: "string"
            description: ""

          - name: "user_attribute_params"
            type: "array"
            description: ""
            subattributes:
              - name: "name"
                type: "string"
                description: ""

              - name: "user_attribute"
                type: "string"
                description: ""

      - name: "alias"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "approximate"
        type: "string"
        description: ""

      - name: "approximate_threshold"
        type: "number"
        description: ""

      - name: "can_filter"
        type: "string"
        description: ""

      - name: "convert_tz"
        type: "string"
        description: ""

      - name: "datatype"
        type: "string"
        description: ""

      - name: "description"
        type: "string"
        description: ""

      - name: "direction"
        type: "string"
        description: ""

      - name: "drill_fields"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "fanout_on"
        type: "string"
        description: ""

      - name: "filters"
        type: "array"
        description: ""
        subattributes:
          - name: "field"
            type: "string"
            description: ""

          - name: "value"
            type: "string"
            description: ""

      - name: "group_item_label"
        type: "string"
        description: ""

      - name: "group_label"
        type: "string"
        description: ""

      - name: "hidden"
        type: "string"
        description: ""

      - name: "html"
        type: "string"
        description: ""

      - name: "label"
        type: "string"
        description: ""

      - name: "label_from_parameter"
        type: "string"
        description: ""

      - name: "links"
        type: "array"
        description: ""
        subattributes:
          - name: "icon_url"
            type: "string"
            description: ""

          - name: "label"
            type: "string"
            description: ""

          - name: "url"
            type: "string"
            description: ""

      - name: "list_field"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "percentile"
        type: "number"
        description: ""

      - name: "precision"
        type: "integer"
        description: ""

      - name: "required_access_grants"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "required_fields"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "sql"
        type: "string"
        description: ""

      - name: "sql_distinct_key"
        type: "string"
        description: ""

      - name: "suggest_dimension"
        type: "string"
        description: ""

      - name: "suggest_explore"
        type: "string"
        description: ""

      - name: "suggestable"
        type: "string"
        description: ""

      - name: "tags"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "value_format"
        type: "string"
        description: ""

      - name: "value_format_name"
        type: "string"
        description: ""

      - name: "view_label"
        type: "string"
        description: ""
  
  - name: "parameters"
    type: "array"
    description: ""
    subattributes:
      - name: "alias"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "allowed_values"
        type: "array"
        description: ""
        subattributes:
          - name: "label"
            type: "string"
            description: ""

          - name: "value"
            type: "string"
            description: ""

      - name: "bypass_suggest_restrictions"
        type: "string"
        description: ""

      - name: "convert_tz"
        type: "string"
        description: ""

      - name: "default_value"
        type: "string"
        description: ""

      - name: "description"
        type: "string"
        description: ""

      - name: "full_suggestions"
        type: "string"
        description: ""

      - name: "hidden"
        type: "string"
        description: ""

      - name: "label"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "required_access_grants"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "required_fields"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "suggest_dimension"
        type: "string"
        description: ""

      - name: "suggest_explore"
        type: "string"
        description: ""

      - name: "suggest_persist_for"
        type: "string"
        description: ""

      - name: "suggestable"
        type: "string"
        description: ""

      - name: "suggestions"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "tags"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "view_label"
        type: "string"
        description: ""

  
  - name: "required_access_grants"
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
      - name: "fields"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "name"
        type: "string"
        description: ""

  - name: "sha"
    type: "string"
    description: ""

  - name: "sql_table_name"
    type: "string"
    description: ""

  - name: "suggestions"
    type: "string"
    description: ""

  - name: "view_label"
    type: "string"
    description: ""
---
