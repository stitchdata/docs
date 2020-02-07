---
tap: "shopify"
version: "1"

name: "order_refunds"
doc-link: "https://help.shopify.com/en/api/reference/orders/refund"
singer-schema: "https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/order_refunds.json"
description: |
  The `{{ table.name }}` table contains info about refunds associated with orders.

replication-method: "Key-based Incremental"

api-method:
    name: "Retrieve all refunds from a specific order"
    doc-link: "https://help.shopify.com/en/api/reference/orders/refund#index"

date-time: |
  The date and time in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601){:target="new"} when the [ITEM] was [ACTION].

attributes:
  # - name: "admin_graphql_api_id"
  #   type: "string"
  #   description: ""

  - name: "id"
    type: "integer"
    primary-key: true
    description: "The refund ID."
    foreign-key-id: "order-refund-id"

  - name: "created_at"
    type: "string"
    replication-key: true
    description: |
      {{ table.date-time | replace: "[ITEM]","refund" | replace: "[ACTION]","created" }}

  - name: "note"
    type: "string"
    description: "An optional note attached to a refund."

  - name: "order_id"
    type: "integer"
    description: "The ID of the order the refund is associated with."
    foreign-key-id: "order-id"

  - name: "processed_at"
    type: "string"
    description: |
      {{ table.date-time | replace: "[ITEM]","refund" | replace: "[ACTION]","processed" }}

  - name: "refund_line_items"
    type: "array"
    description: "Details about the line items associated with the refund."
    subattributes:
      - name: "id"
        type: "integer"
        primary-key: true
        description: "The ID of the refund line item."

      - name: "line_item"
        type: "object"
        description: "Details about the line item."
        subattributes:
          # - name: "admin_graphql_api_id"
          #   type: "string"
          #   description: ""

          - name: "id"
            type: "integer"
            description: "The line item ID."

          - name: "discount_allocations"
            type: "array"
            description: "An ordered list of amounts allocated by discount applications. Each discount allocation is associated to a particular appliction."
            subattributes:
              - name: "amount"
                type: "string"
                description: "The discount amount allocated to the line."

              - name: "amount_set"
                type: "object"
                description: "The presentment and shop amounts associated with the line item."
                subattributes:
                  - name: "presentment_money"
                    type: "object"
                    description: "Details about the presentment amount associated with the line item."
                    anchor-id: 1
                    subattributes: &presentment-money
                      - name: "amount"
                        type: "string"
                        description: "The presentment amount."

                      - name: "currency_code"
                        type: "string"
                        description: |
                          The three-letter [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217){:target="new"} code for the presentment amount.

                  - name: "shop_money"
                    type: "object"
                    description: "Details about the shop amount associated with the line item."
                    anchor-id: 2
                    subattributes: &shop-money
                      - name: "amount"
                        type: "string"
                        description: "The shop amount."

                      - name: "currency_code"
                        type: "string"
                        description: |
                          The three-letter [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217){:target="new"} code for the shop amount.

              - name: "discount_application_index"
                type: "integer"
                description: "The index of the associated discount application in the order's `discount_allocations` list."

          - name: "fulfillable_quantity"
            type: "integer"
            description: |
              The amount available to fulfill, calculated as follows:

              _quantity - max(refunded_quantity, fulfilled_quantity) - pending_fulfilled_quantity - open_fulfilled_quantity_

          - name: "fulfillment_service"
            type: "string"
            description: "The service provider that fulfilled the item. Possible values are `manual` or the name of the provider, such as `amazon` or `shipwire`"

          - name: "fulfillment_status"
            type: "string"
            description: |
              The line item's fulfillment status. Possible values are:

              - `shipped`
              - `partial`
              - `unshipped`

          - name: "gift_card"
            type: "boolean"
            description: "Indicates whether the line item is a gift card."

          - name: "grams"
            type: "integer"
            description: "The weight of the item in grams."

          - name: "name"
            type: "string"
            description: "The name of the product variant."

          - name: "pre_tax_price"
            type: "string"
            description: "The pre-tax price of the item."

          - name: "pre_tax_price_set"
            type: "object"
            description: "Presentment and shop money details associated with the pre-tax price for the line item."
            subattributes:
              - name: "presentment_money"
                type: "object"
                description: "Details about the presentment amount associated with the pre-tax price."
                anchor-id: 2
                subattributes: *presentment-money

              - name: "shop_money"
                type: "object"
                description: "Details about the shop amount associated with the pre-tax price."
                anchor-id: 2
                subattributes: *shop-money

          - name: "price"
            type: "string"
            description: "The price of the item before discounts were applied."

          - name: "price_set"
            type: "object"
            description: "Presentment and shop money details associated with the price for the line item."
            subattributes:
              - name: "presentment_money"
                type: "object"
                description: "Details about the presentment amount associated with the price."
                anchor-id: 3
                subattributes: *presentment-money

              - name: "shop_money"
                type: "object"
                description: "Details about the shop amount associated with the price."
                anchor-id: 3
                subattributes: *shop-money

          - name: "product_exists"
            type: "boolean"
            description: "Indicates whether the product exists."

          - name: "product_id"
            type: "integer"
            description: "The product ID."
            foreign-key-id: "product-id"

          - name: "properties"
            type: "array"
            description: "Details about custom info for the item."
            subattributes:
              - name: "name"
                type: "string"
                description: ""

              - name: "value"
                type: "string"
                description: ""

          - name: "quantity"
            type: "integer"
            description: "The number of items purchased."

          - name: "requires_shipping"
            type: "boolean"
            description: "Indicates if the line item requires shipping."

          - name: "sku"
            type: "string"
            description: "The item's SKU."

          - name: "tax_lines"
            type: "array"
            description: "Details about the line item's tax lines, each of which details a tax applicable to this line item."
            subattributes:
              - name: "price"
                type: "string"
                description: "The amount of tax to be charged."

              - name: "price_set"
                type: "object"
                description: "Presentment and shop money details associated with the price for the tax line."
                subattributes:
                  - name: "presentment_money"
                    type: "object"
                    description: "Details about the presentment amount associated with the tax line price."
                    anchor-id: 4
                    subattributes: *presentment-money

                  - name: "shop_money"
                    type: "object"
                    description: "Details about the shop amount associated with the tax line price."
                    anchor-id: 4
                    subattributes: *shop-money

              - name: "rate"
                type: "number"
                description: "The rate of tax to be applied."

              - name: "title"
                type: "string"
                description: "The name of the tax."

          - name: "taxable"
            type: "boolean"
            description: "Indicates if the item is taxable."

          - name: "title"
            type: "string"
            description: "The title of the product."

          - name: "total_discount"
            type: "string"
            description: "The total of any discounts applied to the line item."

          - name: "total_discount_set"
            type: "object"
            description: "Presentment and shop money details associated with the total discount for the line item."
            subattributes:
              - name: "presentment_money"
                type: "object"
                description: "Details about the presentment amount associated with the total discount."
                anchor-id: 5
                subattributes: *presentment-money

              - name: "shop_money"
                type: "object"
                description: "Details about the shop amount associated with the total discount."
                anchor-id: 5
                subattributes: *shop-money

          - name: "variant_id"
            type: "integer"
            description: "The product variant ID."

          - name: "variant_inventory_management"
            type: "string"
            description: "The name of the inventory management system."

          - name: "variant_title"
            type: "string"
            description: "The title of the product variant."

          - name: "vendor"
            type: "string"
            description: "The name of the item's supplier."

      - name: "line_item_id"
        type: "integer"
        description: "The ID of the related line item in the order."
        foreign-key-id: "line-item-id"

      - name: "location_id"
        type: "integer"
        description: "The ID of the physical location where the items will be restocked."

      - name: "quantity"
        type: "integer"
        description: "The quantity of the associated line item that was returned."

      - name: "restock_type"
        type: "string"
        description: |
          Indicates how the refund line item will affect inventory levels. Possible values are:

          - `no_restock` - Refunding these items won't affect inventory. The number of fulfillable units for this line item will remain unchanged. For example: A refund payment can be issued but no items will be returned or made available for sale again.
          - `cancel` - The items have not yet been fulfilled. The canceled quantity will be added back to the available count. The number of fulfillable units for this line item will decrease.
          - `return` - The items were already delivered, and will be returned to the merchant. The returned quantity will be added back to the available count. The number of fulfillable units for this line item will remain unchanged.
          - `legacy_restock` - **Deprecated by Shopify.** These items were made available for sale again.

      - name: "subtotal"
        type: "number"
        description: "The subtotal of the refund line item."

      - name: "subtotal_set"
        type: "object"
        description: "Presentment and shop money details associated with the subtotal for the line item."
        subattributes:
          - name: "presentment_money"
            type: "object"
            description: "Details about the presentment amount associated with the subtotal."
            anchor-id: 6
            subattributes: *presentment-money

          - name: "shop_money"
            type: "object"
            description: "Details about the shop amount associated with the subtotal."
            anchor-id: 6
            subattributes: *shop-money

      - name: "total_tax"
        type: "number"
        description: "The total tax on the refund line item."

      - name: "total_tax_set"
        type: "object"
        description: "Presentment and shop money details associated with the total tax for the line item."
        subattributes:
          - name: "presentment_money"
            type: "object"
            description: "Details about the presentment amount associated with the total tax."
            anchor-id: 7
            subattributes: *presentment-money

          - name: "shop_money"
            type: "object"
            description: "Details about the shop amount associated with the total tax."
            anchor-id: 7
            subattributes: *shop-money

  - name: "restock"
    type: "boolean"
    description: "Indicates whether line items will be added back to the store's inventory."

  - name: "user_id"
    type: "integer"
    description: "The ID of the user who performed the refund."
---