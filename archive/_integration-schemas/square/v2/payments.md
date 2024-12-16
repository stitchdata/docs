---
tap: "square"
version: "2"
key: "payment"

name: "payments"
doc-link: "https://developer.squareup.com/reference/square/payments-api"
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/payments.json"
description: |
  The `{{ table.name }}` table contains information about all payments taken in {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
  name: "List payments (V2)"
  doc-link: "https://developer.squareup.com/reference/square/payments-api/list-payments"

attributes:
  - name: "amount_money"
    type: "object"
    description: ""
    subattributes:
    - name: "amount"
      type: "integer"
      description: ""

    - name: "currency"
      type: "string"
      description: ""


  - name: "app_fee_money"
    type: "object"
    description: ""
    subattributes:
    - name: "amount"
      type: "integer"
      description: ""

    - name: "currency"
      type: "string"
      description: ""


  - name: "application_details"
    type: "object"
    description: ""
    subattributes:
    - name: "square_product"
      type: "string"
      description: ""

    - name: "application_id"
      type: "string"
      description: ""


  - name: "approved_money"
    type: "object"
    description: ""
    subattributes:
    - name: "amount"
      type: "integer"
      description: ""

    - name: "currency"
      type: "string"
      description: ""


  - name: "bank_account_details"
    type: "object"
    description: ""
    subattributes:
    - name: "bank_name"
      type: "string"
      description: ""

    - name: "transfer_type"
      type: "string"
      description: ""

    - name: "account_ownership_type"
      type: "string"
      description: ""

    - name: "fingerprint"
      type: "string"
      description: ""

    - name: "country"
      type: "string"
      description: ""

    - name: "statement_description"
      type: "string"
      description: ""

    - name: "ach_details"
      type: "object"
      description: ""
      subattributes:
      - name: "routing_number"
        type: "string"
        description: ""

      - name: "account_number_suffix"
        type: "string"
        description: ""

      - name: "account_type"
        type: "string"
        description: ""


    - name: "errors"
      type: "array"
      description: ""
      subattributes:
      - name: "category"
        type: "string"
        description: ""

      - name: "code"
        type: "string"
        description: ""

      - name: "detail"
        type: "string"
        description: ""

      - name: "field"
        type: "string"
        description: ""



  - name: "billing_address"
    type: "object"
    description: ""
    subattributes:
    - name: "address_line_1"
      type: "string"
      description: ""

    - name: "address_line_2"
      type: "string"
      description: ""

    - name: "address_line_3"
      type: "string"
      description: ""

    - name: "locality"
      type: "string"
      description: ""

    - name: "sublocality"
      type: "string"
      description: ""

    - name: "sublocality_2"
      type: "string"
      description: ""

    - name: "sublocality_3"
      type: "string"
      description: ""

    - name: "administrative_district_level_1"
      type: "string"
      description: ""

    - name: "administrative_district_level_2"
      type: "string"
      description: ""

    - name: "administrative_district_level_3"
      type: "string"
      description: ""

    - name: "postal_code"
      type: "string"
      description: ""

    - name: "country"
      type: "string"
      description: ""

    - name: "first_name"
      type: "string"
      description: ""

    - name: "last_name"
      type: "string"
      description: ""


  - name: "buy_now_pay_later_details"
    type: "object"
    description: ""
    subattributes:
    - name: "brand"
      type: "string"
      description: ""

    - name: "afterpay_details"
      type: "object"
      description: ""
      subattributes:
      - name: "email_address"
        type: "string"
        description: ""


    - name: "clearpay_details"
      type: "object"
      description: ""
      subattributes:
      - name: "email_address"
        type: "string"
        description: ""



  - name: "buyer_email_address"
    type: "string"
    description: ""

  - name: "capabilities"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "card_details"
    type: "object"
    description: ""
    subattributes:
    - name: "status"
      type: "string"
      description: ""

    - name: "card"
      type: "object"
      description: ""
      subattributes:
      - name: "id"
        type: "string"
        description: ""

      - name: "card_brand"
        type: "string"
        description: ""

      - name: "last_4"
        type: "string"
        description: ""

      - name: "exp_month"
        type: "integer"
        description: ""

      - name: "exp_year"
        type: "integer"
        description: ""

      - name: "cardholder_name"
        type: "string"
        description: ""

      - name: "billing_address"
        type: "object"
        description: ""
        subattributes:
        - name: "address_line_1"
          type: "string"
          description: ""

        - name: "address_line_2"
          type: "string"
          description: ""

        - name: "address_line_3"
          type: "string"
          description: ""

        - name: "locality"
          type: "string"
          description: ""

        - name: "sublocality"
          type: "string"
          description: ""

        - name: "sublocality_2"
          type: "string"
          description: ""

        - name: "sublocality_3"
          type: "string"
          description: ""

        - name: "administrative_district_level_1"
          type: "string"
          description: ""

        - name: "administrative_district_level_2"
          type: "string"
          description: ""

        - name: "administrative_district_level_3"
          type: "string"
          description: ""

        - name: "postal_code"
          type: "string"
          description: ""

        - name: "country"
          type: "string"
          description: ""

        - name: "first_name"
          type: "string"
          description: ""

        - name: "last_name"
          type: "string"
          description: ""


      - name: "fingerprint"
        type: "string"
        description: ""

      - name: "customer_id"
        type: "string"
        description: ""

      - name: "merchant_id"
        type: "string"
        description: ""

      - name: "reference_id"
        type: "string"
        description: ""

      - name: "enabled"
        type: "boolean"
        description: ""

      - name: "card_type"
        type: "string"
        description: ""

      - name: "prepaid_type"
        type: "string"
        description: ""

      - name: "bin"
        type: "string"
        description: ""

      - name: "version"
        type: "integer"
        description: ""

      - name: "card_co_brand"
        type: "string"
        description: ""


    - name: "entry_method"
      type: "string"
      description: ""

    - name: "cvv_status"
      type: "string"
      description: ""

    - name: "avs_status"
      type: "string"
      description: ""

    - name: "auth_result_code"
      type: "string"
      description: ""

    - name: "application_identifier"
      type: "string"
      description: ""

    - name: "application_name"
      type: "string"
      description: ""

    - name: "application_cryptogram"
      type: "string"
      description: ""

    - name: "verification_method"
      type: "string"
      description: ""

    - name: "verification_results"
      type: "string"
      description: ""

    - name: "errors"
      type: "array"
      description: ""
      subattributes:
      - name: "category"
        type: "string"
        description: ""

      - name: "code"
        type: "string"
        description: ""

      - name: "detail"
        type: "string"
        description: ""

      - name: "field"
        type: "string"
        description: ""


    - name: "statement_description"
      type: "string"
      description: ""

    - name: "card_payment_timeline"
      type: "object"
      description: ""
      subattributes:
      - name: "authorized_at"
        type: "date-time"
        description: ""

      - name: "captured_at"
        type: "date-time"
        description: ""

      - name: "voided_at"
        type: "date-time"
        description: ""



  - name: "cash_details"
    type: "object"
    description: ""
    subattributes:
    - name: "buyer_supplied_money"
      type: "object"
      description: ""
      subattributes:
      - name: "amount"
        type: "integer"
        description: ""

      - name: "currency"
        type: "string"
        description: ""


    - name: "change_back_money"
      type: "object"
      description: ""
      subattributes:
      - name: "amount"
        type: "integer"
        description: ""

      - name: "currency"
        type: "string"
        description: ""



  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "customer_id"
    type: "string"
    description: ""

  - name: "delay_action"
    type: "string"
    description: ""

  - name: "delay_duration"
    type: "string"
    description: ""

  - name: "delayed_until"
    type: "date-time"
    description: ""

  - name: "device_details"
    type: "object"
    description: ""
    subattributes:
    - name: "device_id"
      type: "string"
      description: ""

    - name: "device_installation_id"
      type: "string"
      description: ""

    - name: "device_name"
      type: "string"
      description: ""


  - name: "external_details"
    type: "object"
    description: ""
    subattributes:
    - name: "type"
      type: "string"
      description: ""

    - name: "source"
      type: "string"
      description: ""

    - name: "source_id"
      type: "string"
      description: ""

    - name: "source_fee_money"
      type: "object"
      description: ""
      subattributes:
      - name: "amount"
        type: "integer"
        description: ""

      - name: "currency"
        type: "string"
        description: ""



  - name: "id"
    type: "string"
    description: ""

  - name: "location_id"
    type: "string"
    description: ""

  - name: "note"
    type: "string"
    description: ""

  - name: "order_id"
    type: "string"
    description: ""

  - name: "processing_fee"
    type: "array"
    description: ""
    subattributes:
    - name: "effective_at"
      type: "date-time"
      description: ""

    - name: "type"
      type: "string"
      description: ""

    - name: "amount_money"
      type: "object"
      description: ""
      subattributes:
      - name: "amount"
        type: "integer"
        description: ""

      - name: "currency"
        type: "string"
        description: ""



  - name: "receipt_number"
    type: "string"
    description: ""

  - name: "receipt_url"
    type: "string"
    description: ""

  - name: "reference_id"
    type: "string"
    description: ""

  - name: "refund_ids"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "refunded_money"
    type: "object"
    description: ""
    subattributes:
    - name: "amount"
      type: "integer"
      description: ""

    - name: "currency"
      type: "string"
      description: ""


  - name: "risk_evaluation"
    type: "object"
    description: ""
    subattributes:
    - name: "created_at"
      type: "date-time"
      description: ""

    - name: "risk_level"
      type: "string"
      description: ""


  - name: "shipping_address"
    type: "object"
    description: ""
    subattributes:
    - name: "address_line_1"
      type: "string"
      description: ""

    - name: "address_line_2"
      type: "string"
      description: ""

    - name: "address_line_3"
      type: "string"
      description: ""

    - name: "locality"
      type: "string"
      description: ""

    - name: "sublocality"
      type: "string"
      description: ""

    - name: "sublocality_2"
      type: "string"
      description: ""

    - name: "sublocality_3"
      type: "string"
      description: ""

    - name: "administrative_district_level_1"
      type: "string"
      description: ""

    - name: "administrative_district_level_2"
      type: "string"
      description: ""

    - name: "administrative_district_level_3"
      type: "string"
      description: ""

    - name: "postal_code"
      type: "string"
      description: ""

    - name: "country"
      type: "string"
      description: ""

    - name: "first_name"
      type: "string"
      description: ""

    - name: "last_name"
      type: "string"
      description: ""


  - name: "source_type"
    type: "string"
    description: ""

  - name: "statement_description_identifier"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "team_member_id"
    type: "string"
    description: ""

  - name: "tip_money"
    type: "object"
    description: ""
    subattributes:
    - name: "amount"
      type: "integer"
      description: ""

    - name: "currency"
      type: "string"
      description: ""


  - name: "total_money"
    type: "object"
    description: ""
    subattributes:
    - name: "amount"
      type: "integer"
      description: ""

    - name: "currency"
      type: "string"
      description: ""


  - name: "updated_at"
    type: "date-time"
    description: ""

  - name: "version_token"
    type: "string"
    description: ""

  - name: "wallet_details"
    type: "object"
    description: ""
    subattributes:
    - name: "status"
      type: "string"
      description: ""

    - name: "brand"
      type: "string"
      description: ""

    - name: "cash_app_details"
      type: "object"
      description: ""
      subattributes:
      - name: "buyer_full_name"
        type: "string"
        description: ""

      - name: "buyer_country_code"
        type: "string"
        description: ""

      - name: "buyer_cashtag"
        type: "string"
        description: ""
---