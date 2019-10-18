---
tap: "mambu"
version: "1.0"

name: "deposit_products"
doc-link: "https://api.mambu.com/?shell#welcome"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/deposit_products.json"
description: "This table contains information about deposit products."

replication-method: "Key-based Incremental"

api-method:
  name: "Get deposit products"
  doc-link: "https://support.mambu.com/docs/savings-products-api#get-savings-products"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The deposit product ID."
#    foreign-key-id: "deposit-product-id"

  - name: "last_modified_date"
    type: "date-time"
    description: "The date and time the deposit product was last modified."
    replication-key: true

  - name: "accounting_method"
    type: "string"
    description: ""

  - name: "activated"
    type: "boolean"
    description: ""

  - name: "allow_arbitrary_fees"
    type: "boolean"
    description: ""

  - name: "allow_offset"
    type: "boolean"
    description: ""

  - name: "allow_overdraft"
    type: "boolean"
    description: ""

  - name: "allow_technical_overdraft"
    type: "boolean"
    description: ""

  - name: "available_product_branches"
    type: "array"
    description: ""
    subattributes:
      - name: "encoded_key"
        type: "string"
        description: ""

      - name: "branch_key"
        type: "string"
        description: ""

  - name: "collect_interest_when_locked"
    type: "boolean"
    description: ""

  - name: "creation_date"
    type: "date-time"
    description: ""

  - name: "currencies"
    type: "array"
    description: ""
    subattributes:
      - name: "code"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "symbol"
        type: "string"
        description: ""

      - name: "digits_after_decimal"
        type: "integer"
        description: ""

      - name: "currency_symbol_position"
        type: "string"
        description: ""

      - name: "is_base_currency"
        type: "boolean"
        description: ""

      - name: "creation_date"
        type: "date-time"
        description: ""

      - name: "last_modified_date"
        type: "string"
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

  - name: "description"
    type: "string"
    description: ""

  - name: "encoded_key"
    type: "string"
    description: ""

  - name: "for_all_branches"
    type: "boolean"
    description: ""

  - name: "for_groups"
    type: "boolean"
    description: ""

  - name: "for_individuals"
    type: "boolean"
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

  - name: "interest_calculation_balance"
    type: "string"
    description: ""

  - name: "interest_days_in_year"
    type: "string"
    description: ""

  - name: "interest_paid_into_account"
    type: "boolean"
    description: ""

  - name: "interest_payment_point"
    type: "string"
    description: ""

  - name: "interest_rate_settings"
    type: "object"
    description: ""
    subattributes:
      - name: "accrue_interest_after_maturity"
        type: "boolean"
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

      - name: "interest_rate_tiers"
        type: "array"
        description: ""
        subattributes: &interest-rate-tiers
          - name: "ending_balance"
            type: "number"
            description: ""

          - name: "interest_rate"
            type: "number"
            description: ""

          - name: "encoded_key"
            type: "string"
            description: ""

          - name: "ending_day"
            type: "integer"
            description: ""

  - name: "line_of_credit_requirement"
    type: "string"
    description: ""

  - name: "maturity_period_limit"
    type: "string"
    description: ""

  - name: "max_overdraft_limit"
    type: "string"
    description: ""

  - name: "min_opening_balance"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "overdraft_days_in_year"
    type: "string"
    description: ""

  - name: "overdraft_interest_rate_settings"
    type: "object"
    description: ""
    subattributes:
      - name: "accrue_interest_after_maturity"
        type: "boolean"
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

      - name: "interest_rate_tiers"
        type: "array"
        description: ""
        subattributes: *interest-rate-tiers

  - name: "product_type"
    type: "string"
    description: ""

  - name: "savings_fees"
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

      - name: "amount_calculation_period"
        type: "string"
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

      - name: "fee_amortization_upon_reschedule_option"
        type: "string"
        description: ""

      - name: "fee_product_rules"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

  - name: "savings_product_rules"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "anything"
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

  - name: "withholding_tax_enabled"
    type: "boolean"
    description: ""
---