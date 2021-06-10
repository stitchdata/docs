---
tap: "mambu"
version: "1"

name: "tasks"
doc-link: "https://api.mambu.com/?shell#welcome"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/tasks.json"
description: "This table contains information about Tasks."

replication-method: "Key-based Incremental"

api-method:
  name: "Get all tasks"
  doc-link: "https://api.mambu.com/?http#tasks-getall"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The task ID."
#    foreign-key-id: "task-id"

  - name: "last_modified_date"
    type: "date-time"
    description: "The date and time the task was last modified."
    replication-key: true

  - name: "assigned_user_key"
    type: "string"
    description: ""
    foreign-key-id: "user-encoded-key"

  - name: "created_by_full_name"
    type: "string"
    description: ""

  - name: "created_by_user_key"
    type: "string"
    description: ""
    foreign-key-id: "user-encoded-key"

  - name: "creation_date"
    type: "date-time"
    description: ""

  - name: "custom_field_sets"
    type: "array"
    description: ""
    subattributes:
      - name: "custom_field_set_id"
        type: "string"
        description: ""
        foreign-key-id: "custom-field-set-id"

      - name: "custom_field_values"
        type: "array"
        description: ""
        subattributes:
          - name: "custom_field_id"
            type: "string"
            description: ""
            foreign-key-id: "custom-field-id"
          - name: "custom_field_value"
            type: "string"
            description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "due_date"
    type: "date"
    description: ""

  - name: "encoded_key"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "task_link"
    type: "string"
    description: ""

  - name: "task_link_type"
    type: "string"
    description: ""

  - name: "title"
    type: "string"
    description: ""
---