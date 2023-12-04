---
tap: "mailshake"
version: "1"
key: "recipient"

name: "recipients"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-mailshake/blob/master/tap_mailshake/schemas/recipients.json"
description: |
  The `{{ table.name }}` table contains info about the recipients in a campaign.

replication-method: "Key-based Incremental"

api-method:
  name: "List recipients"
  doc-link: "https://api-docs.mailshake.com/?shell#List33"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "recipient-id"

  - name: "created"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "action"
    type: "string"
    description: ""

  - name: "campaignId"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-id"

  - name: "emailAddress"
    type: "string"
    description: ""

  - name: "fields"
    type: "object"
    description: ""
    subattributes:
      - name: "VARIES"
        type: "ANY"
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
---