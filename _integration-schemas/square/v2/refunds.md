---
tap: "square"
version: "2"
key: "refund"

name: "refunds"
doc-link: "https://developer.squareup.com/reference/square/refunds-api"
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/refunds.json"
description: |
  The `{{ table.name }}` table contains information about refunds on items in {{ integration.display_name }}.

replication-method: "Full Table"

api-method:
  name: "List payment refunds (V2)"
  doc-link: "https://developer.squareup.com/reference/square/refunds-api/list-payment-refunds"

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


  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "destination_details"
    type: "object"
    description: ""
    subattributes:
    - name: "card_details"
      type: "object"
      description: ""
      subattributes:
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



  - name: "destination_type"
    type: "string"
    description: ""

  - name: "id"
    type: "string"
    description: ""

  - name: "location_id"
    type: "string"
    description: ""

  - name: "order_id"
    type: "string"
    description: ""

  - name: "payment_id"
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



  - name: "reason"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "team_member_id"
    type: "string"
    description: ""

  - name: "unlinked"
    type: "boolean"
    description: ""

  - name: "updated_at"
    type: "date-time"
    description: ""
---