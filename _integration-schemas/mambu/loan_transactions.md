---
tap: "mambu"
version: "1"

name: "loan_transactions"
doc-link: "https://api.mambu.com/?shell#welcome"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/loan_transactions.json"
description: "This table contains information about Loan Transactions."

replication-method: "Key-based Incremental"

api-method:
  name: "Get all loan transactions"
  doc-link: "https://api.mambu.com/?http#loantransactions-getall"

attributes:
  - name: "encoded_key"
    type: "string"
    primary-key: true
    description: "The unique encoded key of the loan transaction."
    foreign-key-id: "loan-transaction-encoded-key"
  
  - name: "creation_date"
    type: "date-time"
    description: ""
    replication-key: true

  - name: "account_balances"
    type: "object"
    description: ""
    subattributes:
      - name: "advance_position"
        type: "number"
        description: ""

      - name: "arrears_position"
        type: "number"
        description: ""

      - name: "expected_principal_redraw"
        type: "number"
        description: ""

      - name: "principal_balance"
        type: "number"
        description: ""

      - name: "redraw_balance"
        type: "number"
        description: ""

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

  - name: "centre_key"
    type: "string"
    description: ""
    foreign-key-id: "center-encoded-key"

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

  - name: "custom_payment_amounts"
    type: "array"
    description: ""
    subattributes:
      - name: "tax_on_amount"
        type: "number"
        description: ""

      - name: "amount"
        type: "number"
        description: ""

      - name: "custom_payment_amount_type"
        type: "string"
        description: ""

  - name: "external_id"
    type: "string"
    description: ""

  - name: "fees"
    type: "array"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "amount"
        type: "number"
        description: ""

      - name: "trigger"
        type: "string"
        description: ""

      - name: "tax_amount"
        type: "number"
        description: ""

      - name: "predefined_fee_key"
        type: "string"
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

  - name: "original_amount"
    type: "number"
    description: ""

  - name: "original_currency_code"
    type: "string"
    description: ""

  - name: "original_transaction_key"
    type: "string"
    description: ""

  - name: "parent_account_key"
    type: "string"
    description: ""

  - name: "parent_loan_transaction_key"
    type: "string"
    description: ""
    # foreign-key-id: "parent-loan-key"

  - name: "taxes"
    type: "object"
    description: ""
    subattributes:
      - name: "deferred_tax_on_interest_amount"
        type: "number"
        description: ""

      - name: "tax_interest_from_arrears_amount"
        type: "number"
        description: ""

      - name: "tax_on_fees_amount"
        type: "number"
        description: ""

      - name: "tax_on_interest_amount"
        type: "number"
        description: ""

      - name: "tax_on_penalty_amount"
        type: "number"
        description: ""

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
          - name: "index_interest_rate"
            type: "number"
            description: ""

          - name: "interest_rate"
            type: "number"
            description: ""

      - name: "principal_payment_amount"
        type: "number"
        description: ""

      - name: "principal_payment_percentage"
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