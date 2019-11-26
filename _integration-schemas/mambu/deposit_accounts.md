---
tap: "mambu"
version: "1.0"

name: "deposit_accounts"
doc-link: "https://api.mambu.com/?shell#welcome"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/deposit_accounts.json"
description: "This table contains information about Deposit Accounts."

replication-method: "Key-based Incremental"

api-method:
  name: "Get all deposit accounts"
  doc-link: "https://api.mambu.com/?http#depositaccounts-getall"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The deposit account ID."
#   foreign-key-id: "deposit-account-id"

  - name: "last_modified_date"
    type: "date-time"
    replication-key: true
    description: "The date and time the deposit account was last modified."
    
  - name: "account_holder_key"
    type: "string"
    description: "The encoded key of the client or group."
    # foreign-key-id: "client-encoded-key"

  - name: "account_holder_type"
    type: "string"
    description: "The type of the account holder."

  - name: "account_state"
    type: "string"
    description: "The state of the deposit account."

  - name: "account_type"
    type: "string"
    description: "The type of deposit account."

  - name: "accrued_amounts"
    type: "object"
    description: "Groups all fields related to a deposit account's accrued amounts."
    subattributes:
      - name: "interest_accrued"
        type: "number"
        description: "The amount of interest that has been accrued in the account."

      - name: "overdraft_interest_accrued"
        type: "number"
        description: "The amount of overdraft interest that has been accrued in the account."

      - name: "technical_overdraft_interest_accrued"
        type: "number"
        description: "The amount of technical overdraft interest that has been accrued in the account."

  - name: "activation_date"
    type: "date-time"
    description: "The date this deposit account was activated."

  - name: "approved_date"
    type: "date-time"
    description: "The date this deposit account was approved."

  - name: "balances"
    type: "object"
    description: "Groups all fields related to a deposit account's balances."
    subattributes:
      - name: "available_balance"
        type: "number"
        description: "The current available balance for deposit transactions."

      - name: "fees_due"
        type: "number"
        description: "How much in fees is due to be paid on this account."

      - name: "hold_balance"
        type: "number"
        description: "The sum of all the authorization hold amounts on this account."

      - name: "locked_balance"
        type: "number"
        description: "No operation can modify the balance of the account and get it lower than this locked balance."

      - name: "overdraft_amount"
        type: "number"
        description: "How much money has been taken out in overdraft."

      - name: "overdraft_interest_due"
        type: "number"
        description: "How much interest is due to be paid on this account as a result of the authorized overdraft."

      - name: "technical_overdraft_amount"
        type: "number"
        description: "How much money has been taken out as unplanned overdraft."

      - name: "technical_overdraft_interest_due"
        type: "number"
        description: "How much interest is due to be paid on this account as a result of the technical overdraft."

      - name: "total_balance"
        type: "number"
        description: "The current balance of the account."
        
  - name: "closed_date"
    type: "date-time"
    description: "The date this deposit account was closed."

  - name: "creation_date"
    type: "date-time"
    description: "The date this deposit account was created."

  - name: "credit_arrangement_key"
    type: "string"
    description: "The key to the credit arrangement where this account is registered to."
    foreign-key-id: "credit-arrangement-key"

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

  - name: "encoded_key"
    type: "string"
    description: ""

  - name: "interest_settings"
    type: "object"
    description: ""
    subattributes:
      - name: "interest_payment_settings"
        type: "object"
        description: ""
        subattributes:
          - name: "interest_payment_dates"
            type: "null"
            description: ""

          - name: "interest_payment_point"
            type: "string"
            description: ""

      - name: "interest_rate_settings"
        type: "object"
        description: ""
        subattributes:
          - name: "encoded_key"
            type: "string"
            description: ""

          - name: "interest_charge_frequency"
            type: "string"
            description: ""

          - name: "interest_charge_frequency_count"
            type: "integer"
            description: ""

          - name: "interest_rate"
            type: "number"
            description: ""

          - name: "interest_rate_terms"
            type: "string"
            description: ""

          - name: "interest_rate_tiers"
            type: "null"
            description: ""

  - name: "internal_controls"
    type: "object"
    description: ""
    subattributes:
      - name: "max_withdrawal_amount"
        type: "number"
        description: ""

      - name: "recommended_deposit_amount"
        type: "number"
        description: ""

      - name: "target_amount"
        type: "number"
        description: ""

  - name: "last_account_appraisal_date"
    type: "date-time"
    description: ""

  - name: "last_interest_calculation_date"
    type: "date-time"
    description: ""

  - name: "last_interest_stored_date"
    type: "date-time"
    description: ""

  - name: "last_overdraft_interest_review_date"
    type: "date-time"
    description: ""

  - name: "last_sent_to_arrears_date"
    type: "date-time"
    description: ""

  - name: "linked_settlement_account_keys"
    type: "null"
    description: ""

  - name: "locked_date"
    type: "date-time"
    description: ""

  - name: "maturity_date"
    type: "date-time"
    description: ""

  - name: "migration_event_key"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "notes"
    type: "string"
    description: ""

  - name: "overdraft_interest_settings"
    type: "object"
    description: ""
    subattributes:
      - name: "interest_rate_settings"
        type: "object"
        description: ""
        subattributes:
          - name: "encoded_key"
            type: "string"
            description: ""

          - name: "interest_charge_frequency"
            type: "string"
            description: ""

          - name: "interest_charge_frequency_count"
            type: "integer"
            description: ""

          - name: "interest_rate"
            type: "number"
            description: ""

          - name: "interest_rate_review_count"
            type: "integer"
            description: ""

          - name: "interest_rate_review_unit"
            type: "string"
            description: ""

          - name: "interest_rate_source"
            type: "string"
            description: ""

          - name: "interest_rate_terms"
            type: "string"
            description: ""

          - name: "interest_rate_tiers"
            type: "null"
            description: ""

          - name: "interest_spread"
            type: "number"
            description: ""

  - name: "overdraft_settings"
    type: "object"
    description: ""
    subattributes:
      - name: "allowed_overdraft"
        type: "boolean"
        description: ""

      - name: "overdraft_expiry_date"
        type: "date-time"
        description: ""

      - name: "overdraft_limit"
        type: "number"
        description: ""

  - name: "product_type_key"
    type: "string"
    description: ""
    # foreign-key-id: "product-type-key"

  - name: "withholding_tax_source_key"
    type: "string"
    description: ""
---