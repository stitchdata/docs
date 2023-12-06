---
tap: "recharge"
version: "1"
key: "product"

name: "products"
doc-link: "https://developer.rechargepayments.com/#list-products-beta"
singer-schema: "https://github.com/singer-io/tap-recharge/blob/master/tap_recharge/schemas/products.json"
description: |
  The `{{ table.name }}` table contains info about your products.

replication-method: "Key-based Incremental"
api-method:
  name: "List products"
  doc-link: "https://developer.rechargepayments.com/#list-products-beta"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The product ID."
    foreign-key-id: "product-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The date and time the product was last updated."

  - name: "collection_id"
    type: "integer"
    description: "The ID of the ruleset created in {{ integration.display_name }}."
    foreign-key-id: "collection-id"

  - name: "created_at"
    type: "date-time"
    description: "The date and time the product was created."

  - name: "discount_amount"
    type: "number"
    description: "The discount amount applied based on the {{ integration.display_name }} ruleset."

  - name: "discount_type"
    type: "string"
    description: "The type of discount applied to the product. For example: `percentage`"

  - name: "images"
    type: "object"
    description: "Images of the product in Shopify."
    subattributes:
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

  - name: "product_id"
    type: "integer"
    description: "**This field has been deprecated by {{ integration.display_name }}. Use `shopify_product_id` instead.** The ID of the product in Shopify."
    # foreign-key-id: "product-id"

  - name: "shopify_product_id"
    type: "integer"
    description: "The ID of the product in Shopify."
    # foreign-key-id: "product-id"

  - name: "subscription_defaults"
    type: "object"
    description: "Defaults applied to subscription products."
    subattributes:
      - name: "charge_interval_frequency"
        type: "integer"
        description: "The number of units (specified in `order_interval_unit`) between each charge."

      - name: "cutoff_day_of_month"
        type: "string"
        description: "The number of the day in a month on which customers will be charged. Cut-off windows create an interval between the day a customer goes through {{ integration.display_name }} checkout to purchase a new subscription and when you charge that customer again for their recurring order. Possible values are `1` through `31`."

      - name: "cutoff_day_of_week"
        type: "string"
        description: |
          The number of the day in a week on which customers will be charged. Cut-off windows create an interval between the day a customer goes through {{ integration.display_name }} checkout to purchase a new subscription and when you charge that customer again for their recurring order.

          Possible values are:

          - `0`: Monday
          - `1`: Tuesday
          - `2`: Wednesday
          - `3`: Thursday
          - `4`: Friday
          - `5`: Saturday
          - `6`: Sunday

      - name: "expire_after_specific_number_of_charges"
        type: "integer"
        description: "The number of charges until the subscription expires."

      - name: "handle"
        type: "string"
        description: ""

      - name: "number_charges_until_expiration"
        type: "integer"
        description: "**This field has been deprecated by {{ integration.display_name }}. Use `expire_after_specific_number_of_charges` instead.**"

      - name: "order_day_of_month"
        type: "string"
        description: "**Applicable only to subscriptions where `order_interval_unit: month`**. The set day of the month the order is created."

      - name: "order_day_of_week"
        type: "string"
        description: "**Applicable only to subscriptions where `order_interval_unit: week`**. The set day of the week the order is created. A value of `0` equals Monday, `1` equals Tuesday, etc."

      - name: "order_interval_frequency"
        type: "integer"
        description: "The number of units (specified in `order_interval_unit`) between each order. For example: If `order_interval_unit: month` and `order_interval_frequency: 3`, there'd be an order every three months."

      - name: "order_interval_frequency_options"
        type: "array"
        description: "The order interval frequency options customers can choose from."
        subattributes:
          - name: "value"
            type: "string"
            description: "The order interval frequency option."

      - name: "order_interval_unit"
        type: "string"
        description: |
          The frequency with which a subscription should have an order created. Possible values are:

          - `days`
          - `weeks`
          - `months`

      - name: "storefront_purchase_options"
        type: "string"
        description: |
          The purchase options for the subscription. Possible values are:

          - `subscription_only`: Products are only offered as a recurring subscription item
          - `subscription_and_onetime`: Products will have the option of being purchased as a one-time or as a recurring subscription item.

  - name: "title"
    type: "string"
    description: "The title of the product in Shopify."
---