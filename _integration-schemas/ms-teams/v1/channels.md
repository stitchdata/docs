---
tap: "ms-teams"
version: "1"
key: ""

name: "channels"
doc-link: "https://docs.microsoft.com/en-us/graph/api/channel-list?view=graph-rest-1.0&tabs=http"
singer-schema: "https://github.com/singer-io/tap-ms-teams/blob/master/tap_ms_teams/schemas/channels.json"
description: |
  The `{{ table.name }}` table contains information about the channels within a team in your Microsoft account.

replication-method: "Full Table"

api-method:
    name: "List channels"
    doc-link: "https://docs.microsoft.com/en-us/graph/api/channel-list?view=graph-rest-1.0&tabs=http"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The channel ID."
    foreign-key-id: "channel-id"

  - name: "description"
    type: "string"
    description: ""
  - name: "display_name"
    type: "string"
    description: ""
  - name: "email"
    type: "string"
    description: ""
  
  - name: "web_url"
    type: "string"
    description: ""
---
