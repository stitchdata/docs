---
tap: "helpscout"
version: "1"

key: "conversation-thread"
name: "conversation_threads"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-helpscout/blob/master/tap_helpscout/schemas/conversation_threads.json"
description: |
  The `{{ table.name }}` table contains info about the threads that make up [`conversations`](#conversations).

replication-method: "Key-based Incremental"

api-method:
    name: "List threads"
    doc-link: "https://developer.helpscout.com/mailbox-api/endpoints/conversations/threads/list/"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The conversation thread ID."
    #foreign-key-id: "conversation-thread-id"

  - name: "created_at"
    type: "date-time"
    replication-key: true
    description: "The UTC time the conversation thread was created."

  - name: "action"
    type: "object"
    description: "Details about the action taken on the conversation thread."
    subattributes:
      - name: "text"
        type: "string"
        description: "**Applicable when thread `type: lineitem`.** A user-friendly description of the action."

      - name: "type"
        type: "string"
        description: "The type of the action."

  - name: "assigned_to"
    type: "object"
    description: |
      Details about the assignee of the conversation thread.

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

  - name: "attachments"
    type: "array"
    description: "A list of conversation attachments."

  - name: "bcc"
    type: "array"
    description: "A list of emails that have been BCC'd on the conversation."
    subattributes:
      - name: "value"
        type: "string"
        description: "The email that was BCC'd on the conversation."

  - name: "body"
    type: "string"
    description: "The text content of the conversation thread."

  - name: "cc"
    type: "array"
    description: "A list of emails that have been CC'd on the conversation."
    subattributes:
      - name: "value"
        type: "string"
        description: "The email that was CC'd on the conversation."

  - name: "conversation_id"
    type: "integer"
    description: "The ID of the conversation the thread is associated with."
    foreign-key-id: "conversation-id"

  - name: "created_by"
    type: "object"
    description: |
      Details about the user that created the conversation thread.

      {% capture user %}user{% endcapture %}
    subattributes: *user-attributes

  - name: "customer"
    type: "object"
    description: |
      If `type: message`, this will contain details about the customer associated with the conversation.

      If `type: customer`, this will contain details about the customer who initiated the thread.
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

  - name: "opened_at"
    type: "date-time"
    description: "**Applicable only when `type: message`.** The time the thread was viewed by the customer."

  - name: "saved_reply_id"
    type: "integer"
    description: "The ID of the saved reply used to create the thread."

  - name: "source"
    type: "object"
    description: "Details about the originating source of the conversation thread."
    subattributes:
      - name: "type"
        type: "string"
        description: "The originating type of the conversation thread: `email`, `web`, `API`, etc."

      - name: "via"
        type: "string"
        description: |
          The originating source of the conversation thread. Possible values are:

          - `user`
          - `customer`

  - name: "state"
    type: "string"
    description: |
      The [state of the thread](https://developer.helpscout.com/mailbox-api/endpoints/conversations/threads/list/#thread-state){:target="new"}. Possible values are:

      - `draft`
      - `hidden`
      - `published`
      - `review`

  - name: "status"
    type: "string"
    description: |
      The [status of the thread](https://developer.helpscout.com/mailbox-api/endpoints/conversations/threads/list/#thread-status){:target="new"}. Possible values are:

      - `active`
      - `closed`
      - `nochange`
      - `pending`
      - `spam`

  - name: "to"
    type: "array"
    description: "A list of emails that from the `to:` field."
    subattributes:
      - name: "value"
        type: "string"
        description: "The email included in the `to:` field."

  - name: "type"
    type: "string"
    description: |
      The [type of the thread](https://developer.helpscout.com/mailbox-api/endpoints/conversations/threads/list/#thread-type){:target="new"}. Possible values are:

      - `beaconchat`
      - `chat`
      - `customer`
      - `fowardchild`
      - `forwardparent`
      - `lineitem`
      - `message`
      - `note`
      - `phone`
---