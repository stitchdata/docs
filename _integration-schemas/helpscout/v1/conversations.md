---
tap: "helpscout"
version: "1.0"

key: "conversation"
name: "conversations"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-helpscout/blob/master/tap_helpscout/schemas/conversations.json"
description: |
  The `{{ table.name }}` table contains info about the conversations in your {{ integration.display_name }} mailbox. Stitch will replicate all conversations, including active, closed, open, pending, and spam.

  **Note**: If custom fields are available, Stitch will replicate them.

replication-method: "Key-based Incremental"

api-method:
    name: "List conversations"
    doc-link: "https://developer.helpscout.com/mailbox-api/endpoints/conversations/list/"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The conversation ID."
    foreign-key-id: "conversation-id"

  - name: "user_updated_at"
    type: "date-time"
    replication-key: true
    description: "The UTC time when the last user update occurred; equal to `customerWaitingSince` if a no user action since the last customer action."

  - name: "assignee"
    type: "object"
    description: |
      Details about the assignee of the conversation.

      {% capture user %}assignee{% endcapture %}
    subattributes: &user-attributes
      - name: "email"
        type: "string"
        description: "The {{ user }}'s email address."

      - name: "first"
        type: "string"
        description: "The {{ user }}'s first name."

      - name: "id"
        type: "integer"
        description: "The {{ user }}'s user ID."
        foreign-key-id: "user-id"

      - name: "last"
        type: "string"
        description: "The {{ user }}'s last name."

      - name: "photo_url"
        type: "string"
        description: "The URL of the {{ user }}'s photo, if one exists."

      - name: "type"
        type: "string"
        description: |
          The user type. Possible values are:

          - `team`
          - `user`

  - name: "bcc"
    type: "array"
    description: "A list of emails that have been BCC'd on the conversation."
    subattributes:
      - name: "value"
        type: "string"
        description: "The email that was BCC'd on the conversation."

  - name: "cc"
    type: "array"
    description: "A list of emails that have been CC'd on the conversation."
    subattributes:
      - name: "value"
        type: "string"
        description: "The email that was CC'd on the conversation."

  - name: "closed_by"
    type: "integer"
    description: "The ID of the {{ integration.display_name }} user that closed the conversation."
    foreign-key-id: "user-id"

  - name: "created_at"
    type: "date-time"
    description: "The UTC time when the conversation was created."

  - name: "created_by"
    type: "object"
    description: |
      Details about the user who created the conversation.

      {% capture user %}user{% endcapture %}
    subattributes: *user-attributes

  - name: "custom_fields"
    type: "array"
    description: "Custom fields associated with the conversation."
    subattributes:
      - name: "id"
        type: "number"
        description: "The custom field's ID."

      - name: "name"
        type: "string"
        description: "The name of the custom field."

      - name: "value"
        type: "string"
        description: "The value of the custom field."

      - name: "text"
        type: "string"
        description: "The text value of the custom field."

  - name: "customer_waiting_since"
    type: "object"
    description: "Details about when the conversation was last updated."
    subattributes:
      - name: "friendly"
        type: "string"
        description: "A user-friendly version of the waiting period."

      - name: "last_reply_from"
        type: "string"
        description: "Indicates if the last reply was from a user or a customer."

      - name: "time"
        type: "date-time"
        description: "The UTC time since the last reply sent to the customer."

  - name: "folder_id"
    type: "integer"
    description: "The ID of the mailbox folder the conversation is in."
    foreign-key-id: "mailbox-folder-id"

  - name: "mailbox_id"
    type: "integer"
    description: "The ID of the mailbox the conversation is in."
    foreign-key-id: "mailbox-id"

  - name: "number"
    type: "integer"
    description: ""

  - name: "preview"
    type: "string"
    description: "Preview text from the start of the conversation."

  - name: "primary_customer"
    type: "object"
    description: |
      Details about the primary customer in the conversation.

      {% capture user %}primary customer{% endcapture %}
    subattributes:
      - name: "email"
        type: "string"
        description: "The customer's email address."

      - name: "first"
        type: "string"
        description: "The customer's first name."

      - name: "id"
        type: "integer"
        description: "The customer's user ID."
        foreign-key-id: "customer-id"

      - name: "last"
        type: "string"
        description: "The customer's last name."

      - name: "photo_url"
        type: "string"
        description: "The URL of the customer's photo, if one exists."

      - name: "type"
        type: "string"
        description: |
          The user type. Possible values are:

          - `team`
          - `user`

  - name: "source"
    type: "object"
    description: "Details about the originating source of the conversation."
    subattributes:
      - name: "type"
        type: "string"
        description: "The originating type of the conversation: `email`, `web`, `API`, etc."

      - name: "via"
        type: "string"
        description: |
          The originating source of the conversation. Possible values are:

          - `user`
          - `customer`

  - name: "state"
    type: "string"
    description: |
      The state of the conversation. Possible values are:
      
      - `deleted`
      - `draft`
      - `published`

  - name: "status"
    type: "string"
    description: |
      The status of the conversation. Possible values are:

      - `active`
      - `all`
      - `closed`
      - `open`
      - `pending`
      - `spam`

  - name: "subject"
    type: "string"
    description: "The subject of the conversation."

  - name: "tags"
    type: "array"
    description: "A list of tags applied to the conversation."
    subattributes:
      - name: "value"
        type: "string"
        description: "The tag applied to the conversation."

  - name: "threads"
    type: "integer"
    description: "The number of threads the conversation has."

  - name: "type"
    type: "string"
    description: |
      The type of the conversation. Possible values are:

      - `chat`
      - `email`
      - `phone`
---