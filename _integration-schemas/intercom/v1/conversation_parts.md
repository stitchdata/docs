---
tap: "intercom"
version: "1"
key: "conversation-part"

name: "conversation_parts"
doc-link: "https://developers.intercom.com/intercom-api-reference/v2.0/reference#conversation-model"
singer-schema: "https://github.com/singer-io/tap-intercom/blob/master/tap_intercom/schemas/conversation_parts.json"
description: |
  The `{{ table.name }}` table lists the individual parts of conversations in your {{ integration.display_name }} account.

  **Note**: When this table is replicated, all conversation parts associated with an updated conversation will be replicated.

replication-method: "Full Table"

api-method:
  name: "Retrieve a conversation"
  doc-link: "https://developers.intercom.com/intercom-api-reference/v2.0/reference#retrieve-a-conversation"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The conversation part ID."
    # foreign-key-id: "part-id"

  - name: "assigned_to"
    type: "string"
    description: "The ID of the admin that the conversation part is assigned to."
    foreign-key-id: "admin-id"

  - name: "attachments"
    type: "array"
    description: "Details about the attachments, if any, that are a part of the conversation part."
    subattributes:
      - name: "url"
        type: "string"
        description: "The attachment URL."

      - name: "name"
        type: "string"
        description: "The name of the attachment. Ex: `image001.png`, `presentation.pdf`"

      - name: "content_type"
        type: "string"
        description: "The content type of the attachment. Ex: `image/png`, `application/pdf`"

      - name: "height"
        type: "integer"
        description: "For image attachments, the height of the image."

      - name: "width"
        type: "integer"
        description: "For image attachments, the width of the image."

      - name: "filesize"
        type: "integer"
        description: "The file size of the attachment."

      - name: "type"
        type: "string"
        description: "The value of this field will be `upload`."

  - name: "author"
    type: "object"
    description: "Details about the admin or user that created the conversation part."
    subattributes:
      - name: "id"
        type: "string"
        description: |
          The ID of the admin or end-user that created the conversation part.

          Depending on the author's `type`, this will be a foreign key to either the [`admins`](#admins) or [`contacts`](#contacts) table.

      - name: "type"
        type: "string"
        description: "The type of user that created the conversation part."

  - name: "body"
    type: "string"
    description: "The HTML-encoded body of the conversation part."

  - name: "conversation_created_at"
    type: "date-time"
    description: "The time the parent conversation associated with the part was created."

  - name: "conversation_id"
    type: "string"
    description: "The ID of the conversation associated with the part."
    foreign-key-id: "conversation-id"

  - name: "conversation_total_parts"
    type: "integer"
    description: "The total number of conversation parts associated with the parent conversation."

  - name: "conversation_updated_at"
    type: "date-time"
    description: "The time the parent conversation associated with the part was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the conversation part was created."

  - name: "external_id"
    type: "string"
    description: ""

  - name: "notified_at"
    type: "date-time"
    description: "The time the user was notified with the conversation part."

  - name: "part_type"
    type: "string"
    description: "The type of the conversation part."

  - name: "type"
    type: "string"
    description: "This will be `conversation_part`."

  - name: "updated_at"
    type: "date-time"
    description: "The time the conversation part was updated."
---