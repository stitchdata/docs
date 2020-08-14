---
tap: "intercom"
version: "02-02-2016"

name: "conversations"
doc-link: https://developers.intercom.com/reference#conversations
description: |
  The `{{ table.name }}` table contains info about user conversations, or conversations initiated by your end-users.

  #### Conversation Parts
  To reconstruct an entire conversation, use the `conversation_parts` associated with the conversation. These are the individual elements - actions, messages, and so on - that make up a conversation.

  If your destination doesn't natively support nested data structures, a subtable named `conversations__conversation_parts` will be created. More info on this table can be found below.

replication-method: "Key-based Incremental"
api-method:
  name: listConversations
  doc-link: https://developers.intercom.io/docs/list-conversations
attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The conversation ID."
    # foreign-key-id: "conversation-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the conversation was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the conversation was created."

  - name: "waiting_since"
    type: "date-time"
    description: |
      An epoch timestamp that indicates the last time a customer responded to an admin, or the time a customer started waiting for a response.

      **Note**: According to [{{ integration.display_name }}'s documentation](https://developers.intercom.com/reference#conversation-model), this field may sometimes contain a value that is 2000 years in the future. This can occur when the last person to respond was an admin or when the conversation was closed aver a customer response.

  - name: "snoozed_until"
    type: "date-time"
    description: "If set, this is the time in the future that the conversation will be marked as `open`."

  - name: "state"
    type: "string"
    description: |
      The current state of the conversation. Possible values are:

      - `open`
      - `closed`
      - `snoozed`

  - name: "conversation_message"
    type: "object"
    description: "Details about the message that started the conversation."
    doc-link: https://developers.intercom.com/reference#section-message-object
    subattributes:
      - name: "subject"
        type: "string"
        description: "The conversation message subject, or the subject of the message that started the conversation."

      - name: "body"
        type: "string"
        description: "The conversation message body, which may contain HTML. This is the body of the message that started the conversation."

      - name: "author"
        type: "object"
        description: "Details about the user that created the conversation message."
        subattributes:
          - name: "id"
            type: "string"
            description: |
              The ID of the user who created the conversation message.

              Depending on the user's `type`, this will be a foreign key to the `users` or `admins` table.
            foreign-key-id: "author-id"

          - name: "type"
            type: "string"
            description: |
              The type of user that created the conversation message. Possible values are:

              - `user`
              - `lead`
              - `admin`

      - name: "attachments"
        type: "array"
        description: "Details about the attachments, if any, that are a part of the conversation message."
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

      - name: "type"
        type: "string"
        description: "The value of this field will be `conversation_message`."

  - name: "conversation_parts"
    type: "array"
    description: "Details about the individual elements that make up the conversation."
    subattributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The conversation part ID."

      - name: "part_type"
        type: "string"
        description: |
          The type of conversation part. Possible values are:

          - `comment` - A standard reply from a user or admin. 
          - `note` - Created by and only viewable to an admin.
          - `assignment` - Assignment of the conversation to an admin or nobody. Viewable only to an admin.
          - `open` - Opens the conversation. Viewable only to an admin.
          - `close` - Closes the conversation. Viewable only to an admin.

      - name: "body"
        type: "string"
        description: "The HTML-encoded body of the conversation part."

      - name: "created_at"
        type: "date-time"
        description: "The time the conversation part was created."

      - name: "updated_at"
        type: "date-time"
        description: "The time the conversation part was last updated."

      - name: "assigned_to"
        type: "string"
        description: "For `assignment` types only: the ID of the admin that the conversation is assigned to."
        foreign-key-id: "admin-id"

      - name: "author"
        type: "object"
        description: "Details about the admin or user that created the conversation part."
        subattributes:
          - name: "id"
            type: "string"
            description: "The ID of the admin or user that created the conversation part."
            foreign-key-id: "author-id"

          - name: "type"
            type: "string"
            description: "The type of user that created the conversation part."

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

  - name: "total_count"
    type: "integer"
    description: "The total number of conversation parts in the conversation."

  - name: "user"
    type: "object"
    description: "Details about the user or lead involved in the conversation."
    subattributes:
      - name: "id"
        type: "string"
        description: "The ID of the user or lead involved in the conversation."
        foreign-key-id: "user-id"

      - name: "type"
        type: "string"
        description: |
          The type of user involved in the conversation. Possible values include:

          - `lead`
          - `user`

  - name: "assignee"
    type: "object"
    description: "Details about the admin assigned to the conversation."
    subattributes:
      - name: "id"
        type: "string"
        description: "The ID of the admin that the conversation is assigned to."
        foreign-key-id: "admin-id"

      - name: "type"
        type: "string"
        description: |
          The type of admin the conversation is assigned to. Possible values are:

          - `nobody_admin` - Indicates the conversation is assigned to _Nobody_.
          - `admin` - Indicates the conversation is assigned to an admin.

  - name: "customers"
    type: "array"
    description: "Details about the customers (users or leads) involved in the conversation."
    subattributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The user's ID."
        foreign-key-id: "user-id"

      - name: "type"
        type: "string"
        description: "The value of this field will be `user`."

  - name: "open"
    type: "boolean"
    description: "Indicates whether a conversation is open (`true`) or closed (`false`)."

  - name: "read"
    type: "boolean"
    description: "Indicates whether a conversation has been read."

  - name: "tags"
    type: "array"
    description: "The tags associated with the conversation."
    subattributes:
      - name: "tags"
        type: "array"
        description: "The tags associated with the conversation."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The tag ID."
            foreign-key-id: "tag-id"

          - name: "name"
            type: "string"
            description: "The name of the tag."

          - name: "type"
            type: "string"
            description: "The value of this field will be `tag`."

  - name: "type"
    type: "string"
    description: "The value of this field will be `conversation`."
---