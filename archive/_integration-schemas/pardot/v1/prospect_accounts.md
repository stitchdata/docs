---
tap: "pardot"
version: "1"
key: "prospect-account"

name: "prospect_accounts"
doc-link: "http://developer.pardot.com/kb/object-field-references/#prospect-account"
singer-schema: "https://github.com/singer-io/tap-pardot/blob/master/tap_pardot/schemas/prospect_accounts.json"
description: |
  The `{{ table.name }}` table contains info about prospect accounts.

replication-method: "Key-based Incremental"

api-method:
  name: "Query prospect accounts"
  doc-link: "http://developer.pardot.com/kb/api-version-3/prospect-accounts/"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the prospect account."
    # foreign-key-id: "prospect-account-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the prospect account was last updated."

  - name: "assigned_to"
    type: "object"
    description: "Details about who the prospect account is assigned to."
    subattributes:
      - name: "user"
        type: "object"
        description: "Details about the user assigned to the prospect account."
        subattributes:
          - name: "id"
            type: "integer"
            description: "The ID of the user."
            foreign-key-id: "user-id"

          - name: "account"
            type: "integer"
            description: ""

          - name: "created_at"
            type: "date-time"
            description: "The time the user was created."

          - name: "email"
            type: "string"
            description: "The email of the user."

          - name: "first_name"
            type: "string"
            description: "The first name of the user."

          - name: "job_tile"
            type: "string"
            description: "The job title of the user."

          - name: "last_name"
            type: "string"
            description: "The last name of the user."

          - name: "role"
            type: "string"
            description: "The role of the user."

          - name: "updated_at"
            type: "date-time"
            description: "The time the user was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the prospect account was created."

  - name: "name"
    type: "string"
    description: "The name of the prospect account."
---