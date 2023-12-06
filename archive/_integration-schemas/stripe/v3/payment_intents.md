---
tap: "stripe"
version: "3"
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
    type: "date-time"
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
    type: "date-time"
    description: ""

  - name: "cancellation_reason"
    type: "string"
    description: ""

  - name: "capture_method"
    type: "string"
    description: ""

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


  - name: "latest_charge"
    type: "string"
    description: ""

  - name: "livemode"
    type: "boolean"
    description: ""

  - name: "metadata"
    type: "object"
    description: ""

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
        type: "date-time"
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
        type: "date-time"
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

    - name: "verify_with_microdeposits"
      type: "object"
      description: ""
      subattributes:
      - name: "arrival_date"
        type: "date-time"
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
          type: "array"
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
    type: "date-time"
    description: ""

  - name: "updated_by_event_type"
    type: "string"
    description: ""
---