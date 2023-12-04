---
tap: "slack"
version: "1"
key: "team"

name: "teams"
doc-link: "https://api.slack.com/methods/team.info"
singer-schema: "https://github.com/singer-io/tap-slack/blob/master/tap_slack/schemas/teams.json"
description: |
  The `{{ table.name }}` table contains info about teams in your {{ integration.display_name }} workspace.

replication-method: "Full Table"

api-method:
  name: "team.info"
  doc-link: "https://api.slack.com/methods/team.info"

attributes:
  - name: "id"
    type: "string"
    description: "The team ID."
    foreign-key-id: "team-id"

  - name: "archived"
    type: "boolean"
    description: ""

  - name: "avatar_base_url"
    type: "uri"
    description: ""

  - name: "created"
    type: "date-time"
    description: ""

  - name: "date_create"
    type: "date-time"
    description: ""

  - name: "deleted"
    type: "date-time"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "discoverable"
    type: "string"
    description: ""

  - name: "domain"
    type: "string"
    description: ""

  - name: "email_domain"
    type: "string"
    description: ""

  - name: "enterprise_id"
    type: "string"
    description: ""

  - name: "enterprise_name"
    type: "string"
    description: ""

  - name: "has_compliance_export"
    type: "boolean"
    description: ""

  - name: "icon"
    type: "object"
    description: ""
    subattributes:
      - name: "image_102"
        type: "string"
        description: ""

      - name: "image_132"
        type: "string"
        description: ""

      - name: "image_230"
        type: "string"
        description: ""

      - name: "image_34"
        type: "string"
        description: ""

      - name: "image_44"
        type: "string"
        description: ""

      - name: "image_68"
        type: "string"
        description: ""

      - name: "image_88"
        type: "string"
        description: ""

      - name: "image_default"
        type: "boolean"
        description: ""

  - name: "is_assigned"
    type: "boolean"
    description: ""

  - name: "is_enterprise"
    type: "integer"
    description: ""

  - name: "messages_count"
    type: "integer"
    description: ""

  - name: "msg_edit_window_mins"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "over_integrations_limit"
    type: "boolean"
    description: ""

  - name: "over_storage_limit"
    type: "boolean"
    description: ""

  - name: "plan"
    type: "string"
    description: ""
---