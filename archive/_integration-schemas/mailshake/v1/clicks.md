---
tap: "mailshake"
version: "1"
key: "click"

name: "clicks"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-mailshake/blob/master/tap_mailshake/schemas/clicks.json"
description: |
  The `{{ table.name }}` table contains info about recent click activity.

replication-method: "Key-based Incremental"

api-method:
  name: "Get click activity"
  doc-link: "https://api-docs.mailshake.com/?shell#Clicks"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    # foreign-key-id: "click-id"

  - name: "actionDate"
    type: "date-time"
    replication-key: true
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

  - name: "isDuplicate"
    type: "boolean"
    description: ""

  - name: "link"
    type: "uri"
    description: ""

  - name: "object"
    type: "string"
    description: ""

  - name: "parent"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
        # foreign-key-id: "sent-message-id"

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

      - name: "type"
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
        subattributes: ""

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
---