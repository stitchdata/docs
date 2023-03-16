---
tap: "looker"
version: "1"
key: "user-session"

name: "user_sessions"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/user_sessions.json"
description: |
  The `{{ table.name }}` table contains info about user web login sessions associated with your {{ integration.display_name }} instance.

replication-method: "Full Table"

api-method:
  name: "Get all web login sessions"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/user#get_all_web_login_sessions"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The user session ID."
    foreign-key-id: "user-session-id"

  - name: "browser"
    type: "string"
    description: ""

  - name: "city"
    type: "string"
    description: ""

  - name: "country"
    type: "string"
    description: ""

  - name: "created_at"
    type: "string"
    description: ""

  - name: "credentials_type"
    type: "string"
    description: ""

  - name: "expires_at"
    type: "string"
    description: ""

  - name: "extended_at"
    type: "string"
    description: ""

  - name: "extended_count"
    type: "integer"
    description: ""

  - name: "ip_address"
    type: "string"
    description: ""

  - name: "operating_system"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "sudo_user_id"
    type: "string"
    description: ""

  - name: "url"
    type: "string"
    description: ""
---