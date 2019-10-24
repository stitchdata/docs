---
tap: "mambu"
version: "1.0"

name: "loan_accounts"
doc-link: "https://api.mambu.com/?shell#welcome"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/loan_accounts.json"
description: "This table contains information about Loan Accounts."

replication-method: "Key-based Incremental"

api-method:
  name: "Get all loan accounts"
  doc-link: "https://api.mambu.com/?http#loanaccounts-getall"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The loan account ID."
#    foreign-key-id: "loan-account-id"

  - name: "last_modified_date"
    type: "date-time"
    description: "The date and time the loan account was last modified."
    replication-key: true

  - name: "account_arrears_settings"
    type: "object"
    description: ""
    subattributes:
      - name: "date_calculation_method"
        type: "string"
        description: ""

      - name: "encoded_key"
        type: "string"
        description: ""

      - name: "monthly_tolerance_day"
        type: "integer"
        description: ""

      - name: "non_working_days_method"
        type: "string"
        description: ""

      - name: "tolerance_calculation_method"
        type: "string"
        description: ""

      - name: "tolerance_period"
        type: "integer"
        description: ""

  - name: "account_holder_key"
    type: "string"
    description: ""

  - name: "account_holder_type"
    type: "string"
    description: ""

  - name: "account_state"
    type: "string"
    description: ""

  - name: "account_sub_state"
    type: "string"
    description: ""

  - name: "accrued_interest"
    type: "number"
    description: ""

  - name: "accrued_penalty"
    type: "number"
    description: ""

  - name: "activation_transaction_key"
    type: "string"
    description: ""

  - name: "allow_offset"
    type: "boolean"
    description: ""

  - name: "approved_date"
    type: "date-time"
    description: ""

  - name: "arrears_tolerance_period"
    type: "integer"
    description: ""

  - name: "assets"
    type: "array"
    description: ""
    subattributes:
      - name: "amount"
        type: "number"
        description: ""

      - name: "depositAccountKey"
        type: "string"
        description: ""

      - name: "assetName"
        type: "string"
        description: ""

      - name: "encodedKey"
        type: "string"
        description: ""

      - name: "guarantorKey"
        type: "string"
        description: ""

      - name: "guarantorType"
        type: "string"
        description: ""
            
  - name: "assigned_branch_key"
    type: "string"
    description: ""
    foreign-key-id: "branch-encoded-key"

  - name: "assigned_centre_key"
    type: "string"
    description: ""
    foreign-key-id: "centre-encoded-key"

  - name: "assigned_user_key"
    type: "string"
    description: ""
    foreign-key-id: "user-encoded-key"

  - name: "balances"
    type: "object"
    description: ""
    subattributes:
      - name: "fees_balance"
        type: "number"
        description: ""

      - name: "fees_due"
        type: "number"
        description: ""

      - name: "fees_paid"
        type: "number"
        description: ""

      - name: "interest_balance"
        type: "number"
        description: ""

      - name: "interest_due"
        type: "number"
        description: ""

      - name: "interest_from_arrears_balance"
        type: "number"
        description: ""

      - name: "interest_from_arrears_due"
        type: "number"
        description: ""

      - name: "interest_from_arrears_paid"
        type: "number"
        description: ""

      - name: "interest_paid"
        type: "number"
        description: ""

      - name: "penalty_balance"
        type: "number"
        description: ""

      - name: "penalty_due"
        type: "number"
        description: ""

      - name: "penalty_paid"
        type: "number"
        description: ""

      - name: "principal_balance"
        type: "number"
        description: ""

      - name: "principal_due"
        type: "number"
        description: ""

      - name: "principal_paid"
        type: "number"
        description: ""

      - name: "redraw_balance"
        type: "number"
        description: ""

  - name: "closed_date"
    type: "date-time"
    description: ""

  - name: "creation_date"
    type: "date-time"
    description: ""

  - name: "credit_arrangement_key"
    type: "string"
    description: ""
    foreign-key-id: "credit-arrangement-key"

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

  - name: "days_in_arrears"
    type: "integer"
    description: ""

  - name: "days_late"
    type: "integer"
    description: ""

  - name: "disbursement_details"
    type: "object"
    description: ""
    subattributes:
      - name: "disbursement_date"
        type: "date-time"
        description: ""

      - name: "encoded_key"
        type: "string"
        description: ""

      - name: "expected_disbursement_date"
        type: "date-time"
        description: ""

      - name: "fees"
        type: "array"
        description: ""
        subattributes:
          - name: "predefined_fee_encoded_key"
            type: "string"
            description: ""

          - name: "encoded_key"
            type: "string"
            description: ""

          - name: "amount"
            type: "integer"
            description: ""

      - name: "first_repayment_date"
        type: "date-time"
        description: ""

      - name: "transaction_details"
        type: "object"
        description: ""
        subattributes:
          - name: "encoded_key"
            type: "string"
            description: ""

          - name: "internal_transfer"
            type: "boolean"
            description: ""

          - name: "target_deposit_account_key"
            type: "string"
            description: ""

          - name: "transaction_channel_id"
            type: "string"
            description: ""

          - name: "transaction_channel_key"
            type: "string"
            description: ""

  - name: "encoded_key"
    type: "string"
    description: ""

  - name: "funding_sources"
    type: "array"
    description: ""
    subattributes:
      - name: "amount"
        type: "number"
        description: ""

      - name: "interest_commission"
        type: "integer"
        description: ""

      - name: "deposit_account_key"
        type: "string"
        description: ""

      - name: "asset_name"
        type: "string"
        description: ""

      - name: "encoded_key"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "guarantor_key"
        type: "string"
        description: ""

      - name: "share_percentage"
        type: "number"
        description: ""

  - name: "future_payments_acceptance"
    type: "string"
    description: ""

  - name: "guarantors"
    type: "array"
    description: ""
    subattributes:
      - name: "amount"
        type: "number"
        description: ""

      - name: "deposit_account_key"
        type: "string"
        description: ""

      - name: "asset_name"
        type: "string"
        description: ""

      - name: "encoded_key"
        type: "string"
        description: ""

      - name: "guarantor_key"
        type: "string"
        description: ""

      - name: "guarantor_type"
        type: "string"
        description: ""

  - name: "id"
    type: "string"
    description: ""
#    foreign-key-id: "loan-account-id"

  - name: "interest_commission"
    type: "number"
    description: ""

  - name: "interest_from_arrears_accrued"
    type: "number"
    description: ""

  - name: "interest_settings"
    type: "object"
    description: ""
    subattributes:
      - name: "accrue_interest_after_maturity"
        type: "boolean"
        description: ""

      - name: "interest_application_method"
        type: "string"
        description: ""

      - name: "interest_balance_calculation_method"
        type: "string"
        description: ""

      - name: "interest_calculation_method"
        type: "string"
        description: ""

      - name: "interest_charge_frequency"
        type: "string"
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

      - name: "interest_spread"
        type: "number"
        description: ""

      - name: "interest_type"
        type: "string"
        description: ""

  - name: "last_appraisal_date"
    type: "date-time"
    description: ""

  - name: "last_interest_applied_date"
    type: "date-time"
    description: ""

  - name: "last_interest_review_date"
    type: "date-time"
    description: ""

  - name: "last_locked_date"
    type: "date-time"
    description: ""

  - name: "last_sent_to_arrears_date"
    type: "date-time"
    description: ""

  - name: "last_tax_rate_review_date"
    type: "date-time"
    description: ""

  - name: "late_payments_recalculation_method"
    type: "string"
    description: ""

  - name: "loan_amount"
    type: "number"
    description: ""

  - name: "loan_name"
    type: "string"
    description: ""

  - name: "locked_operations"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "migration_event_key"
    type: "string"
    description: ""

  - name: "notes"
    type: "string"
    description: ""

  - name: "payment_method"
    type: "string"
    description: ""

  - name: "penalty_settings"
    type: "object"
    description: ""
    subattributes:
      - name: "loan_penalty_calculation_method"
        type: "string"
        description: ""

      - name: "penalty_rate"
        type: "number"
        description: ""

  - name: "prepayment_settings"
    type: "object"
    description: ""
    subattributes:
      - name: "apply_interest_on_prepayment_method"
        type: "string"
        description: ""

      - name: "elements_recalculation_method"
        type: "string"
        description: ""

      - name: "prepayment_recalculation_method"
        type: "string"
        description: ""

      - name: "principal-paid_installment_status"
        type: "string"
        description: ""

  - name: "principal_payment_settings"
    type: "object"
    description: ""
    subattributes:
      - name: "amount"
        type: "number"
        description: ""

      - name: "encoded_key"
        type: "string"
        description: ""

      - name: "include_fees_in_floor_amount"
        type: "boolean"
        description: ""

      - name: "include_interest_in_floor_amount"
        type: "boolean"
        description: ""

      - name: "percentage"
        type: "number"
        description: ""

      - name: "principal_ceiling_value"
        type: "number"
        description: ""

      - name: "principal_floor_value"
        type: "number"
        description: ""

      - name: "principal_payment_method"
        type: "string"
        description: ""

      - name: "total_due_amount_floor"
        type: "number"
        description: ""

      - name: "total_due_payment"
        type: "string"
        description: ""

  - name: "product_type_key"
    type: "string"
    description: ""

  - name: "rescheduled_account_key"
    type: "string"
    description: ""

  - name: "schedule_settings"
    type: "object"
    description: ""
    subattributes:
      - name: "default_first_repayment_due_date_offset"
        type: "integer"
        description: ""

      - name: "fixed_days_of_month"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "integer"
            description: ""

      - name: "grace_period"
        type: "integer"
        description: ""

      - name: "grace_period_type"
        type: "string"
        description: ""

      - name: "has_custom_schedule"
        type: "boolean"
        description: ""

      - name: "payment_plan"
        type: "array"
        description: ""
        subattributes:
          - name: "to_installment"
            type: "integer"
            description: ""

          - name: "encoded_key"
            type: "string"
            description: ""

          - name: "amount"
            type: "number"
            description: ""

      - name: "periodic_payment"
        type: "number"
        description: ""

      - name: "principal_repayment_interval"
        type: "integer"
        description: ""

      - name: "repayment_installments"
        type: "integer"
        description: ""

      - name: "repayment_period_count"
        type: "integer"
        description: ""

      - name: "repayment_period_unit"
        type: "string"
        description: ""

      - name: "repayment_schedule_method"
        type: "string"
        description: ""

      - name: "schedule_due_dates_method"
        type: "string"
        description: ""

      - name: "short_month_handling_method"
        type: "string"
        description: ""

  - name: "settlement_account_key"
    type: "string"
    description: ""

  - name: "tax_rate"
    type: "number"
    description: ""

  - name: "tranches"
    type: "array"
    description: ""
    subattributes:
      - name: "encoded_key"
        type: "string"
        description: ""

      - name: "amount"
        type: "number"
        description: ""

      - name: "tranch_number"
        type: "string"
        description: ""

      - name: "disbursement_details"
        type: "object"
        description: ""
        subattributes:
          - name: "expected_disbursement_date"
            type: "date-time"
            description: ""

          - name: "disbursement_transaction_key"
            type: "string"
            description: ""
---