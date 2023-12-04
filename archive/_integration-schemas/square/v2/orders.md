---
tap: "square"
version: "2"
key: "order"

name: "orders"
doc-link: "https://developer.squareup.com/reference/square/orders-api"
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/orders.json"
description: |
  The `{{ table.name }}` table contains information about order updates in {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
  name: "Search orders (V2)"
  doc-link: "https://developer.squareup.com/reference/square/orders-api/search-orders"

attributes:
  - name: "closed_at"
    type: "date-time"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "discounts"
    type: "array"
    description: ""
    subattributes:
    - name: "catalog_object_id"
      type: "string"
      description: ""

    - name: "catalog_version"
      type: "integer"
      description: ""

    - name: "name"
      type: "string"
      description: ""

    - name: "type"
      type: "string"
      description: ""

    - name: "percentage"
      type: "string"
      description: ""

    - name: "amount_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "applied_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "scope"
      type: "string"
      description: ""

    - name: "pricing_rule_id"
      type: "string"
      description: ""


  - name: "fulfillments"
    type: "array"
    description: ""
    subattributes:
    - name: "type"
      type: "string"
      description: ""

    - name: "pickup_details"
      type: "object"
      description: ""
      subattributes:
      - name: "placed_at"
        type: "date-time"
        description: ""

      - name: "accepted_at"
        type: "date-time"
        description: ""

      - name: "rejected_at"
        type: "date-time"
        description: ""

      - name: "ready_at"
        type: "date-time"
        description: ""

      - name: "picked_up_at"
        type: "date-time"
        description: ""

      - name: "canceled_at"
        type: "date-time"
        description: ""

      - name: "expired_at"
        type: "date-time"
        description: ""

      - name: "expires_at"
        type: "date-time"
        description: ""

      - name: "auto_complete_duration"
        type: "string"
        description: ""

      - name: "schedule_type"
        type: "string"
        description: ""

      - name: "cancel_reason"
        type: "string"
        description: ""

      - name: "pickup_at"
        type: "date-time"
        description: ""

      - name: "pickup_window_duration"
        type: "string"
        description: ""

      - name: "prep_time_duration"
        type: "string"
        description: ""

      - name: "note"
        type: "string"
        description: ""

      - name: "recipient"
        type: "object"
        description: ""
        subattributes:
        - name: "customer_id"
          type: "string"
          description: ""

        - name: "display_name"
          type: "string"
          description: ""

        - name: "email_address"
          type: "string"
          description: ""

        - name: "phone_number"
          type: "string"
          description: ""



    - name: "state"
      type: "string"
      description: ""

    - name: "uid"
      type: "string"
      description: ""


  - name: "id"
    type: "string"
    description: ""

  - name: "line_items"
    type: "array"
    description: ""
    subattributes:
    - name: "base_price_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "total_discount_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "variation_total_price_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "name"
      type: "string"
      description: ""

    - name: "quantity"
      type: "string"
      description: ""

    - name: "quantity_unit"
      type: "object"
      description: ""
      subattributes:
      - name: "precision"
        type: "integer"
        description: ""

      - name: "measurement_unit"
        type: "object"
        description: ""
        subattributes:
        - name: "custom_unit"
          type: "object"
          description: ""
          subattributes:
          - name: "name"
            type: "string"
            description: ""

          - name: "abbreviation"
            type: "string"
            description: ""


        - name: "area_unit"
          type: "string"
          description: ""

        - name: "length_unit"
          type: "string"
          description: ""

        - name: "volume_unit"
          type: "string"
          description: ""

        - name: "weight_unit"
          type: "string"
          description: ""

        - name: "generic_unit"
          type: "string"
          description: ""

        - name: "time_unit"
          type: "string"
          description: ""

        - name: "type"
          type: "string"
          description: ""


      - name: "catalog_object_id"
        type: "string"
        description: ""

      - name: "catalog_version"
        type: "integer"
        description: ""


    - name: "note"
      type: "string"
      description: ""

    - name: "uid"
      type: "string"
      description: ""

    - name: "gross_sales_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "total_tax_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "total_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "catalog_object_id"
      type: "string"
      description: ""

    - name: "catalog_version"
      type: "integer"
      description: ""

    - name: "variation_name"
      type: "string"
      description: ""

    - name: "item_type"
      type: "string"
      description: ""

    - name: "modifiers"
      type: "array"
      description: ""
      subattributes:
      - name: "catalog_object_id"
        type: "string"
        description: ""

      - name: "catalog_version"
        type: "integer"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "quantity"
        type: "string"
        description: ""

      - name: "base_price_money"
        type: "object"
        description: ""
        subattributes:
        - name: "amount"
          type: "integer"
          description: ""

        - name: "currency"
          type: "string"
          description: ""


      - name: "total_price_money"
        type: "object"
        description: ""
        subattributes:
        - name: "amount"
          type: "integer"
          description: ""

        - name: "currency"
          type: "string"
          description: ""




  - name: "location_id"
    type: "string"
    description: ""

  - name: "net_amount_due_money"
    type: "object"
    description: ""
    subattributes:
    - name: "currency"
      type: "string"
      description: ""

    - name: "amount"
      type: "integer"
      description: ""


  - name: "net_amounts"
    type: "object"
    description: ""
    subattributes:
    - name: "tip_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "service_charge_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "tax_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "discount_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "total_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""



  - name: "pricing_options"
    type: "object"
    description: ""
    subattributes:
    - name: "auto_apply_discounts"
      type: "boolean"
      description: ""


  - name: "reference_id"
    type: "string"
    description: ""

  - name: "refunds"
    type: "array"
    description: ""
    subattributes:
    - name: "location_id"
      type: "string"
      description: ""

    - name: "transaction_id"
      type: "string"
      description: ""

    - name: "created_at"
      type: "date-time"
      description: ""

    - name: "tender_id"
      type: "string"
      description: ""

    - name: "amount_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "processing_fee_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "status"
      type: "string"
      description: ""

    - name: "id"
      type: "string"
      description: ""

    - name: "reason"
      type: "string"
      description: ""


  - name: "return_amounts"
    type: "object"
    description: ""
    subattributes:
    - name: "tip_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "service_charge_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "tax_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "discount_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "total_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""



  - name: "returns"
    type: "array"
    description: ""
    subattributes:
    - name: "source_order_id"
      type: "string"
      description: ""

    - name: "return_line_items"
      type: "array"
      description: ""
      subattributes:
      - name: "base_price_money"
        type: "object"
        description: ""
        subattributes:
        - name: "currency"
          type: "string"
          description: ""

        - name: "amount"
          type: "integer"
          description: ""


      - name: "catalog_object_id"
        type: "string"
        description: ""

      - name: "catalog_version"
        type: "integer"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "note"
        type: "string"
        description: ""

      - name: "quantity_unit"
        type: "object"
        description: ""
        subattributes:
        - name: "precision"
          type: "integer"
          description: ""

        - name: "measurement_unit"
          type: "object"
          description: ""
          subattributes:
          - name: "area_unit"
            type: "string"
            description: ""

          - name: "custom_unit"
            type: "object"
            description: ""
            subattributes:
            - name: "abbreviation"
              type: "string"
              description: ""

            - name: "name"
              type: "string"
              description: ""


          - name: "generic_unit"
            type: "string"
            description: ""

          - name: "length_unit"
            type: "string"
            description: ""

          - name: "time_unit"
            type: "string"
            description: ""

          - name: "type"
            type: "string"
            description: ""

          - name: "volume_unit"
            type: "string"
            description: ""

          - name: "weight_unit"
            type: "string"
            description: ""


        - name: "catalog_object_id"
          type: "string"
          description: ""

        - name: "catalog_version"
          type: "integer"
          description: ""


      - name: "return_modifiers"
        type: "array"
        description: ""
        subattributes:
        - name: "base_price_money"
          type: "object"
          description: ""
          subattributes:
          - name: "currency"
            type: "string"
            description: ""

          - name: "amount"
            type: "integer"
            description: ""


        - name: "catalog_object_id"
          type: "string"
          description: ""

        - name: "catalog_version"
          type: "integer"
          description: ""

        - name: "quantity"
          type: "string"
          description: ""

        - name: "name"
          type: "string"
          description: ""

        - name: "source_modifier_uid"
          type: "string"
          description: ""

        - name: "total_price_money"
          type: "object"
          description: ""
          subattributes:
          - name: "currency"
            type: "string"
            description: ""

          - name: "amount"
            type: "integer"
            description: ""


        - name: "uid"
          type: "string"
          description: ""


      - name: "source_line_item_uid"
        type: "string"
        description: ""

      - name: "variation_name"
        type: "string"
        description: ""

      - name: "item_type"
        type: "string"
        description: ""

      - name: "total_tax_money"
        type: "object"
        description: ""
        subattributes:
        - name: "currency"
          type: "string"
          description: ""

        - name: "amount"
          type: "integer"
          description: ""


      - name: "gross_return_money"
        type: "object"
        description: ""
        subattributes:
        - name: "currency"
          type: "string"
          description: ""

        - name: "amount"
          type: "integer"
          description: ""


      - name: "total_money"
        type: "object"
        description: ""
        subattributes:
        - name: "currency"
          type: "string"
          description: ""

        - name: "amount"
          type: "integer"
          description: ""


      - name: "variation_total_price_money"
        type: "object"
        description: ""
        subattributes:
        - name: "currency"
          type: "string"
          description: ""

        - name: "amount"
          type: "integer"
          description: ""


      - name: "quantity"
        type: "string"
        description: ""

      - name: "applied_discounts"
        type: "array"
        description: ""
        subattributes:
        - name: "discount_uid"
          type: "string"
          description: ""

        - name: "applied_money"
          type: "object"
          description: ""
          subattributes:
          - name: "currency"
            type: "string"
            description: ""

          - name: "amount"
            type: "integer"
            description: ""


        - name: "uid"
          type: "string"
          description: ""


      - name: "applied_taxes"
        type: "array"
        description: ""
        subattributes:
        - name: "tax_uid"
          type: "string"
          description: ""

        - name: "applied_money"
          type: "object"
          description: ""
          subattributes:
          - name: "currency"
            type: "string"
            description: ""

          - name: "amount"
            type: "integer"
            description: ""


        - name: "uid"
          type: "string"
          description: ""


      - name: "total_discount_money"
        type: "object"
        description: ""
        subattributes:
        - name: "currency"
          type: "string"
          description: ""

        - name: "amount"
          type: "integer"
          description: ""


      - name: "total_service_charge_money"
        type: "object"
        description: ""
        subattributes:
        - name: "currency"
          type: "string"
          description: ""

        - name: "amount"
          type: "integer"
          description: ""


      - name: "applied_service_charges"
        type: "array"
        description: ""
        subattributes:
        - name: "uid"
          type: "string"
          description: ""

        - name: "service_charge_uid"
          type: "string"
          description: ""

        - name: "applied_money"
          type: "object"
          description: ""
          subattributes:
          - name: "currency"
            type: "string"
            description: ""

          - name: "amount"
            type: "integer"
            description: ""



      - name: "uid"
        type: "string"
        description: ""


    - name: "uid"
      type: "string"
      description: ""

    - name: "return_service_charges"
      type: "array"
      description: ""
      subattributes:
      - name: "source_service_charge_uid"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "catalog_object_id"
        type: "string"
        description: ""

      - name: "catalog_version"
        type: "integer"
        description: ""

      - name: "percentage"
        type: "string"
        description: ""

      - name: "amount_money"
        type: "object"
        description: ""
        subattributes:
        - name: "currency"
          type: "string"
          description: ""

        - name: "amount"
          type: "integer"
          description: ""


      - name: "applied_money"
        type: "object"
        description: ""
        subattributes:
        - name: "currency"
          type: "string"
          description: ""

        - name: "amount"
          type: "integer"
          description: ""


      - name: "total_money"
        type: "object"
        description: ""
        subattributes:
        - name: "currency"
          type: "string"
          description: ""

        - name: "amount"
          type: "integer"
          description: ""


      - name: "total_tax_money"
        type: "object"
        description: ""
        subattributes:
        - name: "currency"
          type: "string"
          description: ""

        - name: "amount"
          type: "integer"
          description: ""


      - name: "calculation_phase"
        type: "string"
        description: ""

      - name: "taxable"
        type: "boolean"
        description: ""


    - name: "return_taxes"
      type: "array"
      description: ""
      subattributes:
      - name: "uid"
        type: "string"
        description: ""

      - name: "source_tax_uid"
        type: "string"
        description: ""

      - name: "catalog_object_id"
        type: "string"
        description: ""

      - name: "catalog_version"
        type: "integer"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "percentage"
        type: "string"
        description: ""

      - name: "applied_money"
        type: "object"
        description: ""
        subattributes:
        - name: "currency"
          type: "string"
          description: ""

        - name: "amount"
          type: "integer"
          description: ""


      - name: "scope"
        type: "string"
        description: ""


    - name: "return_discounts"
      type: "array"
      description: ""
      subattributes:
      - name: "uid"
        type: "string"
        description: ""

      - name: "source_discount_uid"
        type: "string"
        description: ""

      - name: "catalog_object_id"
        type: "string"
        description: ""

      - name: "catalog_version"
        type: "integer"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "percentage"
        type: "string"
        description: ""

      - name: "amount_money"
        type: "object"
        description: ""
        subattributes:
        - name: "currency"
          type: "string"
          description: ""

        - name: "amount"
          type: "integer"
          description: ""


      - name: "applied_money"
        type: "object"
        description: ""
        subattributes:
        - name: "currency"
          type: "string"
          description: ""

        - name: "amount"
          type: "integer"
          description: ""


      - name: "scope"
        type: "string"
        description: ""


    - name: "rounding_adjustment"
      type: "object"
      description: ""
      subattributes:
      - name: "uid"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "amount_money"
        type: "object"
        description: ""
        subattributes:
        - name: "currency"
          type: "string"
          description: ""

        - name: "amount"
          type: "integer"
          description: ""



    - name: "return_amounts"
      type: "object"
      description: ""
      subattributes:
      - name: "total_money"
        type: "object"
        description: ""
        subattributes:
        - name: "currency"
          type: "string"
          description: ""

        - name: "amount"
          type: "integer"
          description: ""


      - name: "tax_money"
        type: "object"
        description: ""
        subattributes:
        - name: "currency"
          type: "string"
          description: ""

        - name: "amount"
          type: "integer"
          description: ""


      - name: "discount_money"
        type: "object"
        description: ""
        subattributes:
        - name: "currency"
          type: "string"
          description: ""

        - name: "amount"
          type: "integer"
          description: ""


      - name: "tip_money"
        type: "object"
        description: ""
        subattributes:
        - name: "currency"
          type: "string"
          description: ""

        - name: "amount"
          type: "integer"
          description: ""


      - name: "service_charge_money"
        type: "object"
        description: ""
        subattributes:
        - name: "currency"
          type: "string"
          description: ""

        - name: "amount"
          type: "integer"
          description: ""




  - name: "service_charges"
    type: "array"
    description: ""
    subattributes:
    - name: "catalog_object_id"
      type: "string"
      description: ""

    - name: "catalog_version"
      type: "integer"
      description: ""

    - name: "name"
      type: "string"
      description: ""

    - name: "type"
      type: "string"
      description: ""

    - name: "percentage"
      type: "string"
      description: ""

    - name: "amount_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "applied_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "total_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "total_tax_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "calculation_phase"
      type: "string"
      description: ""

    - name: "taxable"
      type: "boolean"
      description: ""


  - name: "source"
    type: "object"
    description: ""
    subattributes:
    - name: "name"
      type: "string"
      description: ""


  - name: "state"
    type: "string"
    description: ""

  - name: "taxes"
    type: "array"
    description: ""
    subattributes:
    - name: "catalog_object_id"
      type: "string"
      description: ""

    - name: "catalog_version"
      type: "integer"
      description: ""

    - name: "name"
      type: "string"
      description: ""

    - name: "type"
      type: "string"
      description: ""

    - name: "percentage"
      type: "string"
      description: ""

    - name: "applied_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "scope"
      type: "string"
      description: ""


  - name: "tenders"
    type: "array"
    description: ""
    subattributes:
    - name: "location_id"
      type: "string"
      description: ""

    - name: "transaction_id"
      type: "string"
      description: ""

    - name: "created_at"
      type: "date-time"
      description: ""

    - name: "card_details"
      type: "object"
      description: ""
      subattributes:
      - name: "card"
        type: "object"
        description: ""
        subattributes:
        - name: "exp_year"
          type: "integer"
          description: ""

        - name: "last_4"
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

        - name: "exp_month"
          type: "integer"
          description: ""

        - name: "bin"
          type: "string"
          description: ""

        - name: "card_type"
          type: "string"
          description: ""

        - name: "cardholder_name  "
          type: "string"
          description: ""

        - name: "id"
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

        - name: "version"
          type: "integer"
          description: ""

        - name: "card_co_brand"
          type: "string"
          description: ""

        - name: "card_brand"
          type: "string"
          description: ""

        - name: "prepaid_type"
          type: "string"
          description: ""


      - name: "entry_method"
        type: "string"
        description: ""

      - name: "status"
        type: "string"
        description: ""


    - name: "cash_details"
      type: "object"
      description: ""
      subattributes:
      - name: "buyer_tendered_money"
        type: "object"
        description: ""
        subattributes:
        - name: "currency"
          type: "string"
          description: ""

        - name: "amount"
          type: "integer"
          description: ""


      - name: "change_back_money"
        type: "object"
        description: ""
        subattributes:
        - name: "currency"
          type: "string"
          description: ""

        - name: "amount"
          type: "integer"
          description: ""



    - name: "payment_id"
      type: "string"
      description: ""

    - name: "customer_id"
      type: "string"
      description: ""

    - name: "type"
      type: "string"
      description: ""

    - name: "amount_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "tip_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "processing_fee_money"
      type: "object"
      description: ""
      subattributes:
      - name: "currency"
        type: "string"
        description: ""

      - name: "amount"
        type: "integer"
        description: ""


    - name: "id"
      type: "string"
      description: ""

    - name: "note"
      type: "string"
      description: ""


  - name: "total_discount_money"
    type: "object"
    description: ""
    subattributes:
    - name: "currency"
      type: "string"
      description: ""

    - name: "amount"
      type: "integer"
      description: ""


  - name: "total_money"
    type: "object"
    description: ""
    subattributes:
    - name: "currency"
      type: "string"
      description: ""

    - name: "amount"
      type: "integer"
      description: ""


  - name: "total_service_charge_money"
    type: "object"
    description: ""
    subattributes:
    - name: "currency"
      type: "string"
      description: ""

    - name: "amount"
      type: "integer"
      description: ""


  - name: "total_tax_money"
    type: "object"
    description: ""
    subattributes:
    - name: "currency"
      type: "string"
      description: ""

    - name: "amount"
      type: "integer"
      description: ""


  - name: "total_tip_money"
    type: "object"
    description: ""
    subattributes:
    - name: "currency"
      type: "string"
      description: ""

    - name: "amount"
      type: "integer"
      description: ""


  - name: "updated_at"
    type: "date-time"
    description: ""
    replication-key: true

  - name: "version"
    type: "integer"
    description: ""
---