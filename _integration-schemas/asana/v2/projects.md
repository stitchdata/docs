---
tap: "asana"
version: "2"
key: "project"

name: "projects"
doc-link: "https://asana.com/developers/api-reference/projects"
singer-schema: "https://github.com/singer-io/tap-asana/blob/master/tap_asana/schemas/projects.json"
description: |
  The `{{ table.name }}` table contains info about the projects the user who authorized the {{ integration.display_name }} integration in Stitch has access to.

replication-method: "Key-based Incremental"

attributes:
  - name: "gid"
    type: "string"
    primary-key: true
    description: "The project's GID."
    foreign-key-id: "project-id"

  - name: "modified_at"
    type: "date-time"
    replication-key: true
    description: "The time the project was last modified."

  - name: "archived"
    type: "boolean"
    description: "Indicates if the project has been archived or not."

  - name: "color"
    type: "string"
    description: |
      The color of the project. Possible values are:

      - `dark-pink`
      - `dark-green` 
      - `dark-blue`
      - `dark-red`
      - `dark-teal` 
      - `dark-brown` 
      - `dark-orange` 
      - `dark-purple`
      - `dark-warm-gray` 
      - `light-pink`
      - `light-green` 
      - `light-blue`
      - `light-red`
      - `light-teal` 
      - `light-yellow` 
      - `light-orange`
      - `light-purple`
      - `light-warm-gray`

  - name: "created_at"
    type: "date-time"
    description: "The time the project was created."

  - name: "current_status"
    type: "string"
    description: "The most recently created status update for the project."

  - name: "custom_fields"
    type: "array"
    description: "Details about the custom fields for the project, and the values applied to them."
    subattributes:
      - name: "description"
        type: "string"
        description: "The description of the custom field."
      - name: "enabled"
        type: "boolean"
        description: "Indicates if the custom field is enabled or not."
      - name: "enum_options"
        type: "array"
        description: |
          **Applicable only when `resource_subtype: enum`.** The possible values that the `enum` field can adopt.

          {% assign type =  "option" %}
        subattributes: &enum-attributes
          - name: "color"
            type: "string"
            description: "The color of the enum {{ type }}. Defaults to `none`."
          - name: "enabled"
            type: "boolean"
            description: "Indicates if the enum {{ type }} is enabled."
          - name: "gid"
            type: "string"
            description: "The globally unique identifier for the enum {{ type }}."
          - name: "name"
            type: "string"
            description: "The name of the enum {{ type }}."
          - name: "resource_type"
            type: "string"
            description: "The base type of the resource."
      - name: "enum_value"
        type: "object"
        description: |
          **Applicable only when `resource_subtype: enum`.** Details about the chosen value for the `enum` field.

          {% assign type =  "value" %}
        subattributes: *enum-attributes

      - name: "gid"
        type: "string"
        description: "The globally unique identifier for the resource."
      - name: "has_notifications_enabled"
        type: "boolean"
        description: "Indicates whether a follower of a project with this custom field should receive inbox notifications when the field's value changes."
      - name: "is_global_to_workspace"
        type: "boolean"
        description: "Indicates whether the custom field is available to every container in the work space."
      - name: "name"
        type: "string"
        description: "The name of the custom field."
      - name: "number_value"
        type: "number"
        description: "**Applicable only when `resource_subtype: number`.** The value of a custom number field."
      - name: "precision"
        type: "integer"
        description: |
          **Applicable only when `resource_subtype: number`.** The number of places after the decimal to round to for custom number fields.

          From {{ integration.display_name }}'s documentation:

          > 0 is integer values, 1 rounds to the nearest tenth, and so on. Must be between 0 and 6, inclusive. For percentage format, this may be unintuitive, as a value of 0.25 has a precision of 0, while a value of 0.251 has a precision of 1. This is due to 0.25 being displayed as 25%. The identifier format will always have a precision of 0.

      - name: "resource_subtype"
        type: "string"
        description: |
          The type of the custom field. Possible values are:

          - `text`
          - `enum`
          - `number`
          
      - name: "resource_type"
        type: "string"
        description: "The base type of the resource."
      - name: "text_value"
        type: "string"
        description: "**Applicable only when `resource_subtype: text`.** The value of a custom text field."
      
      - name: "type"
        type: "string"
        description: "**Deprecated by {{ integration.display_name }}.** Use `resource_subtype` instead."


      - name: "date_value"
        type: "object"
        description: ""
        subattributes:

          - name: "date"
            type: "string"
            description: ""

          - name: "date_time"
            type: "string"
            description: ""
      
      - name: "display_value"
        type: "string"
        description: ""

      - name: "multi_enum_values"
        type: "array"
        description: ""
        subattributes:

        - name: "items"
          type: "object"
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

  - name: "due_date"
    type: "date-time"
    description: "The day on which the project is due."

  - name: "followers"
    type: "array"
    description: "A list of users following the project."
    subattributes:
      - name: "gid"
        type: "string"
        description: "The follower's GID."
        foreign-key-id: "user-id"

      - name: "resource_type"
        type: "string"
        description: "This will be `user`."

  - name: "members"
    type: "array"
    description: "A list of users who are members of the project."
    subattributes:
      - name: "gid"
        type: "string"
        description: "The user's GID."
        foreign-key-id: "user-id"

      - name: "resource_type"
        type: "string"
        description: "This will be `user`."

  - name: "name"
    type: "string"
    description: "The name of the project."

  - name: "notes"
    type: "string"
    description: "Any notes associated with the project."

  - name: "owner"
    type: "object"
    description: "Details about the current owner of the project."
    subattributes:
      - name: "gid"
        type: "string"
        description: "The owner's GID."
        foreign-key-id: "user-id"

      - name: "resource_type"
        type: "string"
        description: "This will be `user`."

  - name: "public"
    type: "boolean"
    description: "Indicates if the project is public to the organization."

  - name: "team"
    type: "object"
    description: "Details about the team the project is associated with."
    subattributes:
      - name: "gid"
        type: "string"
        description: "The team's GID."

      - name: "id"
        type: "integer"
        description: "The team's ID."

      - name: "resource_type"
        type: "string"
        description: "This will be `team`."

  - name: "workspace"
    type: "object"
    description: "Details about the workspace or organization the project is associated with."
    subattributes:
      - name: "gid"
        type: "string"
        description: "The workspace's GID."
        foreign-key-id: "workspace-id"

      - name: "resource_type"
        type: "string"
        description: "This will be `workspace`."


  - name: "default_view"
    type: "string"
    description: ""

  - name: "due_on"
    type: "string"
    description: ""

  - name: "html_notes"
    type: "string"
    description: ""

  - name: "is_template"
    type: "boolean"
    description: ""

  - name: "start_on"
    type: "string"
    description: ""

  - name: "icon"
    type: "string"
    description: ""

  - name: "permalink_url"
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

    - name: "items"
      type: "object"
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
                  type: "string"
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

              - name: "items"
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

              - name: "items"
                type: "object"
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

              - name: "items"
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

  - name: "completed"
    type: "boolean"
    description: ""

  - name: "completed_at"
    type: "string"
    description: ""
    format: date-time

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

---