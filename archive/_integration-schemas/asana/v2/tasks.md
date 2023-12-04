---
tap: "asana"
version: "2"
key: "task"

name: "tasks"
doc-link: "https://asana.com/developers/api-reference/tasks"
singer-schema: "https://github.com/singer-io/tap-asana/blob/master/tap_asana/schemas/tasks.json"
description: |
  The `{{ table.name }}` table contains info about the tasks in your {{ integration.display_name }} account.

  #### Custom fields

  To replicate task custom fields, select the `custom_fields` attribute in Stitch. If your destination doesn't natively support nested data structures, two subtables (`tasks__custom_fields`, `tasks__custom_fields__enum_options`) will be created.

replication-method: "Key-based Incremental"

attributes:
  - name: "approval_status"
    type: "string"
    description: ""

  - name: "assignee"
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


  - name: "assignee_section"
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


  - name: "assignee_status"
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


    - name: "display_value"
      type: "string"
      description: ""

    - name: "format"
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



  - name: "dependencies"
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


  - name: "dependents"
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


  - name: "due_at"
    type: "date-time"
    description: ""

  - name: "due_on"
    type: "date-time"
    description: ""

  - name: "external"
    type: "object"
    description: ""
    subattributes:
    - name: "gid"
      type: "string"
      description: ""

    - name: "data"
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

  - name: "hearted"
    type: "boolean"
    description: ""

  - name: "hearts"
    type: "array"
    description: ""
    subattributes:
    - name: "gid"
      type: "string"
      description: ""

    - name: "user"
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




  - name: "hearts"
    type: "null"
    description: ""


  - name: "html_notes"
    type: "string"
    description: ""

  - name: "is_rendered_as_seperator"
    type: "boolean"
    description: ""

  - name: "liked"
    type: "boolean"
    description: ""

  - name: "likes"
    type: "array"
    description: ""
    subattributes:
    - name: "gid"
      type: "string"
      description: ""

    - name: "user"
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




  - name: "likes"
    type: "null"
    description: ""


  - name: "memberships"
    type: "array"
    description: ""
    subattributes:
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


    - name: "section"
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




  - name: "memberships"
    type: "null"
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

  - name: "num_hearts"
    type: "integer"
    description: ""

  - name: "num_likes"
    type: "integer"
    description: ""

  - name: "num_subtasks"
    type: "integer"
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

    - name: "resource_subtype"
      type: "string"
      description: ""


  - name: "permalink_url"
    type: "string"
    description: ""

  - name: "projects"
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

  - name: "resource_type"
    type: "string"
    description: ""

  - name: "start_at"
    type: "date-time"
    description: ""

  - name: "start_on"
    type: "string"
    description: ""

  - name: "tags"
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