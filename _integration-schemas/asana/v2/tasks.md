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
  - name: "gid"
    type: "string"
    primary-key: true
    description: "The task's GID."
    #foreign-key-id: "task-id"

  - name: "modified_at"
    type: "date-time"
    replication-key: true
    description: "The time the task was last modified."

  - name: "assignees"
    type: "array"
    description: "A list of users assigned to the task."
    subattributes:
      - name: "gid"
        type: "string"
        description: "The assignee's GID."
        foreign-key-id: "user-id"

      - name: "resource_type"
        type: "string"
        description: "This will be `user`."

  - name: "assignee_status"
    type: "string"
    description: "The scheduling status of the task for the user it is assigned to."

  - name: "completed"
    type: "boolean"
    description: "Indicates if the task has been completed or not."

  - name: "completed_at"
    type: "date-time"
    description: "The time at which the task was completed. This will be `null` until `completed: true`."

  - name: "created_at"
    type: "date-time"
    description: "The time the task was created."

  - name: "custom_fields"
    type: "array"
    description: |
      Details about the custom fields for the task, and the values applied to them.
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

          - name: "id"
            type: "integer"
            description: "The enum {{ type }} ID."

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
        description: "Indicates whether a follower of a task with this custom field should receive inbox notifications when the field's value changes."

      - name: "id"
        type: "integer"
        description: "The ID of the custom field."

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

  - name: "due_at"
    type: "date-time"
    description: "The date and time on which the task is due. This will be `null` if the task has no due time."

  - name: "due_on"
    type: "date-time"
    description: "The date on which the task is due. This will be `null` if the task has no due date."

  - name: "external"
    type: "string"
    description: ""

  - name: "followers"
    type: "array"
    description: "A list of users following the task."
    subattributes:
      - name: "gid"
        type: "string"
        description: "The follower's GID."
        foreign-key-id: "user-id"

      - name: "resource_type"
        type: "string"
        description: "This will be `user`."

  - name: "hearted"
    type: "boolean"
    description: ""

  - name: "hearts"
    type: "string"
    description: ""

  - name: "memberships"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: "The name of the task."

  - name: "notes"
    type: "string"
    description: "Any notes associated with the task."

  - name: "num_hearts"
    type: "integer"
    description: "The number of users who have hearted this task."

  - name: "parent"
    type: "string"
    description: "The parent of the task, or `null` if this is not a subtask."
    foreign-key-id: "task-id"

  - name: "projects"
    type: "array"
    description: "A list of projects the task is associated with."
    subattributes:
      - name: "gid"
        type: "string"
        description: "The project's GID."
        foreign-key-id: "project-id"

      - name: "resource_type"
        type: "string"
        description: "This will be `project`."

  - name: "workspace"
    type: "object"
    description: "Details about the workspace or organization the task is associated with."
    subattributes:
      - name: "gid"
        type: "string"
        description: "The workspace's GID."
        foreign-key-id: "workspace-id"

      - name: "resource_type"
        type: "string"
        description: "This will be `workspace`."
---