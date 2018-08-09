---
tap: "uservoice"
# version: "1.0"

name: "comments"
doc-link: "https://developer.uservoice.com/docs/api/v2/reference/#/comments,comments_0?q=comments"
singer-schema: https://github.com/singer-io/tap-uservoice/blob/master/tap_uservoice/streams/comments.py
description: |
  The `comments` table contains info about the comments forum users have made.

replication-method: "Key-based Incremental"

api-method:
  name: List comments
  doc-link: https://developer.uservoice.com/docs/api/v2/reference/#list-comments

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The comment ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the comment was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the comment was created."

  - name: "body"
    type: "string"
    description: "The plaintext body of the comment."

  - name: "body_mime_type"
    type: "string"
    description: "The MIME type of the comment body."

  - name: "state"
    type: "string"
    description: "The state of the comment. For example: `approved`"

  - name: "inappropriate_flags_count"
    type: "integer"
    description: "The count of times the comment has been flagged as inappropriate."

  - name: "is_admin_comment"
    type: "boolean"
    description: "If `true`, the comment was made by an admin."

  - name: "channel"
    type: "string"
    description: "The channel used to create the comment."

  - name: "links"
    type: "object"
    description: "Details about the links associated with the comment."
    object-attributes: 
      - name: "suggestion"
        type: "integer"
        description: "The ID of the suggestion."
        foreign-key: true
        table: "suggestions"

      - name: "created_by"
        type: "integer"
        description: "The ID of the user who created the comment."
        foreign-key: true
        table: "users"
---