---
tap: "asana"
version: "2.0"
key: "story"

name: "stories"
doc-link: "https://developers.asana.com/docs/stories"
singer-schema: "https://github.com/singer-io/tap-asana/blob/master/tap_asana/schemas/stories.json"
description: |
  The `{{ table.name }}` table contains info about all stories within specified tasks in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "Get stories from a task"
    doc-link: "https://developers.asana.com/docs/get-stories-from-a-task"

attributes:
  - name: "gid"
    type: "string"
    primary-key: true
    description: "The story's GID."
    foreign-key-id: "story-id"

  - name: "created_at"
    type: "date-time"
    description: "The time the story was created."
    replication-key: true  

  - name: "assignee"
    type: "object"
    description: ""
    subattributes:
      - name: "gid"
        type: "string"
        description: "The user's GID."
        foreign-key-id: "user-id"
      - name: "name"
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
        description: "The user's GID."
        foreign-key-id: "user-id"
      - name: "name"
        type: "string"
        description: ""
      - name: "resource_type"
        type: "string"
        description: ""
  - name: "dependency"
    type: "object"
    description: ""
    subattributes:
      - name: "gid"
        type: "string"
        description: "The user's GID."
        foreign-key-id: "user-id"
      - name: "name"
        type: "string"
        description: ""
      - name: "resource_type"
        type: "string"
        description: ""
  - name: "duplicate_of"
    type: "object"
    description: ""
    subattributes:
      - name: "gid"
        type: "string"
        description: ""
      - name: "name"
        type: "string"
        description: ""
      - name: "resource_type"
        type: "string"
        description: ""
  - name: "duplicated_from"
    type: "object"
    description: ""
    subattributes:
      - name: "gid"
        type: "string"
        description: ""
      - name: "name"
        type: "string"
        description: ""
      - name: "resource_type"
        type: "string"
        description: ""
  - name: "follower"
    type: "object"
    description: ""
    subattributes:
      - name: "gid"
        type: "string"
        description: ""
      - name: "name"
        type: "string"
        description: ""
      - name: "resource_type"
        type: "string"
        description: ""
  
  - name: "hearted"
    type: "boolean"
    description: ""
  - name: "hearts"
    type: "null"
    description: ""
  - name: "html_text"
    type: "string"
    description: ""
  - name: "is_edited"
    type: "boolean"
    description: ""
  - name: "is_pinned"
    type: "boolean"
    description: ""
  - name: "liked"
    type: "boolean"
    description: ""
  - name: "likes"
    type: "null"
    description: ""
  - name: "new_approval_status"
    type: "boolean"
    description: ""
  - name: "new_dates"
    type: "object"
    description: ""
    subattributes:
      - name: "due_at"
        type: "date-time"
        description: ""
      - name: "due_on"
        type: "date-time"
        description: ""
      - name: "start_on"
        type: "date-time"
        description: ""
  - name: "new_enum_value"
    type: "object"
    description: ""
    subattributes:
      - name: "color"
        type: "string"
        description: ""
      - name: "enabled"
        type: "boolean"
        description: ""
      - name: "gid"
        type: "string"
        description: ""
      - name: "name"
        type: "string"
        description: ""
      - name: "resource_type"
        type: "string"
        description: ""
  - name: "new_name"
    type: "string"
    description: ""
  - name: "new_number_value"
    type: "number"
    description: ""
  - name: "new_resource_subtype"
    type: "string"
    description: ""
  - name: "new_section"
    type: "object"
    description: ""
    subattributes:
      - name: "gid"
        type: "string"
        description: "The section's GID."
        foreign-key-id: "section-id"
      - name: "name"
        type: "string"
        description: ""
      - name: "resource_type"
        type: "string"
        description: ""
  - name: "new_text_value"
    type: "string"
    description: ""
  - name: "num_hearts"
    type: "integer"
    description: ""
  - name: "num_likes"
    type: "integer"
    description: ""
  - name: "old_approval_status"
    type: "string"
    description: ""
  - name: "old_dates"
    type: "object"
    description: ""
    subattributes:
      - name: "due_at"
        type: "date-time"
        description: ""
      - name: "due_on"
        type: "date-time"
        description: ""
      - name: "start_on"
        type: "date-time"
        description: ""
  - name: "old_enum_value"
    type: "object"
    description: ""
    subattributes:
      - name: "color"
        type: "string"
        description: ""
      - name: "enabled"
        type: "boolean"
        description: ""
      - name: "gid"
        type: "string"
        description: ""
      - name: "name"
        type: "string"
        description: ""
      - name: "resource_type"
        type: "string"
        description: ""
  - name: "old_name"
    type: "string"
    description: ""
  - name: "old_number_value"
    type: "number"
    description: ""
  - name: "old_resource_subtype"
    type: "string"
    description: ""
  - name: "old_section"
    type: "object"
    description: ""
    subattributes:
      - name: "gid"
        type: "string"
        description: "The section's GID."
        foreign-key-id: "section-id"
      - name: "name"
        type: "string"
        description: ""
      - name: "resource_type"
        type: "string"
        description: ""
  - name: "old_text_value"
    type: "string"
    description: ""
  - name: "previews"
    type: "null"
    description: ""
  - name: "project"
    type: "object"
    description: ""
    subattributes:
      - name: "gid"
        type: "string"
        description: "The project's GID."
        foreign-key-id: "project-id"
      - name: "name"
        type: "string"
        description: ""
      - name: "resource_type"
        type: "string"
        description: ""
  - name: "resource_subtype"
    type: "string"
    description: ""
  - name: "resource_type"
    type: "string"
    description: ""
  - name: "source"
    type: "string"
    description: ""
  - name: "story"
    type: "object"
    description: ""
    subattributes:
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
          - name: "name"
            type: "string"
            description: ""
          - name: "resource_type"
            type: "string"
            description: ""
      - name: "gid"
        type: "string"
        description: "The story's GID."
        foreign-key-id: "story-id"
      - name: "name"
        type: "string"
        description: ""
      - name: "resource_subtype"
        type: "string"
        description: ""
      - name: "resource_type"
        type: "string"
        description: ""
  - name: "tag"
    type: "object"
    description: ""
    subattributes:
      - name: "gid"
        type: "string"
        description: "The tag's GID."
        foreign-key-id: "tag-id"
      - name: "name"
        type: "string"
        description: ""
      - name: "resource_type"
        type: "string"
        description: ""
  - name: "target"
    type: "object"
    description: ""
    subattributes:
      - name: "gid"
        type: "string"
        description: ""
      - name: "name"
        type: "string"
        description: ""
  - name: "task"
    type: "object"
    description: ""
    subattributes:
      - name: "gid"
        type: "string"
        description: "The task's GID."
        foreign-key-id: "task-id"
      - name: "name"
        type: "string"
        description: ""
      - name: "resource_type"
        type: "string"
        description: ""
  - name: "text"
    type: "string"
    description: ""
---