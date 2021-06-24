---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "mambu"
version: "2"
key: "card"

name: "cards"
doc-link: "https://api.mambu.com/?shell#welcome"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/cards.json"
description: |
  This table contains information about cards.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

replication-method: "Full Table"

api-method:
  name: "Get all cards (v2.0)"
  doc-link: "https://api.mambu.com/?http#depositaccounts-getallcards"

dependent-table-key: "deposit_accounts"


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "deposit_id"
    type: "string"
    primary-key: true
    description: "The deposit ID."
    # foreign-key-id: "deposit-id"

  - name: "reference_token"
    type: "string"
    primary-key: true
    description: "The token used to externally identify the card."
#    foreign-key-id: "reference-token"
---