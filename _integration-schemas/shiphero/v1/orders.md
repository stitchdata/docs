---
tap: "shiphero"
version: "1.0"

name: "orders"
doc-link: "https://shipheropublic.docs.apiary.io/#reference/orders/get-orders/get-orders"
singer-schema: "https://github.com/singer-io/tap-shiphero/blob/master/tap_shiphero/schemas/orders.json"
description: |
  The `{{ table.name }}` table contains info about the orders in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"
api-method:
    name: "Get orders"
    doc-link: "https://shipheropublic.docs.apiary.io/#reference/orders/get-orders/get-orders"

replication-key:
  name: "updated_from:updated_to"
  description: "Path parameters indicating the date range from which records should be selected."

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The order ID."
    foreign-key-id: "order-id"

  - name: "account_id"
    type: "integer"
    description: "The customer's account ID."

  - name: "adult_signature_required"
    type: "integer"
    description: "Indicates if an adult's signature is required."

  - name: "alcohol"
    type: "integer"
    description: "Indicates if alcohol is included in the order."

  - name: "allocation_priority"
    type: "integer"
    description: ""

  - name: "allow_partial"
    type: "integer"
    description: ""

  - name: "allow_split"
    type: "integer"
    description: ""

  - name: "billing_address"
    type: "object"
    description: "The customer's billing address."
    address-type: "billing"
    subattributes: &address-attributes
      - name: "address1"
        type: "string"
        description: "The first line of the {{ attribute.address-type }} address."

      - name: "address2"
        type: "string"
        description: "The second line of the {{ attribute.address-type }} address."

      - name: "city"
        type: "string"
        description: "The city of the {{ attribute.address-type }} address."

      - name: "company"
        type: "string"
        description: "The company associated with the {{ attribute.address-type }} address."

      - name: "country"
        type: "string"
        description: "The country of the {{ attribute.address-type }} address."

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
        description: "The phone number of the {{ attribute.address-type }} address."

      - name: "province"
        type: "string"
        description: "The province of the {{ attribute.address-type }} address."

      - name: "province_code"
        type: "string"
        description: "The province code."

      - name: "zip"
        type: "string"
        description: "The zip code."

  - name: "created_at"
    type: "date-time"
    description: "The time the order was created."

  - name: "currency"
    type: "string"
    description: "The currency of the order."

  - name: "discount"
    type: "string"
    description: ""

  - name: "expected_weight_in_oz"
    type: "number"
    description: ""

  - name: "flagged"
    type: "integer"
    description: ""

  - name: "fraudscore"
    type: "integer"
    description: ""

  - name: "fraudscore_details"
    type: "string"
    description: ""

  - name: "fulfillment_status"
    type: "string"
    description: ""

  - name: "gift_invoice"
    type: "integer"
    description: ""

  - name: "gift_note"
    type: "string"
    description: ""

  - name: "has_dry_ice"
    type: "integer"
    description: ""

  - name: "hold_shipment_until"
    type: "date-time"
    description: ""

  - name: "holds"
    type: "object"
    description: ""
    subattributes:
      - name: "address"
        type: "integer"
        description: ""

      - name: "fraud"
        type: "integer"
        description: ""

      - name: "operator"
        type: "integer"
        description: ""

      - name: "payment"
        type: "integer"
        description: ""

      - name: "shipping_method"
        type: "integer"
        description: ""

  - name: "ignore_address_validation_errors"
    type: "integer"
    description: ""

  - name: "insurance"
    type: "integer"
    description: "Indicates if the order has insurance."

  - name: "insurance_amount"
    type: "integer"
    description: "The amount of insurance associated with the order."

  - name: "invoice"
    type: "string"
    description: ""

  - name: "line_items"
    type: "array"
    description: "Details about the line items in the order."
    subattributes:
      - name: "id"
        type: "integer"
        primary-key: true
        description: "The line item ID."

      - name: "backorder_quantity"
        type: "integer"
        description: ""

      - name: "barcode"
        type: "string"
        description: "The barcode associated with the line item."

      - name: "created_at"
        type: "date-time"
        description: "The time the line item was created."

      - name: "custom_barcode"
        type: "string"
        description: "The custom barcode associated with the line item."

      - name: "custom_options"
        type: "string"
        description: ""

      - name: "customs_value"
        type: "string"
        description: ""

      - name: "eligible_for_return"
        type: "integer"
        description: "Indicates if the item is eligible for return."

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

      - name: "product_id"
        type: "string"
        description: "The product ID of the line item."
        foreign-key-id: "product-id"

      - name: "quantity"
        type: "integer"
        description: "The quantity of the item in the order."

      - name: "quantity_allocated"
        type: "integer"
        description: "The allocated quantity of the line item."

      - name: "quantity_pending_fulfillment"
        type: "integer"
        description: "The quantity pending fulfillment."

      - name: "quantity_shipped"
        type: "integer"
        description: "The quantity that has been shipped."

      - name: "sku"
        type: "string"
        description: "The SKU associated with the line item."

      - name: "subtotal"
        type: "string"
        description: "The subtotal of the line item. This is calculated as `price x quantity`."

      - name: "thumbnail"
        type: "string"
        description: ""

      - name: "updated_at"
        type: "date-time"
        description: "The time the line item was last updated."

      - name: "warehouse"
        type: "string"
        description: ""

      - name: "warehouse_id"
        type: "integer"
        description: ""
        foreign-key-id: "warehouse-id"

  - name: "lock_data"
    type: "object"
    description: ""

  - name: "order_date"
    type: "date-time"
    description: "The date of the order."

  - name: "order_history"
    type: "array"
    description: ""
    subattributes:
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

  - name: "packing_note"
    type: "string"
    description: ""

  - name: "partner_order_id"
    type: "string"
    description: ""

  - name: "payment_method"
    type: "string"
    description: "The payment method associated with the order."

  - name: "priority_flag"
    type: "integer"
    description: ""

  - name: "profile"
    type: "string"
    description: ""

  - name: "requested_delivery_at"
    type: "date-time"
    description: "The requested delivery date for the order."

  - name: "require_signature"
    type: "integer"
    description: "Indicates if a signature is required for the order."

  - name: "required_ship_date"
    type: "date-time"
    description: "The required ship date for the order."

  - name: "saturday_delivery"
    type: "integer"
    description: ""

  - name: "shipping_address"
    type: "object"
    description: ""
    address-type: "shipping"
    subattributes: *address-attributes

  - name: "shipping_lines"
    type: "object"
    description: "Details about the shipping lines in the order."
    subattributes:
      - name: "carrier"
        type: "string"
        description: "The shipping carrier."

      - name: "method"
        type: "string"
        description: "The shipping method."

      - name: "title"
        type: "string"
        description: "The shipping title."

  - name: "shipping_price"
    type: "number"
    description: "The price of shipping for the order."

  - name: "shop_name"
    type: "string"
    description: "The shop name associated with the order."

  - name: "source"
    type: "string"
    description: "The source of the order."

  - name: "subtotal"
    type: "string"
    description: "The subtotal of the order."

  - name: "tags"
    type: "array"
    description: "Tags that have been applied to the order."
    subattributes:
      - name: "value"
        type: "string"
        description: "The tag applied to the order."

  - name: "third_party_shipper"
    type: "object"
    description: ""
    subattributes:
      - name: "account_number"
        type: "string"
        description: ""

      - name: "country"
        type: "string"
        description: ""

      - name: "zip"
        type: "string"
        description: ""

  - name: "total_price"
    type: "string"
    description: "The total of the order."

  - name: "total_tax"
    type: "string"
    description: "The total tax on the order."

  - name: "updated_at"
    type: "date-time"
    description: "The time the order was last updated."
---