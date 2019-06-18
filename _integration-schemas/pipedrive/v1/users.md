---
tap: "pipedrive"
version: "1.0"
key: "user"

name: "users"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-pipedrive/blob/master/tap_pipedrive/schemas/recents/users.json"
description: |
  The `{{ table.name }}` table contains info about the users associated with your {{ integration.display_name }} account. **Note**: This table contains info about the people with access to your {{ integration.display_name }} account - they should not be confused with [`persons`](#persons).

replication-method: "Key-based Incremental"

api-method:
  name: "Get recent users"
  doc-link: "https://developers.pipedrive.com/docs/api/v1/#!/Recents"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The user ID."
    foreign-key-id: "user-id"

  - name: "modified"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "activated"
    type: "boolean"
    description: ""

  - name: "active_flag"
    type: "boolean"
    description: ""

  - name: "created"
    type: "date-time"
    description: ""

  - name: "default_currency"
    type: "string"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "has_created_company"
    type: "boolean"
    description: ""

  - name: "icon_url"
    type: "string"
    description: ""

  - name: "is_admin"
    type: "integer"
    description: ""

  - name: "is_you"
    type: "boolean"
    description: ""

  - name: "lang"
    type: "integer"
    description: ""

  - name: "last_login"
    type: "null"
    description: ""

  - name: "locale"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "phone"
    type: "string"
    description: ""

  - name: "role_id"
    type: "integer"
    description: ""

  - name: "signup_flow_variation"
    type: "string"
    description: ""

  - name: "timezone_name"
    type: "string"
    description: ""

  - name: "timezone_offset"
    type: "string"
    description: ""
---