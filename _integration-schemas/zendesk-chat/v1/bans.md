---
tap: "zendesk-chat"
version: "1"
key: "ban"

name: "bans"
doc-link: "https://developer.zendesk.com/api-reference/live-chat/chat-api/bans/"
singer-schema: "https://github.com/singer-io/tap-zendesk-chat/blob/master/tap_zendesk_chat/schemas/bans.json"
description: |
  The `{{ table.name }}` table contains info about bans created in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "get Bans"
  doc-link: "https://developer.zendesk.com/api-reference/live-chat/chat-api/bans/"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ban ID."
    #foreign-key-id: "ban-id"

  - name: "ip_address"
    type: "string"
    description: ""

  - name: "reason"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "visitor_id"
    type: "string"
    description: ""

  - name: "visitor_name"
    type: "string"
    description: ""
---