---
tap: "freshdesk"
# version:

name: "conversations"
doc-link: https://developers.freshdesk.com/api/#conversations
singer-schema: https://github.com/singer-io/tap-freshdesk/blob/master/tap_freshdesk/schemas/conversations.json
description: |
  The `conversations` table contains info about replies and public/private notes added to the tickets in your Freshdesk account."

replication-method: "Incremental"
api-method:
  name: "listAllConversationsOfATicket"
  doc-link: https://developers.freshdesk.com/api/#list_all_ticket_notes

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The conversation ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the conversation was updated."

  - name: "body_text"
    type: "string"
    description: "The content of the conversation in plain text."

  - name: "incoming"
    type: "boolean"
    description: "Indicates if the conversation should appear as being created from 'outside', ie: not through the Freshdesk web portal."

  - name: "private"
    type: "boolean"
    description: "Indicates if a note is private."

  - name: "user_id"
    type: "integer"
    description: "The ID of the agent/user who added the conversation."

  - name: "support_email"
    type: "string"
    description: "The email address from which replies are sent. For notes, this will be `NULL`."

  - name: "source"
    type: "integer"
    description: "Denotes the type of conversation."

  - name: "ticket_id"
    type: "integer"
    description: "The ID of the ticket to which the conversation is being added."

  - name: "to_emails"
    type: "array"
    description: "Email addresses of agents/users who should be notified about the conversation."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The email address of the person who should be notified about the conversation."

  - name: "from_email"
    type: "string"
    description: "The email address that the message was sent from."

  - name: "cc_emails"
    type: "array"
    description: "Email addresses of agents/users who should be CC'd on the conversation."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The email address of the person who is being CC'd."

  - name: "bcc_emails"
    type: "array"
    description: "Email addresses of agents/users who should be BCC'd on the conversation."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The email address of the person who is being BCC'd."

  - name: "created_at"
    type: "date-time"
    description: "The timestamp of when the conversation was first created."
---