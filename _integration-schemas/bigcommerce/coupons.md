---
tap: "bigcommerce"
version: "1.0"

name: "coupons"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-bigcommerce/blob/master/tap_bigcommerce/schemas/coupons.json"
description: |
  The `{{ table.name }}` table contains info about the coupons in your {{ integration.display_name }} store.

  {% capture replication-tip %}
  This table uses Full Table Replication, which means all records will be replicated during every replication job.

  To avoid re-replicating unnecessary data, create a second {{ integration.display_name }} integration in your Stitch account (you can even use the same {{ integration.display_name }} API credentials) and set the integration to replicate every 12 or 24 hours.
  {% endcapture %}

  {% include tip.html content=replication-tip %}

replication-method: "Full Table"
api-method:
  name: "Get all coupons"
  doc-link: "https://developer.bigcommerce.com/api-reference/marketing/marketing-api/coupons/getallcoupons"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The coupon ID."
    foreign-key-id: "coupon-id"

  - name: "amount"
    type: "number"
    description: |
      The discount to apply to an order as either an amount or a percentage. This field is determined by the coupon's `type`.

      For example: If `type: percentage_discount`, this value would represent a percentage discount.

  - name: "applies_to"
    type: "object"
    description: "A list of product or category IDs the coupon can be applied to. The value of the `applies_to__entity` field indicates whether these are product or category IDs."
    subattributes:
      - name: "entity"
        type: "string"
        description: "The type of entity. For example: `product`"

      - name: "ids"
        type: "array"
        description: "The list of IDs the coupon can be applied to. The value of the `entity` field indicates whether these are product or category IDs."
        subattributes:
          - name: "value"
            type: "integer"
            primary-key: true
            description: "The product or category ID."

  - name: "code"
    type: "string"
    description: "The coupon code that customers will enter to receive the coupon's discount."

  - name: "date_created"
    type: "date-time"
    description: "The date the coupon was created, in RFC 2822 format."

  - name: "enabled"
    type: "boolean"
    description: "Indicates if the coupon is enabled."

  - name: "expires"
    type: "date-time"
    description: "The date the coupon was expires, in RFC 2822 format."

  - name: "max_uses"
    type: "integer"
    description: "The maximum number of times this coupon can be used."

  - name: "max_uses_per_customer"
    type: "integer"
    description: "The maximum number of times each customer can use the coupon."

  - name: "min_purchase"
    type: "number"
    description: "The minimum value that an order must have before the coupon can be applied."

  - name: "name"
    type: "string"
    description: "The name of the coupon."

  - name: "num_uses"
    type: "integer"
    description: "The number of times the coupon has been used."

  - name: "restricted_to"
    type: "array"
    description: &restricted-to "A list of countries that the coupon is restricted to."
    subattributes:
      - name: "countries"
        type: "array"
        description: *restricted-to
        subattributes:
          - name: "value"
            type: "string"
            description: "The country the coupon is restricted to."

  - name: "shipping_methods"
    type: "array"
    description: "A list of shipping method names."
    subattributes:
      - name: "value"
        type: "string"
        description: "The name of the shipping method."

  - name: "type"
    type: "string"
    description: |
      The type of coupon. Possible values are:

      - `per_item_discount`
      - `per_total_discount`
      - `shipping_discount`
      - `free_shipping`
      - `percentage_discount`
---