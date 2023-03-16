---
tap: "asana"
version: "2"
key: "portfolio"

name: "portfolios"
doc-link: "https://developers.asana.com/docs/portfolios"
singer-schema: "https://github.com/singer-io/tap-asana/blob/master/tap_asana/schemas/portfolios.json"
description: |
  The `{{ table.name }}` table contains info about the portfolios in your {{ integration.display_name }} account.

  #### Custom fields

  To replicate task custom fields, select the `custom_fields` attribute in Stitch. If your destination doesn't natively support nested data structures, two subtables (`tasks__custom_fields`, `tasks__custom_fields__enum_options`) will be created.

replication-method: "Full Table"

api-method:
    name: "Get multiple portfolios"
    doc-link: "https://developers.asana.com/docs/get-multiple-portfolios"

attributes:  
  - name: "archived"
    type: "boolean"
    description: ""

  - name: "color"
    type: "string"
    description: ""

  - name: "completed"
    type: "boolean"
    description: ""

  - name: "completed_at"
    type: "date-time"
    description: ""

  - name: "completed_by"
    type: "object"
    description: ""
    subattributes:
    - name: "gid"
      type: "string"
      description: ""

    - name: "resource_type"
      type: "string"
      description: ""

    - name: "name"
      type: "string"
      description: ""


  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "created_by"
    type: "object"
    description: ""
    subattributes:
    - name: "gid"
      type: "string"
      description: ""

    - name: "resource_type"
      type: "string"
      description: ""

    - name: "name"
      type: "string"
      description: ""

  - name: "created_from_template"
    type: "object"
    description: ""
    subattributes:
    - name: "gid"
      type: "string"
      description: ""

    - name: "resource_type"
      type: "string"
      description: ""

    - name: "name"
      type: "string"
      description: ""


  - name: "current_status"
    type: "string"
    description: ""

  - name: "current_status_update"
    type: "object"
    description: ""
    subattributes:
    - name: "gid"
      type: "string"
      description: ""

    - name: "resource_type"
      type: "string"
      description: ""

    - name: "resource_subtype"
      type: "string"
      description: ""

    - name: "title"
      type: "string"
      description: ""


  - name: "custom_field_settings"
    type: "array"
    description: ""
    subattributes:
    - name: "gid"
      type: "string"
      description: ""

    - name: "resource_type"
      type: "string"
      description: ""

    - name: "custom_field"
      type: "object"
      description: ""
      subattributes:
      - name: "gid"
        type: "string"
        description: ""

      - name: "resource_type"
        type: "string"
        description: ""

      - name: "created_by"
        type: "object"
        description: ""
        subattributes:
        - name: "gid"
          type: "string"
          description: ""

        - name: "resource_type"
          type: "string"
          description: ""

        - name: "name"
          type: "string"
          description: ""


      - name: "currency_code"
        type: "string"
        description: ""

      - name: "custom_label"
        type: "string"
        description: ""

      - name: "custom_label_position"
        type: "string"
        description: ""

      - name: "date_value"
        type: "object"
        description: ""
        subattributes:
        - name: "date"
          type: "string"
          description: ""

        - name: "date_time"
          type: "date-time"
          description: ""


      - name: "description"
        type: "string"
        description: ""

      - name: "display_value"
        type: "string"
        description: ""

      - name: "enabled"
        type: "boolean"
        description: ""

      - name: "enum_options"
        type: "array"
        description: ""
        subattributes:
        - name: "gid"
          type: "string"
          description: ""

        - name: "resource_type"
          type: "string"
          description: ""

        - name: "name"
          type: "string"
          description: ""

        - name: "enabled"
          type: "boolean"
          description: ""

        - name: "color"
          type: "string"
          description: ""


      - name: "enum_value"
        type: "object"
        description: ""
        subattributes:
        - name: "gid"
          type: "string"
          description: ""

        - name: "resource_type"
          type: "string"
          description: ""

        - name: "name"
          type: "string"
          description: ""

        - name: "enabled"
          type: "boolean"
          description: ""

        - name: "color"
          type: "string"
          description: ""


      - name: "format"
        type: "string"
        description: ""

      - name: "has_notifications_enabled"
        type: "boolean"
        description: ""

      - name: "is_global_to_workspace"
        type: "boolean"
        description: ""

      - name: "multi_enum_values"
        type: "array"
        description: ""
        subattributes:
        - name: "gid"
          type: "string"
          description: ""

        - name: "resource_type"
          type: "string"
          description: ""

        - name: "color"
          type: "string"
          description: ""

        - name: "enabled"
          type: "boolean"
          description: ""

        - name: "name"
          type: "string"
          description: ""


      - name: "name"
        type: "string"
        description: ""

      - name: "number_value"
        type: "number"
        description: ""

      - name: "people_value"
        type: "array"
        description: ""
        subattributes:
        - name: "gid"
          type: "string"
          description: ""

        - name: "resource_type"
          type: "string"
          description: ""

        - name: "name"
          type: "string"
          description: ""


      - name: "precision"
        type: "integer"
        description: ""

      - name: "resource_subtype"
        type: "string"
        description: ""

      - name: "text_value"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""


    - name: "is_important"
      type: "boolean"
      description: ""

    - name: "parent"
      type: "object"
      description: ""
      subattributes:
      - name: "gid"
        type: "string"
        description: ""

      - name: "resource_type"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""


    - name: "project"
      type: "object"
      description: ""
      subattributes:
      - name: "gid"
        type: "string"
        description: ""

      - name: "resource_type"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""



  - name: "custom_fields"
    type: "array"
    description: ""
    subattributes:
    - name: "gid"
      type: "string"
      description: ""

    - name: "resource_type"
      type: "string"
      description: ""

    - name: "name"
      type: "string"
      description: ""

    - name: "resource_subtype"
      type: "string"
      description: ""

    - name: "type"
      type: "string"
      description: ""

    - name: "enum_options"
      type: "array"
      description: ""
      subattributes:
      - name: "gid"
        type: "string"
        description: ""

      - name: "resource_type"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "enabled"
        type: "boolean"
        description: ""

      - name: "color"
        type: "string"
        description: ""


    - name: "enum_value"
      type: "object"
      description: ""
      subattributes:
      - name: "gid"
        type: "string"
        description: ""

      - name: "resource_type"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "enabled"
        type: "boolean"
        description: ""

      - name: "color"
        type: "string"
        description: ""


    - name: "enabled"
      type: "boolean"
      description: ""

    - name: "text_value"
      type: "string"
      description: ""

    - name: "number_value"
      type: "number"
      description: ""

    - name: "description"
      type: "string"
      description: ""

    - name: "precision"
      type: "integer"
      description: ""

    - name: "is_global_to_workspace"
      type: "boolean"
      description: ""

    - name: "has_notifications_enabled"
      type: "boolean"
      description: ""

    - name: "date_value"
      type: "object"
      description: ""
      subattributes:
      - name: "date"
        type: "string"
        description: ""

      - name: "date_time"
        type: "date-time"
        description: ""


    - name: "display_value"
      type: "string"
      description: ""

    - name: "multi_enum_values"
      type: "array"
      description: ""
      subattributes:
      - name: "gid"
        type: "string"
        description: ""

      - name: "resource_type"
        type: "string"
        description: ""

      - name: "color"
        type: "string"
        description: ""

      - name: "enabled"
        type: "boolean"
        description: ""

      - name: "name"
        type: "string"
        description: ""



  - name: "default_view"
    type: "string"
    description: ""

  - name: "due_date"
    type: "string"
    description: ""

  - name: "due_on"
    type: "string"
    description: ""

  - name: "followers"
    type: "array"
    description: ""
    subattributes:
    - name: "gid"
      type: "string"
      description: ""

    - name: "resource_type"
      type: "string"
      description: ""

    - name: "name"
      type: "string"
      description: ""


  - name: "gid"
    type: "string"
    description: ""
    primary-key: true

  - name: "html_notes"
    type: "string"
    description: ""

  - name: "icon"
    type: "string"
    description: ""

  - name: "is_template"
    type: "boolean"
    description: ""

  - name: "members"
    type: "array"
    description: ""
    subattributes:
    - name: "gid"
      type: "string"
      description: ""

    - name: "resource_type"
      type: "string"
      description: ""

    - name: "name"
      type: "string"
      description: ""


  - name: "modified_at"
    type: "date-time"
    description: ""
    replication-key: true

  - name: "name"
    type: "string"
    description: ""

  - name: "notes"
    type: "string"
    description: ""

  - name: "owner"
    type: "object"
    description: ""
    subattributes:
    - name: "gid"
      type: "string"
      description: ""

    - name: "resource_type"
      type: "string"
      description: ""

    - name: "name"
      type: "string"
      description: ""


  - name: "permalink_url"
    type: "string"
    description: ""

  - name: "portfolio_items"
    type: "array"
    description: ""
    subattributes:
    - name: "gid"
      type: "string"
      description: ""

    - name: "resource_type"
      type: "string"
      description: ""

    - name: "name"
      type: "string"
      description: ""

  - name: "project_brief"
    type: "object"
    description: ""
    subattributes:
    - name: "gid"
      type: "string"
      description: ""

    - name: "resource_type"
      type: "string"
      description: ""


  - name: "public"
    type: "boolean"
    description: ""

  - name: "resource_type"
    type: "string"
    description: ""

  - name: "start_on"
    type: "string"
    description: ""

  - name: "team"
    type: "object"
    description: ""
    subattributes:
    - name: "gid"
      type: "string"
      description: ""

    - name: "resource_type"
      type: "string"
      description: ""

    - name: "name"
      type: "string"
      description: ""


  - name: "workspace"
    type: "object"
    description: ""
    subattributes:
    - name: "gid"
      type: "string"
      description: ""

    - name: "resource_type"
      type: "string"
      description: ""

    - name: "name"
      type: "string"
      description: ""
---