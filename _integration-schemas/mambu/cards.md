---
tap: "mambu"
version: "1.0"

name: "cards"
doc-link: "https://api.mambu.com/?shell#welcome"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/cards.json"
description: |
  This table contains information about cards.
  
  **Note**: To replicate this table, the [`deposit_accounts`](#deposit_accounts) table must also be set to replicate.

replication-method: "Full Table"

api-method:
  name: "Get all cards"
    doc-link: "https://api.mambu.com/?shell#cards"

attributes:
  - name: "deposit_id"
    type: "string"
    primary-key: true
    description: "The deposit ID."
    foreign-key-id: "deposit-id"
  - name: "reference_token"
    type: "string"
    primary-key: true
    description: "The token used to externally identify the card."
#    foreign-key-id: "reference-token"
---
