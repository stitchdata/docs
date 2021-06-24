---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "mambu"
version: "2"
key: "gl-journal-entry"

name: "gl_journal_entries"
doc-link: "https://support.mambu.com/docs/gl-journal-entries-api"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/gl_journal_entries.json"
description: |
  This table contains information about general ledger entries.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "Search GL journal entries (v1.0)"
  doc-link: "https://api.mambu.com/v1/#gl-journal-entries-search-for-gl-journal-entries"

replication-method: "Key-based Incremental"


# -------------------------- #
#       Table Attributes     #
# -------------------------- #
    
attributes:
  - name: "entry_id"
    type: "string"
    primary-key: true
    description: "The GL journal entry ID."
    #foreign-key-id: "gl-journal-entry"

  - name: "booking_date"
    type: "date-time"
    replication-key: true
    description: "The journal entry booking date."  

  - name: "account_key"
    type: "string"
    description: ""

  - name: "amount"
    type: "singer.decimal"
    description: ""
  
  - name: "creation_date"
    type: "date-time"
    description: ""

  - name: "encoded_key"
    type: "string"
    description: ""

  - name: "entry_date"
    type: "date-time"
    description: ""
  
  - name: "gl_account"
    type: "object"
    description: ""
    subattributes:
      - name: "activated"
        type: "boolean"
        description: ""

      - name: "allow_manual_journal_entries"
        type: "boolean"
        description: ""

      - name: "balance"
        type: "singer.decimal"
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

      - name: "gl_code"
        type: "string"
        description: ""
        foreign-key-id: "gl-account-code"

      - name: "last_modified_date"
        type: "date-time"
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

  - name: "product_key"
    type: "string"
    description: ""
    
  - name: "transaction_id"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "user_key"
    type: "string"
    description: ""
    foreign-key-id: "user-key"
---