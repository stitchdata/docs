---
tap: "ms-teams"
version: "1"
key: "user"

name: "users"
doc-link: "hhttps://docs.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-beta"
singer-schema: "https://github.com/singer-io/tap-ms-teams/blob/master/tap_ms_teams/schemas/users.json"
description: |
  The `{{ table.name }}` table contains information about users in your Microsoft account.

replication-method: "Full Table"

api-method:
    name: "List users"
    doc-link: "https://docs.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0&tabs=http"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The user ID."
    foreign-key-id: "user-id"

  - name: "business_phones"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "display_name"
    type: "string"
    description: ""

  - name: "given_name"
    type: "string"
    description: ""

  - name: "job_title"
    type: "string"
    description: ""

  - name: "mail"
    type: "string"
    description: ""

  - name: "mobile_phone"
    type: "string"
    description: ""

  - name: "office_location"
    type: "string"
    description: ""

  - name: "preferred_language"
    type: "string"
    description: ""

  - name: "surname"
    type: "string"
    description: ""

  - name: "user_principal_name"
    type: "string"
    description: ""
---