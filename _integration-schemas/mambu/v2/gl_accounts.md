---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "mambu"
version: "2"
key: "gl-account"

name: "gl_accounts"
doc-link: "https://support.mambu.com/docs/gl-accounts-api"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/gl_accounts.json"
description: |
  This table contains information about general ledger accounts.


# -------------------------- #
#    Replication Details     #
# -------------------------- #
api-method:
  name: "Get GL accounts (v1.0)"
  doc-link: "https://api.mambu.com/v1/#general-ledger-accounts-get-all-gl-accounts"

replication-method: "Key-based Incremental"


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "gl_code"
    type: "string"
    primary-key: true
    description: "The unique general ledger code."
    foreign-key-id: "gl-account-code"

  - name: "last_modified_date"
    type: "date-time"
    replication-key: true
    description: "The time the GL account was last modified."

  - name: "activated"
    type: "boolean"
    description: ""
    
  - name: "allow_manual_journal_entries"
    type: "boolean"
    description: ""

  - name: "balance"
    type: "string"
    description: ""

  - name: "creation_date"
    type: "date-time"
    description: ""

  - name: "currency"
    type: "object"
    description: ""
    subattributes:
      - name: "code"
        type: "string"
        description: ""

      - name: "currency_symbol_position"
        type: "string"
        description: ""

      - name: "digits_after_decimal"
        type: "integer"
        description: ""

      - name: "is_base_currency"
        type: "boolean"
        description: ""

      - name: "last_modified_date"
        type: "date-time"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "symbol"
        type: "string"
        description: ""

  - name: "encoded_key"
    type: "string"
    description: ""

  - name: "entry_id"
    type: "string"
    description: ""
  
  - name: "name"
    type: "string"
    description: ""

  - name: "strip_trailing_zeros"
    type: "boolean"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "usage"
    type: "string"
    description: ""
---