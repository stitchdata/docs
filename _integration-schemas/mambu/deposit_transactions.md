---
tap: "mambu"
version: "1.0"

name: "deposit_transactions"
doc-link: "https://api.mambu.com/?shell#welcome"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/deposit_transactions.json"
description: "This table contains information about Deposit Transactions."

replication-method: "Key-based Incremental"

api-method:
  name: "Search deposit transactions"
  doc-link: "https://api.mambu.com/?http#deposittransactions-search"

attributes:
  - name: "encoded_key"
    type: "string"
    primary-key: true
    description: "The unique encoded key of the deposit transaction."
#    foreign-key-id: "deposit-transaction-encoded-key"  

  - name: "creation_date"
    type: "date-time"
    description: "The date when the deposit transaction was created."
    replication-key: true

  - name: "account_balances"
    type: "object"
    description: ""
    subattributes:
      - name: "total_balance"
        type: "number"
        description: ""

  - name: "adjustment_transaction_key"
    type: "string"
    description: ""

  - name: "affected_amounts"
    type: "object"
    description: ""
    subattributes:
      - name: "fees_amount"
        type: "number"
        description: ""

      - name: "fraction_amount"
        type: "number"
        description: ""

      - name: "funds_amount"
        type: "number"
        description: ""

      - name: "interest_amount"
        type: "number"
        description: ""

      - name: "overdraft_amount"
        type: "number"
        description: ""

      - name: "overdraft_fees_amount"
        type: "number"
        description: ""

      - name: "overdraft_interest_amount"
        type: "number"
        description: ""

      - name: "technical_overdraft_amount"
        type: "number"
        description: ""

      - name: "technical_overdraft_interest_amount"
        type: "number"
        description: ""

  - name: "amount"
    type: "number"
    description: ""

  - name: "booking_date"
    type: "date-time"
    description: ""

  - name: "branch_key"
    type: "string"
    description: ""
    foreign-key-id: "branch-encoded-key"

  - name: "card_transaction"
    type: "object"
    description: ""
    subattributes:
      - name: "advice"
        type: "boolean"
        description: ""

      - name: "amount"
        type: "number"
        description: ""

      - name: "card_acceptor"
        type: "object"
        description: ""
        subattributes:
          - name: "city"
            type: "string"
            description: ""

          - name: "country"
            type: "string"
            description: ""

          - name: "mcc"
            type: "integer"
            description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "state"
            type: "string"
            description: ""

          - name: "zip"
            type: "string"
            description: ""

      - name: "card_token"
        type: "string"
        description: ""

      - name: "currency_code"
        type: "string"
        description: ""

      - name: "encoded_key"
        type: "string"
        description: ""

      - name: "external_authorization_reference_id"
        type: "string"
        description: ""

      - name: "external_reference_id"
        type: "string"
        description: ""

      - name: "user_transaction_time"
        type: "string"
        description: ""

  - name: "centre_key"
    type: "string"
    description: ""
    foreign-key-id: "center-encoded-key"

  - name: "currency_code"
    type: "string"
    description: ""

  - name: "custom_field_sets"
    type: "array"
    description: ""
    subattributes:
      - name: "custom_field_set_id"
        type: "string"
        description: ""
        foreign-key-id: "custom-field-set-id"

      - name: "custom_field_values"
        type: "array"
        description: ""
        subattributes:
          - name: "custom_field_id"
            type: "string"
            description: ""
            foreign-key-id: "custom-field-id"

          - name: "custom_field_value"
            type: "string"
            description: ""

  - name: "external_id"
    type: "string"
    description: ""

  - name: "fees"
    type: "null"
    description: ""

  - name: "id"
    type: "string"
    description: ""

  - name: "linked_loan_transaction_key"
    type: "string"
    description: ""
    foreign-key-id: "linked-loan-transaction-key"

  - name: "migration_event_key"
    type: "string"
    description: ""

  - name: "notes"
    type: "string"
    description: ""

  - name: "original_transaction_key"
    type: "string"
    description: ""

  - name: "parent_account_key"
    type: "string"
    description: ""

  - name: "taxes"
    type: "object"
    description: ""
    subattributes:
      - name: "tax_rate"
        type: "number"
        description: ""

  - name: "terms"
    type: "object"
    description: ""
    subattributes:
      - name: "interest_settings"
        type: "object"
        description: ""
        subattributes:
          - name: "interest_rate"
            type: "number"
            description: ""

      - name: "overdraft_interest_settings"
        type: "object"
        description: ""
        subattributes:
          - name: "index_interest_rate"
            type: "number"
            description: ""

          - name: "interest_rate"
            type: "number"
            description: ""

      - name: "overdraft_settings"
        type: "object"
        description: ""
        subattributes:
          - name: "overdraft_limit"
            type: "number"
            description: ""

  - name: "till_key"
    type: "string"
    description: ""

  - name: "transaction_details"
    type: "object"
    description: ""
    subattributes:
      - name: "transaction_channel_id"
        type: "string"
        description: ""

      - name: "transaction_channel_key"
        type: "string"
        description: ""

  - name: "transfer_details"
    type: "object"
    description: ""
    subattributes:
      - name: "linked_deposit_transaction_key"
        type: "string"
        description: ""
        foreign-key-id: "linked-deposit-transaction-key"

      - name: "linked_loan_transaction_key"
        type: "string"
        description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "user_key"
    type: "string"
    description: ""
    foreign-key-id: "user-encoded-key"

  - name: "value_date"
    type: "date-time"
    description: ""
---