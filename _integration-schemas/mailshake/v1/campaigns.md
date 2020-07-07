---
tap: "mailshake"
version: "1"
key: "campaign"

name: "campaigns"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-mailshake/blob/master/tap_mailshake/schemas/campaigns.json"
description: |
  The `{{ table.name }}` table contains info about your team's campaigns.

replication-method: "Key-based Incremental"

api-method:
  name: "List a team's campaigns"
  doc-link: "https://api-docs.mailshake.com/?shell#List"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "campaign-id"

  - name: "created"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "actionDate"
    type: "date-time"
    description: ""

  - name: "archived"
    type: "boolean"
    description: ""

  - name: "endedAt"
    type: "date-time"
    description: ""

  - name: "isPaused"
    type: "boolean"
    description: ""

  - name: "messages"
    type: "array"
    description: ""
    subattributes:
      - name: "campaignId"
        type: "integer"
        description: ""
        foreign-key-id: "campaign-id"

      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "message-id"

      - name: "isPaused"
        type: "boolean"
        description: ""

      - name: "object"
        type: "string"
        description: ""

      - name: "replyToID"
        type: "integer"
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

  - name: "sender"
    type: "object"
    description: ""
    subattributes:
      - name: "created"
        type: "date-time"
        description: ""

      - name: "emailAddress"
        type: "string"
        description: ""

      - name: "fromName"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "sender-id"

      - name: "object"
        type: "string"
        description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "url"
    type: "uri"
    description: ""
---