---
tap: "recharge"
version: "1"
key: "subscription"

name: "subscriptions"
doc-link: "https://developer.rechargepayments.com/#list-subscriptions"
singer-schema: "https://github.com/singer-io/tap-recharge/blob/master/tap_recharge/schemas/subscriptions.json"
description: |
  The `{{ table.name }}` table contains info about subscriptions. Subscriptions are individual items that customers receive on a recurring basis.

replication-method: "Key-based Incremental"
api-method:
  name: "List subscriptions"
  doc-link: "https://developer.rechargepayments.com/#list-subscriptions"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the subscription."
    foreign-key-id: "subscription-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The date and time the subscription was created."

  - name: "address_id"
    type: "integer"
    description: "The ID of the address the subscription is associated with."
    foreign-key-id: "address-id"

  - name: "cancellation_reason"
    type: "string"
    description: "The reason for the subscription cancellation."

  - name: "cancellation_reason_comments"
    type: "string"
    description: "Additional information about cancellation."

  - name: "cancelled_at"
    type: "date-time"
    description: "The time the subscription was canceled."

  - name: "charge_interval_frequency"
    type: "string"
    description: "The number of units (specified in `order_interval_unit`) between each charge."

  - name: "created_at"
    type: "date-time"
    description: "The date and time the subscription was created."

  - name: "customer_id"
    type: "integer"
    description: "The ID of the customer associated with the subscription."
    foreign-key-id: "customer-id"

  - name: "expire_after_specific_number_of_charges"
    type: "integer"
    description: "The number of charges until the subscription expires."

  - name: "has_queued_charges"
    type: "integer"
    description: "Indicates if the subscription has a queued charge. If `1`, there's a queued charge."

  - name: "is_skippable"
    type: "boolean"
    description: "If `true`, the item is not a prepaid item."

  - name: "is_swappable"
    type: "boolean"
    description: "If `true`, the item isn't a prepaid item and swapping is allowed for customers in the Customer portal settings."

  - name: "max_retries_reached"
    type: "integer"
    description: "Indicates if the charge on the subscription has reached the maximum number of error retries. If `1`, the maximum has been reached."

  - name: "next_charge_scheduled_at"
    type: "date-time"
    description: "The date of the next charge for subscription."

  - name: "order_day_of_month"
    type: "string"
    description: "**Applicable only to subscriptions where `order_interval_unit: month`**. The set day of the month the order is created."

  - name: "order_day_of_week"
    type: "string"
    description: "**Applicable only to subscriptions where `order_interval_unit: week`**. The set day of the week the order is created. A value of `0` equals Monday, `1` equals Tuesday, etc."

  - name: "order_interval_frequency"
    type: "string"
    description: "The number of units (specified in `order_interval_unit`) between each order. For example: If `order_interval_unit: month` and `order_interval_frequency: 3`, there'd be an order every three months."

  - name: "order_interval_unit"
    type: "string"
    description: |
      The frequency with which a subscription should have order created. Possible values are:

      - `day`
      - `week`
      - `month`

  - name: "price"
    type: "number"
    description: "The price of the item before discounts, taxes, or shipping have been applied."

  - name: "product_title"
    type: "string"
    description: "The name of the product in a shop’s catalog."

  - name: "properties"
    type: "array"
    description: "A list of line item objects, each one containing information about the subscription."
    subattributes: &name-value
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "quantity"
    type: "integer"
    description: "The number of items on the subscription."

  - name: "recharge_product_id"
    type: "integer"
    description: "The ID of the product in {{ integration.display_name }}."

  - name: "shopify_product_id"
    type: "integer"
    description: "The ID of the product in Shopify."
    foreign-key-id: "product-id"

  - name: "shopify_variant_id"
    type: "integer"
    description: "The ID of the product variant in Shopify."
    foreign-key-id: "variant-id"

  - name: "sku"
    type: "string"
    description: "A unique identifier of the item in the fulfillment."

  - name: "sku_override"
    type: "string"
    description: |
      If `true`, the SKU on the subscription will be used to generate charges and orders. If `false`, {{ integration.display_name }} will dynamically fetch the SKU from the corresponding Shopify variant.

  - name: "status"
    type: "string"
    description: |
      The status of the subscription. Possible values are:

      - `active`
      - `cancelled`
      - `expired`

  - name: "variant_title"
    type: "string"
    description: "The name of the variant in a shop’s catalog."
---