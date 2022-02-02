---
tap: "intercom"
version: "1"
key: "conversation"

name: "conversations"
doc-link: "https://developers.intercom.com/intercom-api-reference/v2.0/reference#conversation-model"
singer-schema: "https://github.com/singer-io/tap-intercom/blob/master/tap_intercom/schemas/conversations.json"
description: |
  The `{{ table.name }}` table contains info about user conversations in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "List all conversations"
  doc-link: "https://developers.intercom.com/intercom-api-reference/v2.0/reference#list-conversations"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The conversation ID."
    foreign-key-id: "conversation-id"

  - name: "updated_at"
    type: "date-time"
    description: "The time that the conversation was last updated."
    replication-key: true

  - name: "assignee"
    type: "object"
    description: "Details about the admin or team assigned to the conversation."
    subattributes:
      - name: "email"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: |
          The ID of the admin or team assigned to the conversation message.

          Depending on the `type`, this will be a foreign key to either the [`admins`](#admins) or [`teams`](#teams) table.

      - name: "name"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

  - name: "contacts"
    type: "array"
    description: "Information about the contacts associated with the conversation."
    subattributes:
      - name: "id"
        type: "string"
        description: "The contact ID."
        foreign-key-id: "contact-id"

      - name: "type"
        type: "string"
        description: ""
              
  - name: "conversation_message"
    type: "object"
    description: "A list of message details."
    subattributes:
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

      - name: "author"
        type: "object"
        description: "Details about the user that created the conversation message."
        subattributes:
          - name: "id"
            type: "string"
            description: |
              The ID of the user who created the conversation message.

              Depending on the author's `type`, this will be a foreign key to either the [`admins`](#admins) or [`contacts`](#contacts) table.

          - name: "type"
            type: "string"
            description: |
              The type of user that created the conversation message. Possible values are:

              - `user`
              - `lead`
              - `admin`

      - name: "body"
        type: "string"
        description: "The conversation message body, which may contain HTML. This is the body of the message that started the conversation."

      - name: "delivered_as"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: "The ID of the conversation message."

      - name: "subject"
        type: "string"
        description: "The conversation message subject, or the subject of the message that started the conversation."

      - name: "type"
        type: "string"
        description: |
          The type of the conversation message. Possible values are:

          - `conversation`
          - `push`
          - `facebook`
          - `twitter`
          - `email`

      - name: "url"
        type: "string"
        description: "The URL where the conversation was started. For Twitter, Email, and Bots, this will be `null`."

  - name: "conversation_rating"
    type: "object"
    description: "Details about the rating for the conversation."
    subattributes:
      - name: "created_at"
        type: "date-time"
        description: "The time that the conversation being rated was created."

      - name: "customer"
        type: "object"
        description: "Details about the customer who rated the conversation."
        subattributes:
          - name: "id"
            type: "string"
            description: "The customer ID."
            foreign-key-id: "contact-id"

          - name: "type"
            type: "string"
            description: "This will be `contact`."

      - name: "rating"
        type: "integer"
        description: "The rating, between 1 and 5, for the conversation."

      - name: "remark"
        type: "string"
        description: "A remark about the rating, if any."

      - name: "teammate"
        type: "object"
        description: "The ID of the teammate associated with the conversation when it was rated."
        subattributes:
          - name: "id"
            type: "integer"
            description: "The ID of the teammate."
            foreign-key-id: "admin-id"

          - name: "type"
            type: "string"
            description: "The type of the teammate."

  - name: "created_at"
    type: "date-time"
    description: "The time the conversation was created."

  - name: "customer_first_reply"
    type: "object"
    description: "Details about the customer's first reply to the conversation."
    subattributes:
      - name: "created_at"
        type: "date-time"
        description: "The time the user's message was created, in Unix timestamp format."

      - name: "type"
        type: "string"
        description: |
          The channel over which the first reply occurred. Possible values are:

          - `conversation`
          - `push`
          - `facebook`
          - `twitter`
          - `email`

      - name: "url"
        type: "string"
        description: "The URL where the first reply originated from."

  - name: "customers"
    type: "array"
    description: "Details about the customers involved in the conversation."
    subattributes:
      - name: "id"
        type: "string"
        description: "The customer ID."
        foreign-key-id: "contact-id"

      - name: "type"
        type: "string"
        description: "The type of the customer. This will be either `lead` or `user`."
  
  - name: "first_contact_reply"
    type: "object"
    description: "Details about the contact's first reply to the conversation."
    subattributes:
      - name: "created_at"
        type: "date-time"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

  - name: "open"
    type: "boolean"
    description: "Indicates whether a conversation is open/snoozed (`true`) or closed (`false`)."

  - name: "priority"
    type: "string"
    description: "The conversation's priority level."

  - name: "read"
    type: "boolean"
    description: "Indicates whether a conversation has been read."

  - name: "sent_at"
    type: "date-time"
    description: ""
  
  - name: "sla_applied"
    type: "object"
    description: "Information about the service-level agreement applied to the conversation."
    subattributes:
      - name: "sla_name"
        type: "string"
        description: ""

      - name: "sla_status"
        type: "string"
        description: ""

  - name: "snoozed_until"
    type: "date-time"
    description: "If set, this is the time in the future when the conversation will be marked as open."

  - name: "source"
    type: "object"
    description: ""
    subattributes:
      - name: "attachments"
        type: "array"
        description: ""

      - name: "author"
        type: "object"
        description: ""
        anchor-id: 2
        subattributes:
          - name: "email"
            type: "string"
            description: ""

          - name: "id"
            type: "string"
            description: |
              The ID of the user who created the source.

              Depending on the author's `type`, this will be a foreign key to either the [`admins`](#admins) or [`contacts`](#contacts) table.

          - name: "name"
            type: "string"
            description: ""

          - name: "type"
            type: "string"
            description: ""

      - name: "body"
        type: "string"
        description: ""

      - name: "delivered_as"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "subject"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""  

  - name: "state"
    type: "string"
    description: |
      The current state of the conversation. Possible values are:

      - `open`
      - `closed`
      - `snoozed`

  - name: "statistics"
    type: "object"
    description: "Details on conversation statistics."
    subattributes:
      - name: "count_assignments"
        type: "integer"
        description: ""

      - name: "count_conversation_parts"
        type: "integer"
        description: ""

      - name: "count_reopens"
        type: "integer"
        description: ""

      - name: "first_admin_reply_at"
        type: "date-time"
        description: ""

      - name: "first_assignment_at"
        type: "date-time"
        description: ""

      - name: "first_close_at"
        type: "date-time"
        description: ""

      - name: "first_contact_reply_at"
        type: "date-time"
        description: ""

      - name: "last_admin_reply_at"
        type: "date-time"
        description: ""

      - name: "last_assignment_admin_reply_at"
        type: "date-time"
        description: ""

      - name: "last_assignment_at"
        type: "date-time"
        description: ""

      - name: "last_close_at"
        type: "date-time"
        description: ""

      - name: "last_closed_by_id"
        type: "integer"
        description: ""

      - name: "last_contact_reply_at"
        type: "date-time"
        description: ""

      - name: "median_time_to_reply"
        type: "integer"
        description: ""

      - name: "time_to_admin_reply"
        type: "integer"
        description: ""

      - name: "time_to_assignment"
        type: "integer"
        description: ""

      - name: "time_to_first_close"
        type: "integer"
        description: ""

      - name: "time_to_last_close"
        type: "integer"
        description: ""

      - name: "type"
        type: "string"
        description: ""

  - name: "tags"
    type: "array"
    description: "Details about the tags applied to the conversation."
    subattributes:
      - name: "id"
        type: "string"
        description: "The tag ID."
        foreign-key-id: "tag-id"

      - name: "applied_at"
        type: "date-time"
        description: "The time the tag was applied."

      - name: "applied_by"
        type: "object"
        description: "Details about the admin that applied the tag."
        subattributes:
          - name: "id"
            type: "integer"
            description: "The admin ID."
            foreign-key-id: "admin-id"

          - name: "type"
            type: "string"
            description: "This will be `tag`."

      - name: "name"
        type: "string"
        description: "The name of the tag."

      - name: "type"
        type: "string"
        description: "This will be `tags.list`."
  
  - name: "teammates"
    type: "object"
    description: "Information about team members."
    subattributes:
      - name: "admins"
        type: "array"
        description: "The admin IDs of the team members associated with the conversation."
        subattributes:
          - name: "id"
            type: "string"
            description: "The admin ID."
            foreign-key-id: "admin-id"

          - name: "type"
            type: "string"
            description: ""

      - name: "type"
        type: "string"
        description: ""

  - name: "type"
    type: "string"
    description: "This will be `conversation`."
  
  - name: "user"
    type: "object"
    description: "A list of users associated with the conversation."
    subattributes:
      - name: "id"
        type: "string"
        description: "The user ID."

      - name: "type"
        type: "string"
        description: ""

  - name: "waiting_since"
    type: "date-time"
    description: "The last time a contact responded to an admin. In other words, the time a customer started waiting for a response. This will be `null` if last reply is from an admin."
---