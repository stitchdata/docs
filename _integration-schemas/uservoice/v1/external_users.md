---
tap: "uservoice"
# version: "1.0"

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

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the external user was last updated."

  - name: "email"
    type: "string"
    description: "The email address associated with the user."

  - name: "external_id"
    type: "string"
    description: "The external ID associated with the user."

  - name: "ip"
    type: "string"
    description: "The external user's IP address."

  - name: "links"
    type: "object"
    description: "Details about the external accounts and users the user is associated with."
    object-attributes: 
      - name: "external_accounts"
        type: "integer"
        description: "The external ID of the account associated with the user."

      - name: "external_users"
        type: "integer"
        description: "The external ID of the user associated with the user."

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