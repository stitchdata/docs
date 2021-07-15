---
tap: "zendesk-chat"
version: "1"
key: "account"

name: "account"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-zendesk-chat/blob/master/tap_zendesk_chat/schemas/account.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
  name: ""
  doc-link: ""

attributes:
  - name: "account_key"
    type: "string"
    primary-key: true
    description: ""

  - name: "billing"
    type: "object"
    description: ""
    subattributes:
      - name: "additional_info"
        type: "string"
        description: ""

      - name: "address1"
        type: "string"
        description: ""

      - name: "address2"
        type: "string"
        description: ""

      - name: "city"
        type: "string"
        description: ""

      - name: "company"
        type: "string"
        description: ""

      - name: "country_code"
        type: "string"
        description: ""

      - name: "email"
        type: "string"
        description: ""

      - name: "first_name"
        type: "string"
        description: ""

      - name: "last_name"
        type: "string"
        description: ""

      - name: "postal_code"
        type: "string"
        description: ""

      - name: "state"
        type: "string"
        description: ""

  - name: "create_date"
    type: "date-time"
    description: ""

  - name: "plan"
    type: "object"
    description: ""
    subattributes:
      - name: "agent_leaderboard"
        type: "boolean"
        description: ""

      - name: "agent_reports"
        type: "boolean"
        description: ""

      - name: "analytics"
        type: "boolean"
        description: ""

      - name: "chat_reports"
        type: "boolean"
        description: ""

      - name: "daily_reports"
        type: "boolean"
        description: ""

      - name: "email_reports"
        type: "boolean"
        description: ""

      - name: "file_upload"
        type: "boolean"
        description: ""

      - name: "goals"
        type: "integer"
        description: ""

      - name: "high_load"
        type: "boolean"
        description: ""

      - name: "integrations"
        type: "boolean"
        description: ""

      - name: "ip_restriction"
        type: "boolean"
        description: ""

      - name: "long_desc"
        type: "string"
        description: ""

      - name: "max_advanced_triggers"
        type: "string"
        description: ""

      - name: "max_agents"
        type: "integer"
        description: ""

      - name: "max_basic_triggers"
        type: "string"
        description: ""

      - name: "max_concurrent_chats"
        type: "string"
        description: ""

      - name: "max_departments"
        type: "string"
        description: ""

      - name: "max_history_search_days"
        type: "string"
        description: ""

      - name: "monitoring"
        type: "boolean"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "operating_hours"
        type: "boolean"
        description: ""

      - name: "price"
        type: "number"
        description: ""

      - name: "rest_api"
        type: "boolean"
        description: ""

      - name: "short_desc"
        type: "string"
        description: ""

      - name: "sla"
        type: "boolean"
        description: ""

      - name: "support"
        type: "boolean"
        description: ""

      - name: "unbranding"
        type: "boolean"
        description: ""

      - name: "widget_customization"
        type: "string"
        description: ""

  - name: "status"
    type: "string"
    description: ""
---