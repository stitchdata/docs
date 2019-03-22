---
tap: "zendesk"
version: "1.0"

name: "ticket_comments"
doc-link: https://developer.zendesk.com/rest_api/docs/support/ticket_comments
singer-schema: https://github.com/singer-io/tap-zendesk/blob/master/tap_zendesk/schemas/ticket_comments.json
description: |
  The `{{ table.name }}` table contains info about the comments on tickets, which is the conversation between requesters, collaborators, and agents. Comments can be public or private.

replication-method: "Key-based Incremental"

api-method:
  name: List comments
  doc-link: https://developer.zendesk.com/rest_api/docs/support/ticket_comments#list-comments

attributes:
  - name: "id"
    type: "integer"
    description: "The ticket comment ID."
    primary-key: true
    foreign-key-id: "ticket-comment-id"

  - name: "created_at"
    type: "string"
    replication-key: true
    description: "The time the ticket comment was created."

  - name: "body"
    type: "string"
    description: "The body of the comment."

  - name: "ticket_id"
    type: "integer"
    description: "The ID of the ticket associated with the comment."
    foreign-key-id: "ticket-id"

  - name: "type"
    type: "string"
    description: |
      The comment type. Possible values are `Comment` or `VoiceComment`.

  - name: "html_body"
    type: "string"
    description: "The comment formatted as HTML."

  - name: "plain_body"
    type: "string"
    description: "The comment as plain text."

  - name: "public"
    type: "boolean"
    description: "If `true`, the comment is public. Otherwise, the comment is an internal note."

  - name: "audit_id"
    type: "integer"
    description: "The ID of the associated ticket audit."
    foreign-key-id: "ticket-audit-id"

  - name: "author_id"
    type: "integer"
    description: "The ID of the comment author."
    foreign-key-id: "user-id"

  - name: "attachments"
    type: "array"
    description: "Details about attachments associated with the ticket comment, if any."
    subattributes:
      - name: "id"
        type: "integer"
        description: "The attachment ID."

      - name: "file_name"
        type: "string"
        description: "The name of the image file."

      - name: "content_url"
        type: "string"
        description: "The full URL where the image file can be downloaded."

      - name: "content_type"
        type: "string"
        description: "The content type of the image. For example: `image/png`"

      - name: "size"
        type: "integer"
        description: "The size of the image file in bytes."

      - name: "inline"
        type: "boolean"
        description: "If `true`, the attachment is excluded from the attachment list and the attachment URL can be referenced within the comment of a ticket."

      - name: "thumbnails"
        type: "array"
        description: "Details about the attachment's thumbnails."
        subattributes:
          - name: "id"
            type: "integer"
            description: "The attachment thumbnail ID."

          - name: "file_name"
            type: "string"
            description: "The name of the image thumbnail file."

          - name: "content_url"
            type: "string"
            description: "The full URL where the image thumbnail file can be downloaded."

          - name: "content_type"
            type: "string"
            description: "The content type of the image thumbnail. For example: `image/png`"

          - name: "size"
            type: "integer"
            description: "The size of the image thumbnail in bytes."

  - name: "via"
    type: "object"
    description: "Details about how the ticket comment was created."
    subattributes:
      - name: "source"
        type: "object"
        description: "Details about how the ticket comment was created."
        subattributes:
          - name: "from"
            type: "object"
            description: ""
            subattributes:
              - name: "name"
                type: "string"
                description: ""

              - name: "ticket_id"
                type: "integer"
                description: ""
                foreign-key-id: "ticket-id"

              - name: "address"
                type: "string"
                description: ""

              - name: "subject"
                type: "string"
                description: ""

          - name: "to"
            type: "object"
            description: ""
            subattributes:
              - name: "address"
                type: "string"
                description: ""

              - name: "name"
                type: "string"
                description: ""

          - name: "rel"
            type: "string"
            description: ""

      - name: "channel"
        type: "string"
        description: "The channel used to create the ticket comment. For example: `web`, `rule`, `mobile`"

  - name: "metadata"
    type: "object"
    description: "System information (web client, IP address, etc.) and comment flags, if any."
    subattributes:
      # Commenting out these fields - they're not documented by Zendesk.
      # - name: "custom"
      #   type: 
      #   description: ""

      # - name: "trusted"
      #   type: "boolean"
      #   description: ""

      # - name: "notifications_suppressed_for"
      #   type: "array"
      #   description: "[TODO]"
      #   subattributes:
      #     - name: "value"
      #       type: "integer"
      #       description: "[TODO]"

      - name: "flags"
        type: "array"
        description: "For `Comment` and `VoiceComment` events, the comment flags applied to the comment."
        subattributes:
          - name: "value"
            type: "integer"
            description: |
              The value of the flag applied to the comment. [Refer to {{ integration.display_name }}'s documentation for more info](https://developer.zendesk.com/rest_api/docs/support/ticket_comments#comment-flags){:target="new"}.

              Possible values are:

              - `0` - {{ integration.display_name }} is unsure the comment should be trusted.
              - `2` - The comment author was not part of the conversation.
              - `3` - The comment author wasn't signed in when the comment was submitted.
              - `4` - The comment was automatically generated.
              - `5` - The attached file was rejected because it's too big.
              - `11` - The comment was submitted by the user on behalf of the author.

      - name: "flags_options"
        type: "object"
        description: "For `Comment` and `VoiceComment` events, additional information about the comment flags."
---