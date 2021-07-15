---
tap: "zendesk-chat"
version: "1"
key: "ban"

name: "bans"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-zendesk-chat/blob/master/tap_zendesk_chat/schemas/bans.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
  name: ""
  doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    description: ""

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