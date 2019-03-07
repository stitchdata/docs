---
tap: "shiphero"
version: "1.0"

name: "shipments"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-shiphero/blob/master/tap_shiphero/schemas/shipments.json"
description: |
  The `{{ table.name }}` table contains info about the shipments in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"
api-method:
    name: "Get shipments"
    doc-link: "https://shipheropublic.docs.apiary.io/#reference/shipment/get-shipments/get-shipments"

replication-key:
  name: "from"
  description: "A path parameter indicating the date from which records should be selected."

attributes:
  - name: "shipment_id"
    type: "string"
    primary-key: true
    description: "The shipment ID."
    foreign-key-id: "shipment-id"

  - name: "carrier"
    type: "string"
    description: "The carrier associated with the shipment."

  - name: "date"
    type: "date-time"
    description: "The date of the shipment."

  - name: "height"
    type: "number"
    description: "The height of the shipment."

  - name: "label_cost"
    type: "number"
    description: "The cost of the shipping label."

  - name: "length"
    type: "number"
    description: "The length of the shipment."

  - name: "line_items"
    type: "array"
    description: "Details about the line items in the shipment."
    array-attributes:
      - name: "line_item_id"
        type: "string"
        primary-key: true
        description: "The line item ID."

      - name: "partner_line_item_id"
        type: "string"
        description: "The partner line item ID."

      - name: "quantity"
        type: "integer"
        description: "The quantity."

      - name: "shipment_line_item_id"
        type: "string"
        description: "The shipment line item ID."

      - name: "sku"
        type: "string"
        description: "The SKU."

  - name: "method"
    type: "string"
    description: "The shipping method."

  - name: "order"
    type: "object"
    description: "Details about the order associated with the shipment."
    object-attributes:
      - name: "authorizations"
        type: "array"
        description: "Details about the authorizations associated with the order."
        array-attributes:
          - name: "authorized_amount"
            type: "number"
            description: "The authorized amount."

          - name: "card_type"
            type: "string"
            description: "The card type."

          - name: "date"
            type: "date-time"
            description: "The date of the authorization."

          - name: "postauthed_amount"
            type: "number"
            description: ""

          - name: "refunded_amount"
            type: "number"
            description: "The refunded amount."

          - name: "transaction_id"
            type: "string"
            description: "The transaction ID."

      - name: "fulfillment_status"
        type: "string"
        description: "The fulfillment status of the order."

      - name: "id"
        type: "integer"
        description: "The ID of the order associated with the shipment."
        foreign-key-id: "order-id"

      - name: "line_items"
        type: "array"
        description: "Details about the line items in the order."
        array-attributes:
          - name: "id"
            type: "integer"
            primary-key: true
            description: "The line item ID."

          - name: "backorder_quantity"
            type: "integer"
            description: ""

          - name: "barcode"
            type: "string"
            description: "The line item ID."

          - name: "created_at"
            type: "date-time"
            description: "The date the line item was created."

          - name: "custom_barcode"
            type: "string"
            description: ""

          - name: "custom_options"
            type: "string"
            description: ""

          - name: "customs_value"
            type: "string"
            description: ""

          - name: "eligible_for_return"
            type: "integer"
            description: "Indicates if the line item is eligible for return."

          - name: "fulfillment_status"
            type: "string"
            description: "The fulfillment status of the line item."

          - name: "large_thumbnail"
            type: "string"
            description: ""

          - name: "locked_to_warehouse_id"
            type: "integer"
            description: ""

          - name: "name"
            type: "string"
            description: "The name of the line item."

          - name: "option_title"
            type: "string"
            description: ""

          - name: "partner_line_item_id"
            type: "string"
            description: ""

          - name: "price"
            type: "string"
            description: "The price of the line item."

          - name: "product_attributes"
            type: "string"
            description: ""

          - name: "product_id"
            type: "string"
            description: "The product ID."
            foreign-key-id: "product-id"

          - name: "quantity"
            type: "integer"
            description: "The quantity of the product in the order."

          - name: "quantity_allocated"
            type: "integer"
            description: ""

          - name: "quantity_pending_fulfillment"
            type: "integer"
            description: ""

          - name: "quantity_shipped"
            type: "integer"
            description: ""

          - name: "sku"
            type: "string"
            description: "The SKU."

          - name: "subtotal"
            type: "string"
            description: "The subtotal for the line item."

          - name: "thumbnail"
            type: "string"
            description: ""

          - name: "updated_at"
            type: "date-time"
            description: "The date the line item was last updated."

          - name: "warehouse"
            type: "string"
            description: ""

          - name: "warehouse_id"
            type: "integer"
            description: "The ID of the warehouse associated with the linte item."
            foreign-key-id: "warehouse-id"

      - name: "note_attributes"
        type: "array"
        description: ""
        array-attributes:
          - name: "name"
            type: "string"
            description: ""

          - name: "value"
            type: "string"
            description: ""

      - name: "order_date"
        type: "date-time"
        description: "The date of the order."

      - name: "order_history"
        type: "array"
        description: ""
        array-attributes:
          - name: "created_at"
            type: "date-time"
            description: ""

          - name: "information"
            type: "string"
            description: ""

          - name: "username"
            type: "string"
            description: ""

      - name: "order_number"
        type: "string"
        description: "The order number."

      - name: "partner_order_id"
        type: "string"
        description: ""

      - name: "payment_method"
        type: "string"
        description: "The payment method associated with the order."

      - name: "ready_to_ship"
        type: "integer"
        description: "Indicates if the order is ready to ship."

      - name: "shipping_address"
        type: "object"
        description: ""
        object-attributes: 
          - name: "address1"
            type: "string"
            description: "The first line of the shipping address."

          - name: "address2"
            type: "string"
            description: "The second line of the shipping address."

          - name: "city"
            type: "string"
            description: "The city of the shipping address."

          - name: "company"
            type: "string"
            description: "The company associated with the shipping address."

          - name: "country"
            type: "string"
            description: "The country of the shipping address."

          - name: "country_code"
            type: "string"
            description: "The country code."

          - name: "email"
            type: "string"
            description: "The email address."

          - name: "first_name"
            type: "string"
            description: "The first name."

          - name: "last_name"
            type: "string"
            description: "The last name."

          - name: "phone"
            type: "string"
            description: "The phone number of the shipping address."

          - name: "province"
            type: "string"
            description: "The province of the shipping address."

          - name: "province_code"
            type: "string"
            description: "The province code."

          - name: "zip"
            type: "string"
            description: "The zip code."

      - name: "shipping_lines"
        type: "object"
        description: "Details about the shipping lines in the order."
        object-attributes:
          - name: "carrier"
            type: "string"
            description: "The shipping carrier."

          - name: "method"
            type: "string"
            description: "The shipping method."

          - name: "price"
            type: "number"
            description: "The price of the shipping line."

          - name: "title"
            type: "string"
            description: "The shipping title."

      - name: "shop_name"
        type: "string"
        description: "The shop name associated with the order."

      - name: "subtotal_price"
        type: "string"
        description: "The subtotal for the order."

      - name: "tags"
        type: "array"
        description: "Tags applied to the order."
        array-attributes:
          - name: "value"
            type: "string"
            description: "The tag."

      - name: "total_discounts"
        type: "number"
        description: "The total discounts applied to the order."

      - name: "total_price"
        type: "string"
        description: "The total cost of the order."

      - name: "total_tax"
        type: "string"
        description: "The total tax applied to the order."

  - name: "order_id"
    type: "string"
    description: "The ID of the order associated with the shipment."
    foreign-key-id: "order-id"

  - name: "order_number"
    type: "string"
    description: "The order number."

  - name: "shipper_email"
    type: "string"
    description: "The shipper email."

  - name: "shipper_id"
    type: "string"
    description: "The shipper ID."

  - name: "shipping_name"
    type: "string"
    description: "The shipping name. For example: `UPS Ground`"

  - name: "status"
    type: "string"
    description: "The status of the shipment."

  - name: "tracking"
    type: "string"
    description: "The tracking number for the shipment."

  - name: "warehouse"
    type: "string"
    description: "The warehouse associated with the shipment."

  - name: "weight"
    type: "number"
    description: "The weight of the shipment."

  - name: "width"
    type: "number"
    description: "The width of the shipment."
---