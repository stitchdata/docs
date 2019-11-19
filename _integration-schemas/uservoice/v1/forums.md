---
tap: "uservoice"
version: "1.0"

name: "forums"
doc-link: https://developer.uservoice.com/docs/api/v2/reference/#/Forum
singer-schema: https://github.com/singer-io/tap-uservoice/blob/master/tap_uservoice/streams/forums.py
description: |
  The `{{ table.name }}` table contains info about your discussion forums.

replication-method: "Key-based Incremental"

api-method:
  name: List forums
  doc-link: https://developer.uservoice.com/docs/api/v2/reference/#

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The forum ID."
    foreign-key-id: "forum-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the forum was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the forum was created."

  - name: "name"
    type: "string"
    description: "The name of the forum."

  - name: "welcome_message"
    type: "string"
    description: "The welcome message that displays in the forum."

  - name: "welcome_message_mime_type"
    type: "string"
    description: "The MIME type of the forum's `welcome_message`."

  - name: "prompt"
    type: "string"
    description: "The question that displays to users when they are creating ideas in the forum."

  - name: "example"
    type: "string"
    description: ""

  - name: "portal_url"
    type: "string"
    description: "The portal URL for the forum."

  - name: "open_suggestions_count"
    type: "integer"
    description: "The total number of open suggestions in the forum."

  - name: "suggestions_count"
    type: "integer"
    description: "The total number of suggestions created in the forum."

  - name: "category_required"
    type: "boolean"
    description: "If `true`, users must select a category when creating an idea."

  - name: "is_public"
    type: "boolean"
    description: "If `true`, the forum is public."

  - name: "is_private"
    type: "boolean"
    description: "If `true`, the forum is private."

  - name: "classic_voting"
    type: "boolean"
    description: "If `true`, classic voting is enabled for the forum."

  - name: "links"
    type: "object"
    description: ""
    subattributes: 
    - name: "updated_by"
      type: "integer"
      description: "The ID of the user who last updated the forum settings."
      foreign-key-id: "user-id"
---