---
tap: "zoom"
version: "1"
key: ""

name: "users"
doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/users/users"
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/users.json"
description: |
  The `{{ table.name }}` table contains user data from your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: "getUsers"
    doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/users/users"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "Your user ID."
    foreign-key-id: "user-id"
    
  - name: "created_at"
    type: "date-time"
    description: ""
  - name: "dept"
    type: "string"
    description: ""
  - name: "email"
    type: "string"
    description: ""
  - name: "first_name"
    type: "string"
    description: ""
  - name: "group_ids"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
  
  - name: "im_group_ids"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
  - name: "last_client_version"
    type: "string"
    description: ""
  - name: "last_login_time"
    type: "date-time"
    description: ""
  - name: "last_name"
    type: "string"
    description: ""
  - name: "pmi"
    type: "integer"
    description: ""
  - name: "status"
    type: "string"
    description: ""
  - name: "timezone"
    type: "string"
    description: ""
  - name: "type"
    type: "integer"
    description: ""
  - name: "verified"
    type: "integer"
    description: ""
---
