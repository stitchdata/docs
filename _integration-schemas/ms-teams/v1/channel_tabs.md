---
tap: "ms-teams"
version: "1"
key: "channel-tab"

name: "channel_tabs"
doc-link: "https://docs.microsoft.com/en-us/graph/api/teamstab-list?view=graph-rest-beta"
singer-schema: "https://github.com/singer-io/tap-ms-teams/blob/master/tap_ms_teams/schemas/channel_tabs.json"
description: |
  The `{{ table.name }}` table contains information about tabs within a channel in one of your Microsoft teams.

replication-method: "Full Table"

api-method:
  name: "List tabs in channel"
  doc-link: "https://docs.microsoft.com/en-us/graph/api/teamstab-list?view=graph-rest-1.0"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The channel tab ID."
    #foreign-key-id: "tab-id"

  - name: "channel_id"
    type: "string"
    description: "The channel ID."
    foreign-key-id: "channel-id"

  - name: "configuration"
    type: "object"
    description: ""
    subattributes:
      - name: "content_url"
        type: "string"
        description: ""

      - name: "entity_id"
        type: "string"
        description: ""

      - name: "has_content"
        type: "boolean"
        description: ""

      - name: "remove_url"
        type: "string"
        description: ""

      - name: "website_url"
        type: "string"
        description: ""

      - name: "wiki_default_tab"
        type: "boolean"
        description: ""

      - name: "wiki_tab_id"
        type: "integer"
        description: ""

  - name: "display_name"
    type: "string"
    description: ""

  - name: "group_id"
    type: "string"
    description: "The group ID."
    foreign-key-id: "group-id"

  - name: "sort_order_index"
    type: "string"
    description: ""

  - name: "teams_app"
    type: "object"
    description: ""
    subattributes:
      - name: "display_name"
        type: "string"
        description: ""

      - name: "distribution_method"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""

  - name: "web_url"
    type: "string"
    description: ""
---