---
tap: "uservoice"
version: "1"

name: "external_users"
doc-link: https://developer.uservoice.com/docs/api/v2/reference/#/ExternalUser
singer-schema: https://github.com/singer-io/tap-uservoice/blob/master/tap_uservoice/streams/external_users.py
description: |
  The `{{ table.name }}` table contains info about users from external systems.

replication-method: "Key-based Incremental"

api-method:
  name: List external users
  doc-link: https://developer.uservoice.com/docs/api/v2/reference/#list-external-users

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The external user's ID in {{ integration.display_name }}."
    foreign-key-id: "external-user-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the external user was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the external user was created in {{ integration.display_name }}."

  - name: "email"
    type: "string"
    description: "The email address associated with the external user."

  - name: "external_id"
    type: "string"
    description: "The ID of the user in the external system."

  - name: "ip"
    type: "string"
    description: "The external user's IP address."

  - name: "links"
    type: "object"
    description: "Details about the external accounts and users the user is associated with."
    subattributes: 
      - name: "external_accounts"
        type: "integer"
        description: "The ID of the external account associated with the user."
        foreign-key-id: "external-account-id"

      - name: "external_users"
        type: "integer"
        description: "The ID of the external user associated with the user."

  - name: "name"
    type: "string"
    description: "The external user's name."

  - name: "seen_days"
    type: "integer"
    description: "The number of days the user has been seen."

  - name: "type"
    type: "string"
    description: "The type of the user."
---