---
tap: "mailshake"
version: "1"
key: "sender"

name: "senders"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-mailshake/blob/master/tap_mailshake/schemas/senders.json"
description: |
  The `{{ table.name }}` table contains info about your team's senders.

replication-method: "Key-based Incremental"

api-method:
  name: "List all senders"
  doc-link: "https://api-docs.mailshake.com/?shell#List75"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "sender-id"

  - name: "created"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "emailAddress"
    type: "string"
    description: ""

  - name: "fromName"
    type: "string"
    description: ""

  - name: "object"
    type: "string"
    description: ""

  - name: "offerType"
    type: "string"
    description: ""
---