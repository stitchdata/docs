---
tap: "stripe"
version: "2"
key: ""

name: "payment_intents"
doc-link: "https://stripe.com/docs/payments/payment-intents"
singer-schema: https://github.com/singer-io/tap-stripe/tree/master/tap_stripe/schemas/payment_intents.json
description: |
  This table contains information about payments, from creation through checkout, in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List all payment intents"
    doc-link: "https://stripe.com/docs/api/payment_intents/list"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The payment intent ID."
    foreign-key-id: "payment-intent-id"

  - name: "created"
    type: "string"
    description: "Time at which the dispute was created. Measured in seconds since the Unix epoch."
    replication-key: true 

  - name: "amount"
    type: "integer"
    description: ""

  - name: "amount_capturable"
    type: "integer"
    description: ""

  - name: "amount_received"
    type: "integer"
    description: ""

  - name: "application"
    type: "string"
    description: ""

  - name: "application_fee_amount"
    type: "integer"
    description: ""

  - name: "automatic_payment_methods"
    type: "object"
    description: ""
    subattributes:
    - name: "enabled"
      type: "boolean"
      description: ""


  - name: "canceled_at"
    type: "string"
    description: ""

  - name: "cancellation_reason"
    type: "string"
    description: ""

  - name: "capture_method"
    type: "string"
    description: ""

  - name: "charges"
    type: "array"
    description: ""
    subattributes:
    - name: "metadata"
      type: "object"
      description: ""
      subattributes:

    - name: "fraud_details"
      type: "object"
      description: ""
      subattributes:
      - name: "stripe_report"
        type: "string"
        description: ""


    - name: "transfer_group"
      type: "string"
      description: ""

    - name: "on_behalf_of"
      type: "string"
      description: ""

    - name: "review"
      type: "string"
      description: ""

    - name: "failure_message"
      type: "string"
      description: ""

    - name: "receipt_email"
      type: "string"
      description: ""

    - name: "application_fee_amount"
      type: "integer"
      description: ""

    - name: "disputed"
      type: "boolean"
      description: ""

    - name: "payment_method"
      type: "string"
      description: ""

    - name: "billing_details"
      type: "object"
      description: ""
      subattributes:
      - name: "address"
        type: "object"
        description: ""
        subattributes:
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


    - name: "statement_descriptor_suffix"
      type: "string"
      description: ""

    - name: "transfer_data"
      type: "object"
      description: ""
      subattributes:
      - name: "amount"
        type: "integer"
        description: ""

      - name: "destination"
        type: "string"
        description: ""


    - name: "receipt_url"
      type: "string"
      description: ""

    - name: "statement_descriptor"
      type: "string"
      description: ""

    - name: "source"
      type: "object"
      description: ""
      subattributes:
      - name: "metadata"
        type: "object"
        description: ""
        subattributes:

      - name: "type"
        type: "string"
        description: ""

      - name: "address_zip"
        type: "string"
        description: ""

      - name: "livemode"
        type: "boolean"
        description: ""

      - name: "card"
        type: "object"
        description: ""
        subattributes:
        - name: "fingerprint"
          type: "string"
          description: ""

        - name: "last4"
          type: "string"
          description: ""

        - name: "dynamic_last4"
          type: "string"
          description: ""

        - name: "address_line1_check"
          type: "string"
          description: ""

        - name: "exp_month"
          type: "integer"
          description: ""

        - name: "tokenization_method"
          type: "string"
          description: ""

        - name: "name"
          type: "string"
          description: ""

        - name: "exp_year"
          type: "integer"
          description: ""

        - name: "three_d_secure"
          type: "string"
          description: ""

        - name: "funding"
          type: "string"
          description: ""

        - name: "brand"
          type: "string"
          description: ""

        - name: "cvc_check"
          type: "string"
          description: ""

        - name: "country"
          type: "string"
          description: ""

        - name: "address_zip_check"
          type: "string"
          description: ""

        - name: "type"
          type: "string"
          description: ""


      - name: "statement_descriptor"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "address_country"
        type: "string"
        description: ""

      - name: "funding"
        type: "string"
        description: ""

      - name: "dynamic_last4"
        type: "string"
        description: ""

      - name: "exp_year"
        type: "integer"
        description: ""

      - name: "last4"
        type: "string"
        description: ""

      - name: "exp_month"
        type: "integer"
        description: ""

      - name: "brand"
        type: "string"
        description: ""

      - name: "address_line2"
        type: "string"
        description: ""

      - name: "country"
        type: "string"
        description: ""

      - name: "object"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""

      - name: "cvc_check"
        type: "string"
        description: ""

      - name: "usage"
        type: "string"
        description: ""

      - name: "address_line1"
        type: "string"
        description: ""

      - name: "owner"
        type: "object"
        description: ""
        subattributes:
        - name: "verified_address"
          type: "string"
          description: ""

        - name: "email"
          type: "string"
          description: ""

        - name: "address"
          type: "object"
          description: ""
          subattributes:
          - name: "line2"
            type: "string"
            description: ""

          - name: "state"
            type: "string"
            description: ""

          - name: "city"
            type: "string"
            description: ""

          - name: "postal_code"
            type: "string"
            description: ""

          - name: "country"
            type: "string"
            description: ""

          - name: "line1"
            type: "string"
            description: ""


        - name: "verified_email"
          type: "string"
          description: ""

        - name: "name"
          type: "string"
          description: ""

        - name: "phone"
          type: "string"
          description: ""

        - name: "verified_name"
          type: "string"
          description: ""

        - name: "verified_phone"
          type: "string"
          description: ""


      - name: "tokenization_method"
        type: "string"
        description: ""

      - name: "client_secret"
        type: "string"
        description: ""

      - name: "fingerprint"
        type: "string"
        description: ""

      - name: "address_city"
        type: "string"
        description: ""

      - name: "currency"
        type: "string"
        description: ""

      - name: "address_line1_check"
        type: "string"
        description: ""

      - name: "receiver"
        type: "object"
        description: ""
        subattributes:
        - name: "refund_attributes_method"
          type: "string"
          description: ""

        - name: "amount_returned"
          type: "integer"
          description: ""

        - name: "amount_received"
          type: "integer"
          description: ""

        - name: "refund_attributes_status"
          type: "string"
          description: ""

        - name: "address"
          type: "string"
          description: ""

        - name: "amount_charged"
          type: "integer"
          description: ""


      - name: "flow"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "ach_credit_transfer"
        type: "object"
        description: ""
        subattributes:
        - name: "bank_name"
          type: "string"
          description: ""

        - name: "fingerprint"
          type: "string"
          description: ""

        - name: "routing_number"
          type: "string"
          description: ""

        - name: "swift_code"
          type: "string"
          description: ""

        - name: "refund_account_holder_type"
          type: "string"
          description: ""

        - name: "refund_account_holder_name"
          type: "string"
          description: ""

        - name: "refund_account_number"
          type: "string"
          description: ""

        - name: "refund_routing_number"
          type: "string"
          description: ""

        - name: "account_number"
          type: "string"
          description: ""


      - name: "customer"
        type: "string"
        description: ""

      - name: "address_zip_check"
        type: "string"
        description: ""

      - name: "status"
        type: "string"
        description: ""

      - name: "created"
        type: "string"
        description: ""

      - name: "address_state"
        type: "string"
        description: ""

      - name: "alipay"
        type: "object"
        description: ""
        subattributes:

      - name: "bancontact"
        type: "object"
        description: ""
        subattributes:

      - name: "eps"
        type: "object"
        description: ""
        subattributes:

      - name: "ideal"
        type: "object"
        description: ""
        subattributes:

      - name: "multibanco"
        type: "object"
        description: ""
        subattributes:

      - name: "redirect"
        type: "object"
        description: ""
        subattributes:
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



    - name: "destination"
      type: "string"
      description: ""

    - name: "id"
      type: "string"
      description: ""

    - name: "object"
      type: "string"
      description: ""

    - name: "outcome"
      type: "object"
      description: ""
      subattributes:
      - name: "type"
        type: "string"
        description: ""

      - name: "seller_message"
        type: "string"
        description: ""

      - name: "reason"
        type: "string"
        description: ""

      - name: "risk_level"
        type: "string"
        description: ""

      - name: "network_status"
        type: "string"
        description: ""

      - name: "risk_score"
        type: "integer"
        description: ""


    - name: "status"
      type: "string"
      description: ""

    - name: "currency"
      type: "string"
      description: ""

    - name: "created"
      type: "string"
      description: ""

    - name: "order"
      type: "string"
      description: ""

    - name: "application"
      type: "string"
      description: ""

    - name: "refunded"
      type: "boolean"
      description: ""

    - name: "receipt_number"
      type: "string"
      description: ""

    - name: "livemode"
      type: "boolean"
      description: ""

    - name: "captured"
      type: "boolean"
      description: ""

    - name: "paid"
      type: "boolean"
      description: ""

    - name: "shipping"
      type: "object"
      description: ""
      subattributes:

    - name: "calculated_statement_descriptor"
      type: "string"
      description: ""

    - name: "invoice"
      type: "string"
      description: ""

    - name: "amount_captured"
      type: "integer"
      description: ""

    - name: "amount"
      type: "integer"
      description: ""

    - name: "customer"
      type: "string"
      description: ""

    - name: "payment_intent"
      type: "string"
      description: ""

    - name: "source_transfer"
      type: "string"
      description: ""

    - name: "statement_description"
      type: "string"
      description: ""

    - name: "refunds"
      type: "array"
      description: ""
      subattributes:
      - name: "items"
        type: ""
        description: ""

    - name: "application_fee"
      type: "string"
      description: ""

    - name: "card"
      type: "object"
      description: ""
      subattributes:
      - name: "metadata"
        type: "object"
        description: ""
        subattributes:

      - name: "exp_month"
        type: "integer"
        description: ""

      - name: "address_state"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "object"
        type: "string"
        description: ""

      - name: "address_line1_check"
        type: "string"
        description: ""

      - name: "address_line1"
        type: "string"
        description: ""

      - name: "exp_year"
        type: "integer"
        description: ""

      - name: "tokenization_method"
        type: "string"
        description: ""

      - name: "address_country"
        type: "string"
        description: ""

      - name: "fingerprint"
        type: "string"
        description: ""

      - name: "address_city"
        type: "string"
        description: ""

      - name: "last4"
        type: "string"
        description: ""

      - name: "address_line2"
        type: "string"
        description: ""

      - name: "customer"
        type: "string"
        description: ""

      - name: "brand"
        type: "string"
        description: ""

      - name: "country"
        type: "string"
        description: ""

      - name: "dynamic_last4"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "funding"
        type: "string"
        description: ""

      - name: "address_zip"
        type: "string"
        description: ""

      - name: "address_zip_check"
        type: "string"
        description: ""

      - name: "cvc_check"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""


    - name: "payment_method_details"
      type: "object"
      description: ""
      subattributes:
      - name: "card_present"
        type: "object"
        description: ""
        subattributes:
        - name: "amount_authorized"
          type: "integer"
          description: ""

        - name: "brand"
          type: "string"
          description: ""

        - name: "cardholder_name"
          type: "string"
          description: ""

        - name: "country"
          type: "string"
          description: ""

        - name: "emv_auth_data"
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

        - name: "generated_card"
          type: "string"
          description: ""

        - name: "last4"
          type: "string"
          description: ""

        - name: "network"
          type: "string"
          description: ""

        - name: "overcapture_supported"
          type: "boolean"
          description: ""

        - name: "read_method"
          type: "string"
          description: ""

        - name: "receipt"
          type: "object"
          description: ""
          subattributes:
          - name: "account_type"
            type: "string"
            description: ""

          - name: "application_cryptogram"
            type: "string"
            description: ""

          - name: "application_preferred_name"
            type: "string"
            description: ""

          - name: "authorization_code"
            type: "string"
            description: ""

          - name: "authorization_response_code"
            type: "string"
            description: ""

          - name: "cardholder_verification_method"
            type: "string"
            description: ""

          - name: "dedicated_file_name"
            type: "string"
            description: ""

          - name: "terminal_verification_results"
            type: "string"
            description: ""

          - name: "transaction_status_information"
            type: "string"
            description: ""



      - name: "ach_credit_transfer"
        type: "object"
        description: ""
        subattributes:
        - name: "account_number"
          type: "string"
          description: ""

        - name: "bank_name"
          type: "string"
          description: ""

        - name: "routing_number"
          type: "string"
          description: ""

        - name: "swift_code"
          type: "string"
          description: ""


      - name: "ach_debit"
        type: "object"
        description: ""
        subattributes:
        - name: "account_holder_type"
          type: "string"
          description: ""

        - name: "bank_name"
          type: "string"
          description: ""

        - name: "country"
          type: "string"
          description: ""

        - name: "fingerprint"
          type: "string"
          description: ""

        - name: "last4"
          type: "string"
          description: ""

        - name: "routing_number"
          type: "string"
          description: ""


      - name: "alipay"
        type: "object"
        description: ""

      - name: "bancontact"
        type: "object"
        description: ""
        subattributes:
        - name: "bank_code"
          type: "string"
          description: ""

        - name: "bank_name"
          type: "string"
          description: ""

        - name: "bic"
          type: "string"
          description: ""

        - name: "iban_last4"
          type: "string"
          description: ""

        - name: "preferred_language"
          type: "string"
          description: ""

        - name: "verified_name"
          type: "string"
          description: ""


      - name: "card"
        type: "object"
        description: ""
        subattributes:
        - name: "brand"
          type: "string"
          description: ""

        - name: "checks"
          type: "object"
          description: ""
          subattributes:
          - name: "address_line1_check"
            type: "string"
            description: ""

          - name: "address_postal_code_check"
            type: "string"
            description: ""

          - name: "cvc_check"
            type: "string"
            description: ""


        - name: "country"
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

        - name: "installments"
          type: "object"
          description: ""
          subattributes:
          - name: "plan"
            type: "object"
            description: ""
            subattributes:
            - name: "count"
              type: "integer"
              description: ""

            - name: "interval"
              type: "string"
              description: ""

            - name: "type"
              type: "string"
              description: ""



        - name: "last4"
          type: "string"
          description: ""

        - name: "network"
          type: "string"
          description: ""

        - name: "three_d_secure"
          type: "object"
          description: ""
          subattributes:
          - name: "authenticated"
            type: "boolean"
            description: ""

          - name: "succeeded"
            type: "boolean"
            description: ""

          - name: "version"
            type: "string"
            description: ""


        - name: "wallet"
          type: "object"
          description: ""
          subattributes:
          - name: "amex_express_checkout"
            type: "object"
            description: ""
            subattributes:

          - name: "apple_pay"
            type: "object"
            description: ""
            subattributes:

          - name: "dynamic_last4"
            type: "string"
            description: ""

          - name: "google_pay"
            type: "object"
            description: ""
            subattributes:

          - name: "masterpass"
            type: "object"
            description: ""
            subattributes:
            - name: "billing_address"
              type: "object"
              description: ""
              subattributes:
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

            - name: "shipping_address"
              type: "object"
              description: ""
              subattributes:
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



          - name: "samsung_pay"
            type: "object"
            description: ""
            subattributes:

          - name: "type"
            type: "string"
            description: ""

          - name: "visa_checkout"
            type: "object"
            description: ""
            subattributes:
            - name: "billing_address"
              type: "object"
              description: ""
              subattributes:
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

            - name: "shipping_address"
              type: "object"
              description: ""
              subattributes:
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




        - name: "card_present"
          type: "object"
          description: ""
          subattributes:
          - name: "brand"
            type: "string"
            description: ""

          - name: "country"
            type: "string"
            description: ""

          - name: "emv_auth_data"
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

          - name: "generated_card"
            type: "string"
            description: ""

          - name: "last4"
            type: "string"
            description: ""

          - name: "network"
            type: "string"
            description: ""

          - name: "read_method"
            type: "string"
            description: ""

          - name: "receipt"
            type: "object"
            description: ""
            subattributes:
            - name: "application_cryptogram"
              type: "string"
              description: ""

            - name: "application_preferred_name"
              type: "string"
              description: ""

            - name: "authorization_code"
              type: "string"
              description: ""

            - name: "authorization_response_code"
              type: "string"
              description: ""

            - name: "cardholder_verification_method"
              type: "string"
              description: ""

            - name: "dedicated_file_name"
              type: "string"
              description: ""

            - name: "terminal_verification_results"
              type: "string"
              description: ""

            - name: "transaction_status_information"
              type: "string"
              description: ""



        - name: "eps"
          type: "object"
          description: ""
          subattributes:
          - name: "verified_name"
            type: "string"
            description: ""


        - name: "giropay"
          type: "object"
          description: ""
          subattributes:
          - name: "bank_code"
            type: "string"
            description: ""

          - name: "bank_name"
            type: "string"
            description: ""

          - name: "bic"
            type: "string"
            description: ""

          - name: "verified_name"
            type: "string"
            description: ""


        - name: "ideal"
          type: "object"
          description: ""
          subattributes:
          - name: "bank"
            type: "string"
            description: ""

          - name: "bic"
            type: "string"
            description: ""

          - name: "iban_last4"
            type: "string"
            description: ""

          - name: "verified_name"
            type: "string"
            description: ""


        - name: "klarna"
          type: "object"
          description: ""
          subattributes:

        - name: "multibanco"
          type: "object"
          description: ""
          subattributes:
          - name: "entity"
            type: "string"
            description: ""

          - name: "reference"
            type: "string"
            description: ""


        - name: "p24"
          type: "object"
          description: ""
          subattributes:
          - name: "reference"
            type: "string"
            description: ""

          - name: "verified_name"
            type: "string"
            description: ""


        - name: "sepa_debit"
          type: "object"
          description: ""
          subattributes:
          - name: "bank_code"
            type: "string"
            description: ""

          - name: "branch_code"
            type: "string"
            description: ""

          - name: "country"
            type: "string"
            description: ""

          - name: "fingerprint"
            type: "string"
            description: ""

          - name: "last4"
            type: "string"
            description: ""

          - name: "mandate"
            type: "string"
            description: ""


        - name: "sofort"
          type: "object"
          description: ""
          subattributes:
          - name: "bank_code"
            type: "string"
            description: ""

          - name: "bank_name"
            type: "string"
            description: ""

          - name: "bic"
            type: "string"
            description: ""

          - name: "country"
            type: "string"
            description: ""

          - name: "iban_last4"
            type: "string"
            description: ""

          - name: "verified_name"
            type: "string"
            description: ""


        - name: "stripe_account"
          type: "object"
          description: ""
          subattributes:

        - name: "type"
          type: "string"
          description: ""

        - name: "wechat"
          type: "object"
          description: ""
          subattributes:

        - name: "metadata"
          type: "object"
          description: ""
          subattributes:

        - name: "address_state"
          type: "string"
          description: ""

        - name: "id"
          type: "string"
          description: ""

        - name: "object"
          type: "string"
          description: ""

        - name: "address_line1_check"
          type: "string"
          description: ""

        - name: "address_line1"
          type: "string"
          description: ""

        - name: "tokenization_method"
          type: "string"
          description: ""

        - name: "address_country"
          type: "string"
          description: ""

        - name: "address_city"
          type: "string"
          description: ""

        - name: "address_line2"
          type: "string"
          description: ""

        - name: "customer"
          type: "string"
          description: ""

        - name: "dynamic_last4"
          type: "string"
          description: ""

        - name: "name"
          type: "string"
          description: ""

        - name: "address_zip"
          type: "string"
          description: ""

        - name: "address_zip_check"
          type: "string"
          description: ""

        - name: "cvc_check"
          type: "string"
          description: ""


      - name: "type"
        type: "string"
        description: ""


    - name: "balance_transaction"
      type: "string"
      description: ""

    - name: "amount_refunded"
      type: "integer"
      description: ""

    - name: "failure_code"
      type: "string"
      description: ""

    - name: "dispute"
      type: "string"
      description: ""

    - name: "description"
      type: "string"
      description: ""

    - name: "updated"
      type: "string"
      description: ""

    - name: "updated_by_event_type"
      type: "string"
      description: "Description of the event"



  - name: "charges"
    type: "object"
    description: ""
    subattributes:
    - name: "metadata"
      type: "object"
      description: ""
      subattributes:

    - name: "fraud_details"
      type: "object"
      description: ""
      subattributes:
      - name: "stripe_report"
        type: "string"
        description: ""


    - name: "transfer_group"
      type: "string"
      description: ""

    - name: "on_behalf_of"
      type: "string"
      description: ""

    - name: "review"
      type: "string"
      description: ""

    - name: "failure_message"
      type: "string"
      description: ""

    - name: "receipt_email"
      type: "string"
      description: ""

    - name: "application_fee_amount"
      type: "integer"
      description: ""

    - name: "disputed"
      type: "boolean"
      description: ""

    - name: "payment_method"
      type: "string"
      description: ""

    - name: "billing_details"
      type: "object"
      description: ""
      subattributes:
      - name: "address"
        type: "object"
        description: ""
        subattributes:
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


    - name: "statement_descriptor_suffix"
      type: "string"
      description: ""

    - name: "transfer_data"
      type: "object"
      description: ""
      subattributes:
      - name: "amount"
        type: "integer"
        description: ""

      - name: "destination"
        type: "string"
        description: ""


    - name: "receipt_url"
      type: "string"
      description: ""

    - name: "statement_descriptor"
      type: "string"
      description: ""

    - name: "source"
      type: "object"
      description: ""
      subattributes:
      - name: "metadata"
        type: "object"
        description: ""
        subattributes:

      - name: "type"
        type: "string"
        description: ""

      - name: "address_zip"
        type: "string"
        description: ""

      - name: "livemode"
        type: "boolean"
        description: ""

      - name: "card"
        type: "object"
        description: ""
        subattributes:
        - name: "fingerprint"
          type: "string"
          description: ""

        - name: "last4"
          type: "string"
          description: ""

        - name: "dynamic_last4"
          type: "string"
          description: ""

        - name: "address_line1_check"
          type: "string"
          description: ""

        - name: "exp_month"
          type: "integer"
          description: ""

        - name: "tokenization_method"
          type: "string"
          description: ""

        - name: "name"
          type: "string"
          description: ""

        - name: "exp_year"
          type: "integer"
          description: ""

        - name: "three_d_secure"
          type: "string"
          description: ""

        - name: "funding"
          type: "string"
          description: ""

        - name: "brand"
          type: "string"
          description: ""

        - name: "cvc_check"
          type: "string"
          description: ""

        - name: "country"
          type: "string"
          description: ""

        - name: "address_zip_check"
          type: "string"
          description: ""

        - name: "type"
          type: "string"
          description: ""


      - name: "statement_descriptor"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "address_country"
        type: "string"
        description: ""

      - name: "funding"
        type: "string"
        description: ""

      - name: "dynamic_last4"
        type: "string"
        description: ""

      - name: "exp_year"
        type: "integer"
        description: ""

      - name: "last4"
        type: "string"
        description: ""

      - name: "exp_month"
        type: "integer"
        description: ""

      - name: "brand"
        type: "string"
        description: ""

      - name: "address_line2"
        type: "string"
        description: ""

      - name: "country"
        type: "string"
        description: ""

      - name: "object"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""

      - name: "cvc_check"
        type: "string"
        description: ""

      - name: "usage"
        type: "string"
        description: ""

      - name: "address_line1"
        type: "string"
        description: ""

      - name: "owner"
        type: "object"
        description: ""
        subattributes:
        - name: "verified_address"
          type: "string"
          description: ""

        - name: "email"
          type: "string"
          description: ""

        - name: "address"
          type: "object"
          description: ""
          subattributes:
          - name: "line2"
            type: "string"
            description: ""

          - name: "state"
            type: "string"
            description: ""

          - name: "city"
            type: "string"
            description: ""

          - name: "postal_code"
            type: "string"
            description: ""

          - name: "country"
            type: "string"
            description: ""

          - name: "line1"
            type: "string"
            description: ""


        - name: "verified_email"
          type: "string"
          description: ""

        - name: "name"
          type: "string"
          description: ""

        - name: "phone"
          type: "string"
          description: ""

        - name: "verified_name"
          type: "string"
          description: ""

        - name: "verified_phone"
          type: "string"
          description: ""


      - name: "tokenization_method"
        type: "string"
        description: ""

      - name: "client_secret"
        type: "string"
        description: ""

      - name: "fingerprint"
        type: "string"
        description: ""

      - name: "address_city"
        type: "string"
        description: ""

      - name: "currency"
        type: "string"
        description: ""

      - name: "address_line1_check"
        type: "string"
        description: ""

      - name: "receiver"
        type: "object"
        description: ""
        subattributes:
        - name: "refund_attributes_method"
          type: "string"
          description: ""

        - name: "amount_returned"
          type: "integer"
          description: ""

        - name: "amount_received"
          type: "integer"
          description: ""

        - name: "refund_attributes_status"
          type: "string"
          description: ""

        - name: "address"
          type: "string"
          description: ""

        - name: "amount_charged"
          type: "integer"
          description: ""


      - name: "flow"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "ach_credit_transfer"
        type: "object"
        description: ""
        subattributes:
        - name: "bank_name"
          type: "string"
          description: ""

        - name: "fingerprint"
          type: "string"
          description: ""

        - name: "routing_number"
          type: "string"
          description: ""

        - name: "swift_code"
          type: "string"
          description: ""

        - name: "refund_account_holder_type"
          type: "string"
          description: ""

        - name: "refund_account_holder_name"
          type: "string"
          description: ""

        - name: "refund_account_number"
          type: "string"
          description: ""

        - name: "refund_routing_number"
          type: "string"
          description: ""

        - name: "account_number"
          type: "string"
          description: ""


      - name: "customer"
        type: "string"
        description: ""

      - name: "address_zip_check"
        type: "string"
        description: ""

      - name: "status"
        type: "string"
        description: ""

      - name: "created"
        type: "string"
        description: ""

      - name: "address_state"
        type: "string"
        description: ""

      - name: "alipay"
        type: "object"
        description: ""
        subattributes:

      - name: "bancontact"
        type: "object"
        description: ""
        subattributes:

      - name: "eps"
        type: "object"
        description: ""
        subattributes:

      - name: "ideal"
        type: "object"
        description: ""
        subattributes:

      - name: "multibanco"
        type: "object"
        description: ""
        subattributes:

      - name: "redirect"
        type: "object"
        description: ""
        subattributes:
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



    - name: "destination"
      type: "string"
      description: ""

    - name: "id"
      type: "string"
      description: ""

    - name: "object"
      type: "string"
      description: ""

    - name: "outcome"
      type: "object"
      description: ""
      subattributes:
      - name: "type"
        type: "string"
        description: ""

      - name: "seller_message"
        type: "string"
        description: ""

      - name: "reason"
        type: "string"
        description: ""

      - name: "risk_level"
        type: "string"
        description: ""

      - name: "network_status"
        type: "string"
        description: ""

      - name: "risk_score"
        type: "integer"
        description: ""


    - name: "status"
      type: "string"
      description: ""

    - name: "currency"
      type: "string"
      description: ""

    - name: "created"
      type: "string"
      description: ""

    - name: "order"
      type: "string"
      description: ""

    - name: "application"
      type: "string"
      description: ""

    - name: "refunded"
      type: "boolean"
      description: ""

    - name: "receipt_number"
      type: "string"
      description: ""

    - name: "livemode"
      type: "boolean"
      description: ""

    - name: "captured"
      type: "boolean"
      description: ""

    - name: "paid"
      type: "boolean"
      description: ""

    - name: "shipping"
      type: "object"
      description: ""
      subattributes:

    - name: "calculated_statement_descriptor"
      type: "string"
      description: ""

    - name: "invoice"
      type: "string"
      description: ""

    - name: "amount_captured"
      type: "integer"
      description: ""

    - name: "amount"
      type: "integer"
      description: ""

    - name: "customer"
      type: "string"
      description: ""

    - name: "payment_intent"
      type: "string"
      description: ""

    - name: "source_transfer"
      type: "string"
      description: ""

    - name: "statement_description"
      type: "string"
      description: ""

    - name: "refunds"
      type: "array"
      description: ""
      subattributes:
      - name: "items"
        type: ""
        description: ""

    - name: "application_fee"
      type: "string"
      description: ""

    - name: "card"
      type: "object"
      description: ""
      subattributes:
      - name: "metadata"
        type: "object"
        description: ""
        subattributes:

      - name: "exp_month"
        type: "integer"
        description: ""

      - name: "address_state"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "object"
        type: "string"
        description: ""

      - name: "address_line1_check"
        type: "string"
        description: ""

      - name: "address_line1"
        type: "string"
        description: ""

      - name: "exp_year"
        type: "integer"
        description: ""

      - name: "tokenization_method"
        type: "string"
        description: ""

      - name: "address_country"
        type: "string"
        description: ""

      - name: "fingerprint"
        type: "string"
        description: ""

      - name: "address_city"
        type: "string"
        description: ""

      - name: "last4"
        type: "string"
        description: ""

      - name: "address_line2"
        type: "string"
        description: ""

      - name: "customer"
        type: "string"
        description: ""

      - name: "brand"
        type: "string"
        description: ""

      - name: "country"
        type: "string"
        description: ""

      - name: "dynamic_last4"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "funding"
        type: "string"
        description: ""

      - name: "address_zip"
        type: "string"
        description: ""

      - name: "address_zip_check"
        type: "string"
        description: ""

      - name: "cvc_check"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""


    - name: "payment_method_details"
      type: "object"
      description: ""
      subattributes:
      - name: "card_present"
        type: "object"
        description: ""
        subattributes:
        - name: "amount_authorized"
          type: "integer"
          description: ""

        - name: "brand"
          type: "string"
          description: ""

        - name: "cardholder_name"
          type: "string"
          description: ""

        - name: "country"
          type: "string"
          description: ""

        - name: "emv_auth_data"
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

        - name: "generated_card"
          type: "string"
          description: ""

        - name: "last4"
          type: "string"
          description: ""

        - name: "network"
          type: "string"
          description: ""

        - name: "overcapture_supported"
          type: "boolean"
          description: ""

        - name: "read_method"
          type: "string"
          description: ""

        - name: "receipt"
          type: "object"
          description: ""
          subattributes:
          - name: "account_type"
            type: "string"
            description: ""

          - name: "application_cryptogram"
            type: "string"
            description: ""

          - name: "application_preferred_name"
            type: "string"
            description: ""

          - name: "authorization_code"
            type: "string"
            description: ""

          - name: "authorization_response_code"
            type: "string"
            description: ""

          - name: "cardholder_verification_method"
            type: "string"
            description: ""

          - name: "dedicated_file_name"
            type: "string"
            description: ""

          - name: "terminal_verification_results"
            type: "string"
            description: ""

          - name: "transaction_status_information"
            type: "string"
            description: ""



      - name: "ach_credit_transfer"
        type: "object"
        description: ""
        subattributes:
        - name: "account_number"
          type: "string"
          description: ""

        - name: "bank_name"
          type: "string"
          description: ""

        - name: "routing_number"
          type: "string"
          description: ""

        - name: "swift_code"
          type: "string"
          description: ""


      - name: "ach_debit"
        type: "object"
        description: ""
        subattributes:
        - name: "account_holder_type"
          type: "string"
          description: ""

        - name: "bank_name"
          type: "string"
          description: ""

        - name: "country"
          type: "string"
          description: ""

        - name: "fingerprint"
          type: "string"
          description: ""

        - name: "last4"
          type: "string"
          description: ""

        - name: "routing_number"
          type: "string"
          description: ""


      - name: "alipay"
        type: "object"
        description: ""

      - name: "bancontact"
        type: "object"
        description: ""
        subattributes:
        - name: "bank_code"
          type: "string"
          description: ""

        - name: "bank_name"
          type: "string"
          description: ""

        - name: "bic"
          type: "string"
          description: ""

        - name: "iban_last4"
          type: "string"
          description: ""

        - name: "preferred_language"
          type: "string"
          description: ""

        - name: "verified_name"
          type: "string"
          description: ""


      - name: "card"
        type: "object"
        description: ""
        subattributes:
        - name: "brand"
          type: "string"
          description: ""

        - name: "checks"
          type: "object"
          description: ""
          subattributes:
          - name: "address_line1_check"
            type: "string"
            description: ""

          - name: "address_postal_code_check"
            type: "string"
            description: ""

          - name: "cvc_check"
            type: "string"
            description: ""


        - name: "country"
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

        - name: "installments"
          type: "object"
          description: ""
          subattributes:
          - name: "plan"
            type: "object"
            description: ""
            subattributes:
            - name: "count"
              type: "integer"
              description: ""

            - name: "interval"
              type: "string"
              description: ""

            - name: "type"
              type: "string"
              description: ""



        - name: "last4"
          type: "string"
          description: ""

        - name: "network"
          type: "string"
          description: ""

        - name: "three_d_secure"
          type: "object"
          description: ""
          subattributes:
          - name: "authenticated"
            type: "boolean"
            description: ""

          - name: "succeeded"
            type: "boolean"
            description: ""

          - name: "version"
            type: "string"
            description: ""


        - name: "wallet"
          type: "object"
          description: ""
          subattributes:
          - name: "amex_express_checkout"
            type: "object"
            description: ""
            subattributes:

          - name: "apple_pay"
            type: "object"
            description: ""
            subattributes:

          - name: "dynamic_last4"
            type: "string"
            description: ""

          - name: "google_pay"
            type: "object"
            description: ""
            subattributes:

          - name: "masterpass"
            type: "object"
            description: ""
            subattributes:
            - name: "billing_address"
              type: "object"
              description: ""
              subattributes:
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

            - name: "shipping_address"
              type: "object"
              description: ""
              subattributes:
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



          - name: "samsung_pay"
            type: "object"
            description: ""
            subattributes:

          - name: "type"
            type: "string"
            description: ""

          - name: "visa_checkout"
            type: "object"
            description: ""
            subattributes:
            - name: "billing_address"
              type: "object"
              description: ""
              subattributes:
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

            - name: "shipping_address"
              type: "object"
              description: ""
              subattributes:
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




        - name: "card_present"
          type: "object"
          description: ""
          subattributes:
          - name: "brand"
            type: "string"
            description: ""

          - name: "country"
            type: "string"
            description: ""

          - name: "emv_auth_data"
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

          - name: "generated_card"
            type: "string"
            description: ""

          - name: "last4"
            type: "string"
            description: ""

          - name: "network"
            type: "string"
            description: ""

          - name: "read_method"
            type: "string"
            description: ""

          - name: "receipt"
            type: "object"
            description: ""
            subattributes:
            - name: "application_cryptogram"
              type: "string"
              description: ""

            - name: "application_preferred_name"
              type: "string"
              description: ""

            - name: "authorization_code"
              type: "string"
              description: ""

            - name: "authorization_response_code"
              type: "string"
              description: ""

            - name: "cardholder_verification_method"
              type: "string"
              description: ""

            - name: "dedicated_file_name"
              type: "string"
              description: ""

            - name: "terminal_verification_results"
              type: "string"
              description: ""

            - name: "transaction_status_information"
              type: "string"
              description: ""



        - name: "eps"
          type: "object"
          description: ""
          subattributes:
          - name: "verified_name"
            type: "string"
            description: ""


        - name: "giropay"
          type: "object"
          description: ""
          subattributes:
          - name: "bank_code"
            type: "string"
            description: ""

          - name: "bank_name"
            type: "string"
            description: ""

          - name: "bic"
            type: "string"
            description: ""

          - name: "verified_name"
            type: "string"
            description: ""


        - name: "ideal"
          type: "object"
          description: ""
          subattributes:
          - name: "bank"
            type: "string"
            description: ""

          - name: "bic"
            type: "string"
            description: ""

          - name: "iban_last4"
            type: "string"
            description: ""

          - name: "verified_name"
            type: "string"
            description: ""


        - name: "klarna"
          type: "object"
          description: ""
          subattributes:

        - name: "multibanco"
          type: "object"
          description: ""
          subattributes:
          - name: "entity"
            type: "string"
            description: ""

          - name: "reference"
            type: "string"
            description: ""


        - name: "p24"
          type: "object"
          description: ""
          subattributes:
          - name: "reference"
            type: "string"
            description: ""

          - name: "verified_name"
            type: "string"
            description: ""


        - name: "sepa_debit"
          type: "object"
          description: ""
          subattributes:
          - name: "bank_code"
            type: "string"
            description: ""

          - name: "branch_code"
            type: "string"
            description: ""

          - name: "country"
            type: "string"
            description: ""

          - name: "fingerprint"
            type: "string"
            description: ""

          - name: "last4"
            type: "string"
            description: ""

          - name: "mandate"
            type: "string"
            description: ""


        - name: "sofort"
          type: "object"
          description: ""
          subattributes:
          - name: "bank_code"
            type: "string"
            description: ""

          - name: "bank_name"
            type: "string"
            description: ""

          - name: "bic"
            type: "string"
            description: ""

          - name: "country"
            type: "string"
            description: ""

          - name: "iban_last4"
            type: "string"
            description: ""

          - name: "verified_name"
            type: "string"
            description: ""


        - name: "stripe_account"
          type: "object"
          description: ""
          subattributes:

        - name: "type"
          type: "string"
          description: ""

        - name: "wechat"
          type: "object"
          description: ""
          subattributes:

        - name: "metadata"
          type: "object"
          description: ""
          subattributes:

        - name: "address_state"
          type: "string"
          description: ""

        - name: "id"
          type: "string"
          description: ""

        - name: "object"
          type: "string"
          description: ""

        - name: "address_line1_check"
          type: "string"
          description: ""

        - name: "address_line1"
          type: "string"
          description: ""

        - name: "tokenization_method"
          type: "string"
          description: ""

        - name: "address_country"
          type: "string"
          description: ""

        - name: "address_city"
          type: "string"
          description: ""

        - name: "address_line2"
          type: "string"
          description: ""

        - name: "customer"
          type: "string"
          description: ""

        - name: "dynamic_last4"
          type: "string"
          description: ""

        - name: "name"
          type: "string"
          description: ""

        - name: "address_zip"
          type: "string"
          description: ""

        - name: "address_zip_check"
          type: "string"
          description: ""

        - name: "cvc_check"
          type: "string"
          description: ""


      - name: "type"
        type: "string"
        description: ""


    - name: "balance_transaction"
      type: "string"
      description: ""

    - name: "amount_refunded"
      type: "integer"
      description: ""

    - name: "failure_code"
      type: "string"
      description: ""

    - name: "dispute"
      type: "string"
      description: ""

    - name: "description"
      type: "string"
      description: ""

    - name: "updated"
      type: "string"
      description: ""

    - name: "updated_by_event_type"
      type: "string"
      description: "Description of the event"



  - name: "client_secret"
    type: "string"
    description: ""

  - name: "confirmation_method"
    type: "string"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "customer"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "invoice"
    type: "string"
    description: ""

  - name: "last_payment_error"
    type: "object"
    description: ""
    subattributes:
    - name: "charge"
      type: "string"
      description: ""

    - name: "code"
      type: "string"
      description: ""

    - name: "decline_code"
      type: "string"
      description: ""

    - name: "doc_url"
      type: "string"
      description: ""

    - name: "message"
      type: "string"
      description: ""

    - name: "param"
      type: "string"
      description: ""

    - name: "payment_method_type"
      type: "string"
      description: ""

    - name: "type"
      type: "string"
      description: ""


  - name: "livemode"
    type: "boolean"
    description: ""

  - name: "metadata"
    type: "object"
    description: ""
    subattributes:

  - name: "next_action"
    type: "object"
    description: ""
    subattributes:
    - name: "alipay_handle_redirect"
      type: "object"
      description: ""
      subattributes:
      - name: "native_data"
        type: "string"
        description: ""

      - name: "native_url"
        type: "string"
        description: ""

      - name: "return_url"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""


    - name: "boleto_display_details"
      type: "object"
      description: ""
      subattributes:
      - name: "expires_at"
        type: "string"
        description: ""

      - name: "hosted_voucher_url"
        type: "string"
        description: ""

      - name: "number"
        type: "string"
        description: ""

      - name: "pdf"
        type: "string"
        description: ""


    - name: "oxxo_display_details"
      type: "object"
      description: ""
      subattributes:
      - name: "expires_after"
        type: "string"
        description: ""

      - name: "hosted_voucher_url"
        type: "string"
        description: ""

      - name: "number"
        type: "string"
        description: ""


    - name: "redirect_to_url"
      type: "object"
      description: ""
      subattributes:
      - name: "return_url"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""


    - name: "type"
      type: "string"
      description: ""

    - name: "use_stripe_sdk"
      type: "object"
      description: ""
      subattributes:

    - name: "verify_with_microdeposits"
      type: "object"
      description: ""
      subattributes:
      - name: "arrival_date"
        type: "string"
        description: ""

      - name: "hosted_verification_url"
        type: "string"
        description: ""


    - name: "wechat_pay_display_qr_code"
      type: "object"
      description: ""
      subattributes:
      - name: "data"
        type: "string"
        description: ""

      - name: "image_data_url"
        type: "string"
        description: ""

      - name: "image_url_png"
        type: "string"
        description: ""

      - name: "image_url_svg"
        type: "string"
        description: ""


    - name: "wechat_pay_redirect_to_android_app"
      type: "object"
      description: ""
      subattributes:
      - name: "app_id"
        type: "string"
        description: ""

      - name: "nonce_str"
        type: "string"
        description: ""

      - name: "package"
        type: "string"
        description: ""

      - name: "partner_id"
        type: "string"
        description: ""

      - name: "prepay_id"
        type: "string"
        description: ""

      - name: "sign"
        type: "string"
        description: ""

      - name: "timestamp"
        type: "string"
        description: ""


    - name: "wechat_pay_redirect_to_ios_app"
      type: "object"
      description: ""
      subattributes:
      - name: "native_url"
        type: "string"
        description: ""



  - name: "object"
    type: "string"
    description: ""

  - name: "on_behalf_of"
    type: "string"
    description: ""

  - name: "payment_method"
    type: "string"
    description: ""

  - name: "payment_method_options"
    type: "object"
    description: ""
    subattributes:
    - name: "acss_debit"
      type: "object"
      description: ""
      subattributes:
      - name: "mandate_options"
        type: "object"
        description: ""
        subattributes:
        - name: "custom_mandate_url"
          type: "string"
          description: ""

        - name: "interval_description"
          type: "string"
          description: ""

        - name: "payment_schedule"
          type: "string"
          description: ""

        - name: "transaction_type"
          type: "string"
          description: ""



    - name: "afterpay_clearpay"
      type: "object"
      description: ""
      subattributes:
      - name: "reference"
        type: "string"
        description: ""

      - name: "setup_future_usage"
        type: "string"
        description: ""


    - name: "alipay"
      type: "object"
      description: ""
      subattributes:
      - name: "setup_future_usage"
        type: "string"
        description: ""


    - name: "au_becs_debit"
      type: "object"
      description: ""
      subattributes:
      - name: "setup_future_usage"
        type: "string"
        description: ""


    - name: "bacs_debit"
      type: "object"
      description: ""
      subattributes:
      - name: "setup_future_usage"
        type: "string"
        description: ""


    - name: "bancontact"
      type: "object"
      description: ""
      subattributes:
      - name: "setup_future_usage"
        type: "string"
        description: ""

      - name: "preferred_language"
        type: "string"
        description: ""


    - name: "boleto"
      type: "object"
      description: ""
      subattributes:
      - name: "setup_future_usage"
        type: "string"
        description: ""

      - name: "expires_after_days"
        type: "integer"
        description: ""


    - name: "card"
      type: "object"
      description: ""
      subattributes:
      - name: "installments"
        type: "object"
        description: ""
        subattributes:
        - name: "available_plans"
          type: "object"
          description: ""
          subattributes:
          - name: "count"
            type: "integer"
            description: ""

          - name: "interval"
            type: "string"
            description: ""

          - name: "type"
            type: "string"
            description: ""


        - name: "enabled"
          type: "boolean"
          description: ""

        - name: "plan"
          type: "object"
          description: ""
          subattributes:
          - name: "count"
            type: "integer"
            description: ""

          - name: "interval"
            type: "string"
            description: ""

          - name: "type"
            type: "string"
            description: ""



      - name: "network"
        type: "string"
        description: ""

      - name: "request_three_d_secure"
        type: "string"
        description: ""

      - name: "setup_future_usage"
        type: "string"
        description: ""


    - name: "card_present"
      type: "object"
      description: ""
      subattributes:

    - name: "eps"
      type: "object"
      description: ""
      subattributes:
      - name: "setup_future_usage"
        type: "string"
        description: ""


    - name: "fps"
      type: "object"
      description: ""
      subattributes:
      - name: "setup_future_usage"
        type: "string"
        description: ""


    - name: "giropay"
      type: "object"
      description: ""
      subattributes:
      - name: "setup_future_usage"
        type: "string"
        description: ""


    - name: "grabpay"
      type: "object"
      description: ""
      subattributes:
      - name: "setup_future_usage"
        type: "string"
        description: ""


    - name: "ideal"
      type: "object"
      description: ""
      subattributes:
      - name: "setup_future_usage"
        type: "string"
        description: ""


    - name: "interac_present"
      type: "object"
      description: ""
      subattributes:

    - name: "klarna"
      type: "object"
      description: ""
      subattributes:
      - name: "preferred_locale"
        type: "string"
        description: ""

      - name: "setup_future_usage"
        type: "string"
        description: ""


    - name: "oxxo"
      type: "object"
      description: ""
      subattributes:
      - name: "expires_after_days"
        type: "integer"
        description: ""

      - name: "setup_future_usage"
        type: "string"
        description: ""


    - name: "p24"
      type: "object"
      description: ""
      subattributes:
      - name: "setup_future_usage"
        type: "string"
        description: ""


    - name: "sepa_debit"
      type: "object"
      description: ""
      subattributes:
      - name: "mandate_options"
        type: "object"
        description: ""
        subattributes:

      - name: "setup_future_usage"
        type: "string"
        description: ""


    - name: "sofort"
      type: "object"
      description: ""
      subattributes:
      - name: "preferred_language"
        type: "string"
        description: ""

      - name: "setup_future_usage"
        type: "string"
        description: ""


    - name: "wechat_pay"
      type: "object"
      description: ""
      subattributes:
      - name: "app_id"
        type: "string"
        description: ""

      - name: "client"
        type: "string"
        description: ""

      - name: "setup_future_usage"
        type: "string"
        description: ""



  - name: "payment_method_types"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: ""
      description: ""

  - name: "processing"
    type: "object"
    description: ""
    subattributes:

  - name: "receipt_email"
    type: "string"
    description: ""

  - name: "review"
    type: "string"
    description: ""

  - name: "setup_future_usage"
    type: "string"
    description: ""

  - name: "shipping"
    type: "object"
    description: ""
    subattributes:
    - name: "address"
      type: "object"
      description: ""
      subattributes:
      - name: "line2"
        type: "string"
        description: ""

      - name: "state"
        type: "string"
        description: ""

      - name: "city"
        type: "string"
        description: ""

      - name: "postal_code"
        type: "string"
        description: ""

      - name: "country"
        type: "string"
        description: ""

      - name: "line1"
        type: "string"
        description: ""


    - name: "name"
      type: "string"
      description: ""

    - name: "phone"
      type: "string"
      description: ""

    - name: "carrier"
      type: "string"
      description: ""

    - name: "tracking_number"
      type: "string"
      description: ""


  - name: "source"
    type: "string"
    description: ""

  - name: "statement_descriptor"
    type: "string"
    description: ""

  - name: "statement_descriptor_suffix"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "transfer_data"
    type: "object"
    description: ""
    subattributes:
    - name: "amount"
      type: "integer"
      description: ""

    - name: "destination"
      type: "string"
      description: ""


  - name: "transfer_group"
    type: "string"
    description: ""

  - name: "updated"
    type: "string"
    description: ""

  - name: "updated_by_event_type"
    type: "string"
    description: "Description of the event"
---