---
tap: "recharge"
version: "1"
key: "order"

name: "orders"
doc-link: "https://developer.rechargepayments.com/#list-orders"
singer-schema: "https://github.com/singer-io/tap-recharge/blob/master/tap_recharge/schemas/orders.json"
description: |
  The `{{ table.name }}` table contains info about orders. Orders are created after a charge is successfully processed.

replication-method: "Key-based Incremental"
api-method:
  name: "List orders"
  doc-link: "https://developer.rechargepayments.com/#list-orders"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The order ID."
    #foreign-key-id: "order-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The date and time the order was last updated."

  - name: "address_id"
    type: "integer"
    description: "The ID of the customer address the order will ship to."
    foreign-key-id: "address-id"

  - name: "address_is_active"
    type: "integer"
    description: "If `true`, the address is inactive."

  - name: "billing_address"
    type: "object"
    description: |
      The billing information related to the order.
      {% assign address-type = "billing" %}
    subattributes: &address
      - name: "address1"
        type: "string"
        description: |
          The street address of the {{ address-type }} address.

      - name: "address2"
        type: "string"
        description: "An optional additional field for the street address of the {{ address-type }} address."

      - name: "city"
        type: "string"
        description: "The city of the {{ address-type }} address."

      - name: "company"
        type: "string"
        description: "The company of the person associated with the {{ address-type }} address."

      - name: "country"
        type: "string"
        description: "The name of the country of the {{ address-type }} address."

      - name: "first_name"
        type: "string"
        description: "The first name of the person associated with the payment method."

      - name: "last_name"
        type: "string"
        description: "The last name of the person associated with the payment method."

      - name: "phone"
        type: "string"
        description: "The phone number associated with the {{ address-type }} address."

      - name: "province"
        type: "string"
        description: "The name of the state or province of the {{ address-type }} address."

      - name: "zip"
        type: "string"
        description: "The zip or postal code of the {{ address-type }} address."

  - name: "charge_id"
    type: "integer"
    description: "The ID of the charge associated with the order."
    foreign-key-id: "charge-id"

  - name: "charge_status"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: "The date and time the order was created."

  - name: "customer_id"
    type: "integer"
    description: "The ID of the customer associated with the order."
    foreign-key-id: "customer-id"

  - name: "discount_codes"
    type: "array"
    description: "Details about the discounts applied to the order."
    subattributes:
      - name: "code"
        type: "string"
        description: "The title of the discount."

      - name: "amount"
        type: "string"
        description: "The amount of the discount."

      - name: "type"
        type: "string"
        description: "The type of the discount. For example: `percentage`"

  - name: "email"
    type: "string"
    description: "The email address of the customer associated with the order."

  - name: "first_name"
    type: "string"
    description: "The first name of the customer associated with the order."

  - name: "hash"
    type: "string"
    description: ""

  - name: "is_prepaid"
    type: "integer"
    description: "If true (`1`), the order has been paid for a pre-determined number of months."

  - name: "last_name"
    type: "string"
    description: "The last name of the customer associated with the order."

  - name: "line_items"
    type: "array"
    description: "Details about the items in the order."
    subattributes:
      - name: "grams"
        type: "integer"
        description: "The weight of the item, in grams."

      - name: "images"
        type: "object"
        description: "Images associated with the item."
        subattriubtes:
          - name: "large"
            type: "string"
            description: "The URL of the large image associated with the item."

          - name: "medium"
            type: "string"
            description: "The URL of the medium image associated with the item."

          - name: "original"
            type: "string"
            description: "The URL of the original image associated with the item."

          - name: "small"
            type: "string"
            description: "The URL of the small image associated with the item."

      - name: "price"
        type: "string"
        description: "The price of the item."

      - name: "properties"
        type: "array"
        description: "Custom information for an item that has been added to the cart."
        subattributes:
          - name: "name"
            type: "string"
            description: ""

          - name: "value"
            type: "string"
            description: ""

      - name: "quantity"
        type: "integer"
        description: "The number of products that were purchased."

      - name: "shopify_product_id"
        type: "string"
        description: "The ID of the Shopify product."
        foreign-key-id: "product-id"

      - name: "shopify_variant_id"
        type: "string"
        description: "The ID of the Shopify product variant."
        foreign-key-id: "variant-id"

      - name: "sku"
        type: "string"
        description: "A unique identifier of the item in the fulfillment."

      - name: "subscription_id"
        type: "integer"
        description: "The ID of the subscription associated with the charge."
        foreign-key-id: "subscription-id"

      - name: "title"
        type: "string"
        description: "The title of the product."

      - name: "variant_title"
        type: "string"
        description: "The title of the product variant."

  - name: "note"
    type: "string"
    description: ""

  - name: "note_attributes"
    type: "array"
    description: ""
    subattributes: &name-value
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "payment_processor"
    type: "string"
    description: "The type of payment the processor has chosen."

  - name: "processed_at"
    type: "date-time"
    description: "The date when the order was submitted."

  - name: "scheduled_at"
    type: "date-time"
    description: "The date when the order will ship."

  - name: "shipped_date"
    type: "date-time"
    description: "The date when the order shipped."

  - name: "shipping_address"
    type: "object"
    description: |
      The shipping information related to the order.
      {% assign address-type = "shipping" %}
    subattributes: *address

  - name: "shipping_date"
    type: "date-time"
    description: "The date when the order will be processed and sent to Shopify."

  - name: "shipping_lines"
    type: "array"
    description: "Details about the shipping used for the order."
    subattributes: &shipping-lines
      - name: "code"
        type: "string"
        description: "A reference to the shipping used."

      - name: "price"
        type: "string"
        description: "The price of the shipping used."

      - name: "title"
        type: "string"
        description: "The title of the shipping used."

  - name: "shopify_cart_token"
    type: "string"
    description: "The token generated by Shopify when an item is added to the order cart."

  - name: "shopify_customer_id"
    type: "string"
    description: "The ID of the customer in Shopify."
    foreign-key-id: "shopify-customer-id"

  - name: "shopify_id"
    type: "string"
    description: "**This field has been deprecated by {{ integration.display_name }}.** The ID of the order in Shopify."

  - name: "shopify_order_id"
    type: "string"
    description: "The ID of the order in Shopify."
    foreign-key-id: "shopify-order-id"

  - name: "shopify_order_number"
    type: "integer"
    description: "The order number in Shopify."

  - name: "status"
    type: "string"
    description: "The status of creating the order in Shopify."

  - name: "subtotal_price"
    type: "string"
    description: "The sum of all of the prices of the items in the order, including taxes and discounts."

  - name: "tags"
    type: "string"
    description: ""

  - name: "tax_lines"
    type: "array"
    description: "Details about the tax lines associated with the order."
    subattributes:
      - name: "code"
        type: "string"
        description: "The code of the tax to be applied."

      - name: "price"
        type: "string"
        description: "The price of the tax to be applied."

      - name: "title"
        type: "string"
        description: "The title of the tax to be applied."

  - name: "total_discounts"
    type: "number"
    description: "The sum of total discounts applied to the order."

  - name: "total_line_items_price"
    type: "number"
    description: ""

  - name: "total_price"
    type: "string"
    description: ""

  - name: "total_refunds"
    type: "number"
    description: "The sum of all refunds applied against the order."

  - name: "total_tax"
    type: "number"
    description: "The sum of total tax applied to the order."

  - name: "total_weight"
    type: "integer"
    description: "The sum of all products in the order."

  - name: "transaction_id"
    type: "string"
    description: "The ID of the transaction associated with the order."
    foreign-key-id: "transaction-id"

  - name: "type"
    type: "string"
    description: |
      Indicates if the order was made from checkout or a recurring charge. Possible values are:

      - `CHECKOUT`
      - `RECURRING`
---