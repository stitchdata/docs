---
tap: "iterable-core"
version: "1"
key: ""

name: "message_types"
doc-link: https://api.iterable.com/api/docs#messageTypes_messageTypes
singer-schema: https://github.com/singer-io/tap-iterable/tree/master/tap_iterable/schemas/message_types.json
description: |
  The **{{ table.name }}** table contains information about all message types within your {{ integration.display_name }} project.

replication-method: "Full Table"

api-method:
  name: "List message types"
  doc-link: "https://api.iterable.com/api/docs#messageTypes_messageTypes"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The message type ID."
    foreign-key-id: "message-id"

  - name: "channelId"
    type: "integer"
    description: "The channel ID."
    foreign-key-id: "channel-id"

  - name: "createdAt"
    type: "date-time"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "subscriptionPolicy"
    type: "string"
    description: ""

  - name: "updatedAt"
    type: "date-time"
    description: ""

---
