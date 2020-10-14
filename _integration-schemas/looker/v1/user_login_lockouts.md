---
tap: "looker"
version: "1"
key: "user-login-lockouts"

name: "user_login_lockouts"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/user_login_lockouts.json"
description: |
  The `{{ table.name }}` table contains info about lockouts for user logins associated with your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get all user login lockouts"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/auth#get_all_user_login_lockouts"

attributes:
  - name: "key"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "user-login-lockout-key"

  - name: "auth_type"
    type: "string"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "fail_count"
    type: "integer"
    description: ""

  - name: "full_name"
    type: "string"
    description: ""

  - name: "ip"
    type: "string"
    description: ""

  - name: "lockout_at"
    type: "date-time"
    description: ""

  - name: "remote_id"
    type: "string"
    description: ""

  - name: "user_id"
    type: "string"
    description: ""
    foreign-key-id: "user-id"
---