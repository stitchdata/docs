---
tap: "pendo"
version: "1"
key: "account"

name: "accounts"
doc-link: "https://developers.pendo.io/docs/?bash#account"
singer-schema: "https://github.com/singer-io/tap-pendo/blob/master/tap_pendo/schemas/accounts.json"
description: |
  The `{{ table.name }}` table contains info about your customer accounts in {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
  name: "Aggregation"
  doc-link: "https://api/v1/aggregation"

attributes:
  - name: "account_id"
    type: "string"
    primary-key: true
    description: "The account ID."
    foreign-key-id: "account-id"

  - name: "lastupdated"
    type: "date-time"
    replication-key: true
    description: "The time the account was last updated."

  - name: "metadata_auto"
    type: "object"
    description: ""
    subattributes:
      - name: "firstvisit"
        type: "date-time"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "idhash"
        type: "integer"
        description: ""

      - name: "lastupdated"
        type: "date-time"
        description: ""

      - name: "lastvisit"
        type: "date-time"
        description: ""

  - name: "metadata_custom"
    type: "object"
    description: ""
    # subattributes:
---