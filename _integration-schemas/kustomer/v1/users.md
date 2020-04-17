---
tap: "kustomer"
version: "1"

name: "users"
doc-link: "https://dev.kustomer.com/v1/users/"
singer-schema: "https://github.com/singer-io/tap-kustomer/blob/master/tap_kustomer/schemas/users.json"
description: |
  The {{ table.name }} contains information about users in the {{ integration.name }} app.

replication-method: "Key-based Incremental"

api-method:
    name: "getUsers"
    doc-link: "https://dev.kustomer.com/v1/users/get-user"
    
attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The user ID."
    #foreign-key-id: "user-id"

  - name: "updated_at"
    type: "date-time"
    description: "The last time the user was updated."
    replication-key: true

  - name: "avatar_url"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "created_by"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
      - name: "type"
        type: "string"
        description: ""

  - name: "deleted_at"
    type: "string"
    description: ""

  - name: "display_name"
    type: "string"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "email_signature"
    type: "string"
    description: ""

  - name: "email_verified_at"
    type: "string"
    description: ""

  - name: "first_email_verified_at"
    type: "string"
    description: ""
  
  - name: "links"
    type: "object"
    description: ""
    subattributes:
      - name: "self"
        type: "string"
        description: ""

  - name: "mobile"
    type: "string"
    description: ""

  - name: "modified_at"
    type: "string"
    description: ""

  - name: "modified_by"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
      - name: "type"
        type: "string"
        description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "org"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
      - name: "type"
        type: "string"
        description: ""

  - name: "password"
    type: "object"
    description: ""
    subattributes:
      - name: "allow_new"
        type: "boolean"
        description: ""
      - name: "force_new"
        type: "boolean"
        description: ""
      - name: "updated_at"
        type: "date-time"
        description: ""

  - name: "role_groups"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "roles"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "user_type"
    type: "string"
    description: ""
---
