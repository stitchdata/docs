---
tap: "recharge"
version: "1"
key: "charge"

name: "charges"
doc-link: "https://developer.rechargepayments.com/#list-charges"
singer-schema: "https://github.com/singer-io/tap-recharge/blob/master/tap_recharge/schemas/charges.json"
description: |
  The `{{ table.name }}` table contains info about charges. A charge is a placeholder for an upcoming charge once the charge is processed successfully.

replication-method: "Key-based Incremental"
api-method:
  name: "List charges"
  doc-link: "https://developer.rechargepayments.com/#list-charges"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The charge ID."
    foreign-key-id: "charge-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The date and time the charge was last updated."

  - name: "address_id"
    type: "integer"
    description: ""
    foreign-key-id: "address-id"

  - name: "billing_address"
    type: "object"
    description: |
      The billing information related to the charge.
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

  - name: "browser_ip"
    type: "string"
    description: ""

  - name: "client_details"
    type: "object"
    description: ""
    subattributes:
      - name: "browser_ip"
        type: "string"
        description: ""

      - name: "user_agent"
        type: "string"
        description: ""

  - name: "created_at"
    type: "date-time"
    description: "The date and time the charge was created."

  - name: "customer_hash"
    type: "string"
    description: ""

  - name: "customer_id"
    type: "integer"
    description: "The ID of the customer associated with the charge."
    foreign-key-id: "customer-id"

  - name: "discount_codes"
    type: "array"
    description: "Details about discounts applied to the charge."
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
    description: "The email address associated with the charge."

  - name: "first_name"
    type: "string"
    description: "The first name of the customer associated with the charge."

  - name: "has_uncommited_changes"
    type: "boolean"
    description: ""

  - name: "last_name"
    type: "string"
    description: "The last name of the customer associated with the charge."

  - name: "line_items"
    type: "array"
    description: "Details about the items in the charge."
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
    description: "Shows the next order in sequence."

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

  - name: "processed_at"
    type: "date-time"
    description: "The date and time when the transaction was created."

  - name: "processor_name"
    type: "string"
    description: "The name of the processor of the charge."

  - name: "scheduled_at"
    type: "date-time"
    description: "The date the charge is scheduled for."

  - name: "shipments_count"
    type: "integer"
    description: "The number of successfully sent orders for the specific charge."

  - name: "shipping_address"
    type: "object"
    description: |
      The shipping information related to the charge.
      {% assign address-type = "shipping" %}
    subattributes: *address

  - name: "shipping_lines"
    type: "array"
    description: "Details about the shipping used for the charge."
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

  - name: "shopify_order_id"
    type: "string"
    description: "The ID of the charge within Shopify."
    foreign-key-id: "shopify-order-id"

  - name: "status"
    type: "string"
    description: |
      The status of creating the charge within Shopify. Possible values are:

      - `SUCCESS`
      - `ERROR`
      - `QUEUED`
      - `SKIPPED`
      - `REFUNDED`
      - `PARTIALLY_REFUNDED`

  - name: "sub_total"
    type: "string"
    description: ""

  - name: "subtotal_price"
    type: "string"
    description: "The item price without taxes and discounts."

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
    type: "string"
    description: "The sum of the discounts applied to the product."

  - name: "total_line_items_price"
    type: "string"
    description: ""

  - name: "total_price"
    type: "string"
    description: "The sum of all the prices of all the items in the charge, including taxes and discounts."

  - name: "total_refunds"
    type: "number"
    description: "The sum of all refunds that were made on specific charge."

  - name: "total_tax"
    type: "number"
    description: "The sum of the taxes applied to the product."

  - name: "total_weight"
    type: "integer"
    description: ""

  - name: "transaction_id"
    type: "string"
    description: "The ID of the transaction associated with the charge."
    foreign-key-id: "transaction-id"

  - name: "type"
    type: "string"
    description: "The type of the charge."
---