---
tap: "mailshake"
version: "1"
key: "sent-message"

name: "sent_messages"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-mailshake/blob/master/tap_mailshake/schemas/sent_messages.json"
description: |
  The `{{ table.name }}` table contains info about recently sent emails.

replication-method: "Key-based Incremental"

api-method:
  name: "Get sent activity"
  doc-link: "https://api-docs.mailshake.com/?shell#Sent"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    # foreign-key-id: "activity-id"

  - name: "actionDate"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "body"
    type: "string"
    description: ""

  - name: "campaign"
    type: "object"
    description: ""
    subattributes:
      - name: "created"
        type: "date-time"
        description: ""

      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "campaign-id"

      - name: "object"
        type: "string"
        description: ""

      - name: "title"
        type: "string"
        description: ""

  - name: "externalConversationID"
    type: "string"
    description: ""

  - name: "externalID"
    type: "string"
    description: ""

  - name: "externalRawMessageID"
    type: "string"
    description: ""

  - name: "from"
    type: "object"
    description: ""
    subattributes:
      - name: "address"
        type: "string"
        description: ""

      - name: "first"
        type: "string"
        description: ""

      - name: "fullName"
        type: "string"
        description: ""

      - name: "last"
        type: "string"
        description: ""

      - name: "object"
        type: "string"
        description: ""

  - name: "message"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "message-id"

      - name: "object"
        type: "string"
        description: ""

      - name: "subject"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

  - name: "object"
    type: "string"
    description: ""

  - name: "plainTextBody"
    type: "string"
    description: ""

  - name: "rawBody"
    type: "string"
    description: ""

  - name: "recipient"
    type: "object"
    description: ""
    subattributes:
      - name: "action"
        type: "string"
        description: ""

      - name: "created"
        type: "date-time"
        description: ""

      - name: "emailAddress"
        type: "string"
        description: ""

      - name: "fields"
        type: "object"
        description: ""
        subattributes: 

      - name: "first"
        type: "string"
        description: ""

      - name: "fullName"
        type: "string"
        description: ""

      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "recipient-id"

      - name: "isPaused"
        type: "boolean"
        description: ""

      - name: "last"
        type: "string"
        description: ""

      - name: "object"
        type: "string"
        description: ""

  - name: "subject"
    type: "string"
    description: ""

  - name: "to"
    type: "array"
    description: ""
    subattributes:
      - name: "address"
        type: "string"
        description: ""

      - name: "first"
        type: "string"
        description: ""

      - name: "fullName"
        type: "string"
        description: ""

      - name: "last"
        type: "string"
        description: ""

      - name: "object"
        type: "string"
        description: ""

  - name: "type"
    type: "string"
    description: ""
---