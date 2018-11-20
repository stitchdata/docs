---
tap: "stripe"
version: "1.0"

name: "customers"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-stripe/blob/master/tap_stripe/schemas/customers.json"
description: |
  The `{{ table.name }}` table contains info about

replication-method: ""

api-method:
    name: ""
    doc-link: ""

## HOLD OFF ON THIS ONE - IT'S A MESS 
attributes:
  - name: "account_balance"
    type: "integer"
    description: ""

  - name: "cards"
    type: "array"
    description: ""

    array-attributes:
      - name: "address_city"
        type: "string"
        description: ""

      - name: "address_country"
        type: "string"
        description: ""

      - name: "address_line1"
        type: "string"
        description: ""

      - name: "address_line1_check"
        type: "string"
        description: ""

      - name: "address_line2"
        type: "string"
        description: ""

      - name: "address_state"
        type: "string"
        description: ""

      - name: "address_zip"
        type: "string"
        description: ""

      - name: "address_zip_check"
        type: "string"
        description: ""

      - name: "brand"
        type: "string"
        description: ""

      - name: "country"
        type: "string"
        description: ""

      - name: "customer"
        type: "string"
        description: ""

      - name: "cvc_check"
        type: "string"
        description: ""

      - name: "dynamic_last4"
        type: "string"
        description: ""

      - name: "exp_month"
        type: "integer"
        description: ""

      - name: "exp_year"
        type: "integer"
        description: ""

      - name: "fingerprint"
        type: "string"
        description: ""

      - name: "funding"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "last4"
        type: "string"
        description: ""

      - name: "metadata"
        type: "object"
        description: ""

        object-attributes:

            

      - name: "name"
        type: "string"
        description: ""

      - name: "object"
        type: "string"
        description: ""

      - name: "tokenization_method"
        type: "string"
        description: ""

  - name: "created"
    type: "date-time"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "default_card"
    type: "string"
    description: ""

  - name: "default_source"
    type: "string"
    description: ""

  - name: "delinquent"
    type: "boolean"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "discount"
    type: "object"
    description: ""

    object-attributes:

      - name: "coupon"
        type: "object"
        description: ""

        object-attributes:

          - name: "amount_off"
            type: "integer"
            description: ""

          - name: "created"
            type: "date-time"
            description: ""

          - name: "currency"
            type: "string"
            description: ""

          - name: "duration"
            type: "string"
            description: ""

          - name: "duration_in_months"
            type: "integer"
            description: ""

          - name: "id"
            type: "string"
            description: ""

          - name: "livemode"
            type: "boolean"
            description: ""

          - name: "max_redemptions"
            type: "integer"
            description: ""

          - name: "metadata"
            type: "object"
            description: ""

            object-attributes:

          - name: "name"
            type: "string"
            description: ""

          - name: "object"
            type: "string"
            description: ""

          - name: "percent_off"
            type: "integer"
            description: ""

          - name: "percent_off_precise"
            type: "number"
            description: ""

          - name: "redeem_by"
            type: "date-time"
            description: ""

          - name: "times_redeemed"
            type: "integer"
            description: ""

          - name: "valid"
            type: "boolean"
            description: ""

      - name: "customer"
        type: "string"
        description: ""

      - name: "end"
        type: "date-time"
        description: ""

      - name: "object"
        type: "string"
        description: ""

      - name: "start"
        type: "date-time"
        description: ""

      - name: "subscription"
        type: "string"
        description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "id"
    type: "string"
    description: ""

  - name: "invoice_prefix"
    type: "string"
    description: ""

  - name: "livemode"
    type: "boolean"
    description: ""

  - name: "metadata"
    type: "object"
    description: ""

    object-attributes:

  - name: "object"
    type: "string"
    description: ""

  - name: "shipping"
    type: "object"
    description: ""

    object-attributes:

      - name: "address"
        type: "object"
        description: ""

        object-attributes:

          - name: "city"
            type: "string"
            description: ""

          - name: "country"
            type: "string"
            description: ""

          - name: "line1"
            type: "string"
            description: ""

          - name: "line2"
            type: "string"
            description: ""

          - name: "postal_code"
            type: "string"
            description: ""

          - name: "state"
            type: "string"
            description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "phone"
        type: "string"
        description: ""

  - name: "sources"
    type: "array"
    description: ""

    array-attributes:
      - name: "ach_credit_transfer"
        type: "object"
        description: ""

        object-attributes:

          - name: "account_number"
            type: "string"
            description: ""

          - name: "bank_name"
            type: "string"
            description: ""

          - name: "fingerprint"
            type: "string"
            description: ""

          - name: "refund_account_holder_name"
            type: "string"
            description: ""

          - name: "refund_account_holder_type"
            type: "string"
            description: ""

          - name: "refund_account_number"
            type: "string"
            description: ""

          - name: "refund_routing_number"
            type: "string"
            description: ""

          - name: "routing_number"
            type: "string"
            description: ""

          - name: "swift_code"
            type: "string"
            description: ""

      - name: "address_city"
        type: "string"
        description: ""

      - name: "address_country"
        type: "string"
        description: ""

      - name: "address_line1"
        type: "string"
        description: ""

      - name: "address_line1_check"
        type: "string"
        description: ""

      - name: "address_line2"
        type: "string"
        description: ""

      - name: "address_state"
        type: "string"
        description: ""

      - name: "address_zip"
        type: "string"
        description: ""

      - name: "address_zip_check"
        type: "string"
        description: ""

      - name: "alipay"
        type: "object"
        description: ""

        object-attributes:

      - name: "amount"
        type: "integer"
        description: ""

      - name: "bancontact"
        type: "object"
        description: ""

        object-attributes:

      - name: "brand"
        type: "string"
        description: ""

      - name: "card"
        type: "object"
        description: ""

        object-attributes:

          - name: "address_line1_check"
            type: "string"
            description: ""

          - name: "address_zip_check"
            type: "string"
            description: ""

          - name: "brand"
            type: "string"
            description: ""

          - name: "country"
            type: "string"
            description: ""

          - name: "cvc_check"
            type: "string"
            description: ""

          - name: "dynamic_last4"
            type: "string"
            description: ""

          - name: "exp_month"
            type: "integer"
            description: ""

          - name: "exp_year"
            type: "integer"
            description: ""

          - name: "fingerprint"
            type: "string"
            description: ""

          - name: "funding"
            type: "string"
            description: ""

          - name: "last4"
            type: "string"
            description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "three_d_secure"
            type: "string"
            description: ""

          - name: "tokenization_method"
            type: "string"
            description: ""

      - name: "client_secret"
        type: "string"
        description: ""

      - name: "country"
        type: "string"
        description: ""

      - name: "created"
        type: "date-time"
        description: ""

      - name: "currency"
        type: "string"
        description: ""

      - name: "customer"
        type: "string"
        description: ""

      - name: "cvc_check"
        type: "string"
        description: ""

      - name: "dynamic_last4"
        type: "string"
        description: ""

      - name: "eps"
        type: "object"
        description: ""

        object-attributes:

      - name: "exp_month"
        type: "integer"
        description: ""

      - name: "exp_year"
        type: "integer"
        description: ""

      - name: "fingerprint"
        type: "string"
        description: ""

      - name: "flow"
        type: "string"
        description: ""

      - name: "funding"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "ideal"
        type: "object"
        description: ""

        object-attributes:

      - name: "last4"
        type: "string"
        description: ""

      - name: "livemode"
        type: "boolean"
        description: ""

      - name: "metadata"
        type: "object"
        description: ""

        object-attributes:

      - name: "multibanco"
        type: "object"
        description: ""

        object-attributes:

      - name: "name"
        type: "string"
        description: ""

      - name: "object"
        type: "string"
        description: ""

      - name: "owner"
        type: "object"
        description: ""

        object-attributes:

          - name: "address"
            type: "object"
            description: ""

            object-attributes:

              - name: "city"
                type: "string"
                description: ""

              - name: "country"
                type: "string"
                description: ""

              - name: "line1"
                type: "string"
                description: ""

              - name: "line2"
                type: "string"
                description: ""

              - name: "postal_code"
                type: "string"
                description: ""

              - name: "state"
                type: "string"
                description: ""

          - name: "email"
            type: "string"
            description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "phone"
            type: "string"
            description: ""

          - name: "verified_address"
            type: "string"
            description: ""

          - name: "verified_email"
            type: "string"
            description: ""

          - name: "verified_name"
            type: "string"
            description: ""

          - name: "verified_phone"
            type: "string"
            description: ""

      - name: "receiver"
        type: "object"
        description: ""

        object-attributes:

          - name: "address"
            type: "string"
            description: ""

          - name: "amount_charged"
            type: "integer"
            description: ""

          - name: "amount_received"
            type: "integer"
            description: ""

          - name: "amount_returned"
            type: "integer"
            description: ""

          - name: "refund_attributes_method"
            type: "string"
            description: ""

          - name: "refund_attributes_status"
            type: "string"
            description: ""

      - name: "redirect"
        type: "object"
        description: ""

        object-attributes:

          - name: "failure_reason"
            type: "string"
            description: ""

          - name: "return_url"
            type: "string"
            description: ""

          - name: "status"
            type: "string"
            description: ""

          - name: "url"
            type: "string"
            description: ""

      - name: "statement_descriptor"
        type: "string"
        description: ""

      - name: "status"
        type: "string"
        description: ""

      - name: "tokenization_method"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "usage"
        type: "string"
        description: ""

  - name: "subscriptions"
    type: "array"
    description: ""

    array-attributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "tax_info"
    type: "string"
    description: ""

  - name: "tax_info_verification"
    type: "string"
    description: ""

  - name: "updated"
    type: "date-time"
    description: ""

---
