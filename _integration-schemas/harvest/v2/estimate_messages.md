---
tap: "harvest"
version: "2"

name: "estimate_messages"
doc-link: https://help.getharvest.com/api-v2/estimates-api/estimates/estimate-messages/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/estimate_messages.json
description: |
  The `{{ table.name }}` table contains info about the messages associated with estimates.

replication-method: "Key-based Incremental"

api-method:
  name: List all messages for an estimate
  doc-link: https://help.getharvest.com/api-v2/estimates-api/estimates/estimate-messages/#list-all-messages-for-an-estimate

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The estimate message ID."
    # foreign-key-id: "estimate-message-id"

  - name: "updated_at"
    type: "string"
    replication-key: true
    description: "The time the message was last updated."

  - name: "sent_by"
    type: "string"
    description: "The name of the user that created the message."

  - name: "sent_by_email"
    type: "string"
    description: "The email of the user that created the message."

  - name: "sent_from"
    type: "string"
    description: "The name of the user that the message was sent from."

  - name: "sent_from_email"
    type: "string"
    description: "The email of the user that the message was sent from."

  - name: "subject"
    type: "string"
    description: "The message subject."

  - name: "body"
    type: "string"
    description: "The message body."

  - name: "send_me_a_copy"
    type: "boolean"
    description: "If `true`, a copy of the message will be emailed to the current user."

  - name: "event_type"
    type: "string"
    description: |
      The type of estimate event that occurred with the message. Possible values are:

      - `sent`
      - `accept`
      - `decline`
      - `re-open`
      - `view`
      - `invoice`

  - name: "created_at"
    type: "string"
    description: "The time the message was created."

  - name: "estimate_id"
    type: "integer"
    description: "The ID of the estimate the message is associated."
    foreign-key-id: "estimate-id"

  - name: "recipients"
    type: "object"
    description: "Details about the recipients of the message."
    subattributes:
      - name: "name"
        type: "string"
        description: "The name of the message recipient."

      - name: "email"
        type: "string"
        description: "The email address of the message recipient."
---