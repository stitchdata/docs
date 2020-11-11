---
tap: "chargify"
version: "1"
key: "subscription"

name: "subscriptions"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-chargify/blob/master/tap_chargify/schemas/subscriptions.json"
description: |
  The `{{ table.name }}` table contains info about the subscriptions in your {{ integration.display_name }} instance.

replication-method: "Key-based Incremental"

api-method:
  name: "Read subscriptions for a site"
  doc-link: "https://reference.chargify.com/v1/subscriptions/list-subscriptions"
  
attributes:
  - name: "id"
    type: "number"
    primary-key: true
    description: ""
    foreign-key-id: "subscription-id"

  - name: "activated_at"
    type: "date-time"
    description: ""

  - name: "balance_in_cents"
    type: "number"
    description: ""

  - name: "cancel_at_end_of_period"
    type: "boolean"
    description: ""

  - name: "canceled_at"
    type: "date-time"
    description: ""

  - name: "cancellation_message"
    type: "string"
    description: ""

  - name: "cancellation_method"
    type: "string"
    description: ""

  - name: "coupon_codes"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "credit_card"
    type: "object"
    description: ""
    subattributes:
      - name: "billing_address"
        type: "string"
        description: ""

      - name: "billing_address_2"
        type: "string"
        description: ""

      - name: "billing_city"
        type: "string"
        description: ""

      - name: "billing_country"
        type: "string"
        description: ""

      - name: "billing_state"
        type: "string"
        description: ""

      - name: "billing_zip"
        type: "string"
        description: ""

      - name: "card_type"
        type: "string"
        description: ""

      - name: "current_vault"
        type: "string"
        description: ""

      - name: "customer_id"
        type: "number"
        description: ""
        foreign-key-id: "customer-id"

      - name: "customer_vault_token"
        type: "string"
        description: ""

      - name: "expiration_month"
        type: "number"
        description: ""

      - name: "expiration_year"
        type: "number"
        description: ""

      - name: "first_name"
        type: "string"
        description: ""

      - name: "id"
        type: "number"
        description: ""

      - name: "last_name"
        type: "string"
        description: ""

      - name: "masked_card_number"
        type: "string"
        description: ""

      - name: "payment_type"
        type: "string"
        description: ""

      - name: "vault_token"
        type: "string"
        description: ""

  - name: "current_period_ends_at"
    type: "date-time"
    description: ""

  - name: "current_period_started_at"
    type: "date-time"
    description: ""

  - name: "customer"
    type: "object"
    description: ""
    subattributes:
      - name: "address"
        type: "string"
        description: ""

      - name: "address_2"
        type: "string"
        description: ""

      - name: "cc_emails"
        type: "string"
        description: ""

      - name: "city"
        type: "string"
        description: ""

      - name: "country"
        type: "string"
        description: ""

      - name: "created_at"
        type: "date-time"
        description: ""

      - name: "email"
        type: "string"
        description: ""

      - name: "first_name"
        type: "string"
        description: ""

      - name: "id"
        type: "number"
        description: ""
        foreign-key-id: "customer-id"

      - name: "last_name"
        type: "string"
        description: ""

      - name: "organization"
        type: "string"
        description: ""

      - name: "phone"
        type: "string"
        description: ""

      - name: "portal_customer_created_at"
        type: "date-time"
        description: ""

      - name: "portal_invite_last_accepted_at"
        type: "number"
        description: ""

      - name: "portal_invite_last_sent_at"
        type: "date-time"
        description: ""

      - name: "reference"
        type: "number"
        description: ""

      - name: "state"
        type: "string"
        description: ""

      - name: "tax_exempt"
        type: "boolean"
        description: ""

      - name: "updated_at"
        type: "date-time"
        description: ""

      - name: "vat_number"
        type: "string"
        description: ""

      - name: "verified"
        type: "boolean"
        description: ""

      - name: "zip"
        type: "string"
        description: ""

  - name: "delayed_cancel_at"
    type: "date-time"
    description: ""

  - name: "expires_at"
    type: "date-time"
    description: ""

  - name: "net_terms"
    type: "number"
    description: ""

  - name: "next_assessment_at"
    type: "date-time"
    description: ""

  - name: "next_product_id"
    type: "number"
    description: ""
    foreign-key-id: "product-id"

  - name: "payment_collection_method"
    type: "string"
    description: ""

  - name: "payment_type"
    type: "string"
    description: ""

  - name: "previous_state"
    type: "string"
    description: ""

  - name: "product"
    type: "object"
    description: ""
    subattributes:
      - name: "accounting_code"
        type: "string"
        description: ""

      - name: "archived_at"
        type: "date-time"
        description: ""

      - name: "created_at"
        type: "date-time"
        description: ""

      - name: "description"
        type: "string"
        description: ""

      - name: "expiration_interval"
        type: "number"
        description: ""

      - name: "expiration_interval_unit"
        type: "string"
        description: ""

      - name: "handle"
        type: "string"
        description: ""

      - name: "id"
        type: "number"
        description: ""
        foreign-key-id: "product-id"

      - name: "initial_charge_after_trial"
        type: "boolean"
        description: ""

      - name: "initial_charge_in_cents"
        type: "number"
        description: ""

      - name: "interval"
        type: "number"
        description: ""

      - name: "interval_unit"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "price_in_cents"
        type: "number"
        description: ""

      - name: "product_family"
        type: "object"
        description: ""
        subattributes:
          - name: "accounting_code"
            type: "number"
            description: ""

          - name: "description"
            type: "string"
            description: ""

          - name: "handle"
            type: "string"
            description: ""

          - name: "id"
            type: "number"
            description: ""
            foreign-key-id: "product-family-id"

          - name: "name"
            type: "string"
            description: ""

      - name: "public_signup_pages"
        type: "array"
        description: ""
        subattributes:
          - name: "id"
            type: "number"
            description: ""

          - name: "url"
            type: "string"
            description: ""

      - name: "request_credit_card"
        type: "boolean"
        description: ""

      - name: "require_credit_card"
        type: "boolean"
        description: ""

      - name: "return_params"
        type: "string"
        description: ""

      - name: "taxable"
        type: "boolean"
        description: ""

      - name: "trial_interval"
        type: "number"
        description: ""

      - name: "trial_interval_unit"
        type: "string"
        description: ""

      - name: "trial_price_in_cents"
        type: "number"
        description: ""

      - name: "update_return_params"
        type: "string"
        description: ""

      - name: "update_return_url"
        type: "string"
        description: ""

      - name: "updated_at"
        type: "date-time"
        description: ""

      - name: "version_number"
        type: "number"
        description: ""

  - name: "product_price_in_cents"
    type: "number"
    description: ""

  - name: "product_version_number"
    type: "number"
    description: ""

  - name: "reason_code"
    type: "string"
    description: ""

  - name: "receives_invoice_emails"
    type: "boolean"
    description: ""

  - name: "referral_code"
    type: "string"
    description: ""

  - name: "signup_payment_id"
    type: "number"
    description: ""
    foreign-key-id: "transaction-id"

  - name: "signup_revenue"
    type: "number"
    description: ""

  - name: "snap_day"
    type: "number"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "stored_credential_transaction_id"
    type: "number"
    description: ""
    foreign-key-id: "transaction-id"

  - name: "total_revenue_in_cents"
    type: "number"
    description: ""

  - name: "trial_ended_at"
    type: "date-time"
    description: ""

  - name: "trial_started_at"
    type: "date-time"
    description: ""

  - name: "updated_at"
    type: "date-time"
    description: ""
---