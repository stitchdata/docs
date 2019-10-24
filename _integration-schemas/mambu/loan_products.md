---
tap: "mambu"
version: "1.0"

name: "loan_products"
doc-link: "https://api.mambu.com/?shell#welcome"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/loan_products.json"
description: "This table contains information about Loan Products."

replication-method: "Key-based Incremental"

api-method:
  name: "Get all loan products"
  doc-link: "https://support.mambu.com/docs/loan-products-api#get-loan-products"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The loan product ID."
#   foreign-key-id: "loan-product-id"
  
  - name: "last_modified_date"
    type: "date-time"
    description: "The date and time the loan product was last modified."
    replication-key: true

  - name: "account_initial_state"
    type: "string"
    description: ""

  - name: "account_linking_enabled"
    type: "boolean"
    description: ""

  - name: "accounting_method"
    type: "string"
    description: ""

  - name: "activated"
    type: "boolean"
    description: ""

  - name: "allow_arbitrary_fees"
    type: "boolean"
    description: ""

  - name: "allow_collateral"
    type: "boolean"
    description: ""

  - name: "allow_guarantors"
    type: "boolean"
    description: ""

  - name: "amortization_method"
    type: "string"
    description: ""

  - name: "apply_interest_on_prepayment_method"
    type: "string"
    description: ""

  - name: "arrears_date_calculation_method"
    type: "string"
    description: ""

  - name: "arrears_non_working_days_method"
    type: "string"
    description: ""

  - name: "arrears_tolerance_period"
    type: "integer"
    description: ""

  - name: "auto_create_linked_accounts"
    type: "boolean"
    description: ""

  - name: "auto_link_accounts"
    type: "boolean"
    description: ""

  - name: "automatically_close_dormant_accounts"
    type: "boolean"
    description: ""

  - name: "creation_date"
    type: "date-time"
    description: ""

  - name: "custom_field_values"
    type: "array"
    description: ""
    subattributes:
      - name: "encoded_key"
        type: "string"
        description: ""

      - name: "parent_key"
        type: "string"
        description: ""

      - name: "custom_field_key"
        type: "string"
        description: ""

      - name: "custom_field"
        type: "object"
        description: ""
        subattributes:
          - name: "encoded_key"
            type: "string"
            description: ""

          - name: "id"
            type: "string"
            description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "type"
            type: "string"
            description: ""

          - name: "data_type"
            type: "string" 
            description: ""

          - name: "value_length"
            type: "string"
            description: ""

          - name: "is_default"
            type: "boolean"
            description: ""

          - name: "is_required"
            type: "boolean"
            description: ""

          - name: "custom_field_set"
            type: "object"
            description: ""
            subattributes:
              - name: "encoded_key"
                type: "string"
                description: ""

              - name: "id"
                type: "string"
                description: ""

              - name: "name"
                type: "string"
                description: ""

              - name: "creation_date"
                type: "date-time"
                description: ""

              - name: "last_modified_date"
                type: "date-time"
                description: ""

              - name: "index_in_list"
                type: "integer"
                description: ""

              - name: "type"
                type: "string"
                description: ""

              - name: "usage"
                type: "string"
                description: ""

          - name: "index_in_list"
            type: "integer"
            description: ""

          - name: "state"
            type: "string"
            description: ""

          - name: "custom_field_selection_options"
            type: "array"
            description: ""
            subattributes:
              - name: "encoded_key"
                type: "string"
                description: ""

              - name: "value"
                type: "string"
                description: ""

              - name: "score"
                type: "string"
                description: ""

          - name: "view_rights"
            type: "object"
            description: ""
            subattributes:
              - name: "encoded_key"
                type: "string"
                description: ""

              - name: "is_accessible_by_all_users"
                type: "boolean"
                description: ""

              - name: "roles"
                type: "array"
                anchor-id: "1"
                description: ""
                subattributes:
                  - name: "value"
                    type: "string"
                    description: ""

          - name: "edit_rights"
            type: "object"
            description: ""
            subattributes:
              - name: "encoded_key"
                type: "string"
                description: ""

              - name: "is_accessible_by_all_users"
                type: "boolean"
                description: ""

              - name: "roles"
                type: "array"
                anchor-id: "2"
                description: ""
                subattributes:
                  - name: "value"
                    type: "string"
                    description: ""

          - name: "unique"
            type: "boolean"
            description: ""

          - name: "amounts"
            type: "object"
            description: ""

          - name: "values"
            type: "array"
            description: ""
            subattributes:
              - name: "value"
                type: "string"
                description: ""

      - name: "value"
        type: "string"
        description: ""

      - name: "amount"
        type: "string"
        description: ""

      - name: "index_in_list"
        type: "integer"
        description: ""

      - name: "custom_field_id"
        type: "string"
        description: ""

      - name: "custom_field_set_group_index"
        type: "integer"
        description: ""

  - name: "days_in_year"
    type: "string"
    description: ""

  - name: "declining_balance_prepayment_recalculation"
    type: "string"
    description: ""

  - name: "default_loan_amount"
    type: "string"
    description: ""

  - name: "default_num_installments"
    type: "integer"
    description: ""

  - name: "default_principal_repayment_interval"
    type: "integer"
    description: ""

  - name: "default_repayment_period_count"
    type: "integer"
    description: ""

  - name: "encoded_key"
    type: "string"
    description: ""

  - name: "for_hybrid_groups"
    type: "boolean"
    description: ""

  - name: "for_individuals"
    type: "boolean"
    description: ""

  - name: "for_pure_groups"
    type: "boolean"
    description: ""

  - name: "future_payments_acceptance"
    type: "string"
    description: ""

  - name: "grace_period_type"
    type: "string"
    description: ""

  - name: "id_generator_type"
    type: "string"
    description: ""

  - name: "id_pattern"
    type: "string"
    description: ""

  - name: "interest_accrued_accounting_method"
    type: "string"
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

  - name: "interest_rate_settings"
    type: "object"
    description: ""
    subattributes:
      - name: "default_interest_rate"
        type: "string"
        description: ""

      - name: "encoded_key"
        type: "string"
        description: ""

      - name: "interest_charge_frequency"
        type: "string"
        description: ""

      - name: "interest_charge_frequency_count"
        type: "integer"
        description: ""

      - name: "interest_rate_source"
        type: "string"
        description: ""

      - name: "interest_rate_terms"
        type: "string"
        description: ""

  - name: "is_investor_funds_enabled"
    type: "boolean"
    description: ""
  
  - name: "late_payments_recalculation_method"
    type: "string"
    description: ""

  - name: "line_of_credit_requirement"
    type: "string"
    description: ""

  - name: "loan_fees"
    type: "array"
    description: ""
    subattributes:
      - name: "encoded_key"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "amount"
        type: "string"
        description: ""

      - name: "amount_calculation_method"
        type: 
        description: ""

      - name: "trigger"
        type: "string"
        description: ""

      - name: "fee_application"
        type: "string"
        description: ""

      - name: "active"
        type: "boolean"
        description: ""

      - name: "creation_date"
        type: "date-time"
        description: ""

      - name: "amortization_profile"
        type: "string"
        description: ""

      - name: "amortization_interval_settings"
        type: "object"
        description: ""
        subattributes:
          - name: "encoded_key"
            type: "string"
            description: ""

          - name: "frequency"
            type: "string"
            description: ""

          - name: "period_unit"
            type: "string"
            description: ""

          - name: "period_count"
            type: "integer"
            description: ""

          - name: "interval_count"
            type: "integer"
            description: ""

      - name: "fee_product_rules"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

  - name: "loan_penalty_calculation_method"
    type: "string"
    description: ""

  - name: "loan_product_rules"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "anything"
        description: ""

  - name: "loan_product_type"
    type: "string"
    description: ""

  - name: "loan_type"
    type: "string"
    description: ""

  - name: "max_number_of_disbursement_tranches"
    type: "integer"
    description: ""

  - name: "payment_method"
    type: "string"
    description: ""

  - name: "prepayment_acceptance"
    type: "string"
    description: ""

  - name: "product_description"
    type: "string"
    description: ""

  - name: "product_name"
    type: "string"
    description: ""

  - name: "product_security_settings"
    type: "object"
    description: ""
    subattributes:
      - name: "encoded_key"
        type: "string"
        description: ""

      - name: "is_collateral_enabled"
        type: "boolean"
        description: ""

      - name: "is_guarantors_enabled"
        type: "boolean"
        description: ""

      - name: "is_investor_funds_enabled"
        type: "boolean"
        description: ""

      - name: "required_guaranties"
        type: "string"
        description: ""

  - name: "repayment_allocation_order"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "repayment_currency_rounding"
    type: "string"
    description: ""

  - name: "repayment_elements_rounding_method"
    type: "string"
    description: ""

  - name: "repayment_period_unit"
    type: "string"
    description: ""

  - name: "repayment_rescheduling_method"
    type: "string"
    description: ""

  - name: "repayment_schedule_edit_options"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "repayment_schedule_method"
    type: "string"
    description: ""

  - name: "required_guaranty_percentage"
    type: "string"
    description: ""

  - name: "rounding_repayment_schedule_method"
    type: "string"
    description: ""

  - name: "schedule_due_dates_method"
    type: "string"
    description: ""

  - name: "schedule_interest_days_count_method"
    type: "string"
    description: ""

  - name: "settlement_options"
    type: "string"
    description: ""

  - name: "taxes_on_fees_enabled"
    type: "boolean"
    description: ""

  - name: "taxes_on_interest_enabled"
    type: "boolean"
    description: ""

  - name: "taxes_on_penalty_enabled"
    type: "boolean"
    description: ""

  - name: "templates"
    type: "array"
    description: ""
    subattributes:
      - name: "type"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "creation_date"
        type: "date-time"
        description: ""

      - name: "last_modified_date"
        type: "date-time"
        description: ""

      - name: "type"
        type: "string"
        description: ""
---