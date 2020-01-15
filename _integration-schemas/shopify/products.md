---
tap: "shopify"
version: "1"

name: "products"
doc-link: "https://help.shopify.com/en/api/reference/products/product"
singer-schema: "https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/products.json"
description: |
  The `{{ table.name }}` table contains info about a shop's products.

  #### Product metafield data

  To replicate product metafield data, you must set this table and the [`metafields`](#metafields) table to replicate.

replication-method: "Key-based Incremental"

api-method:
    name: "Retrieve a list of products"
    doc-link: "https://help.shopify.com/en/api/reference/products/product#index"

date-time: |
  The date and time in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601){:target="new"} when the [ITEM] was [ACTION].

attributes:
  # - name: "admin_graphql_api_id"
  #   type: "string"
  #   description: ""

  - name: "id"
    type: "integer"
    primary-key: true
    description: "The product ID."
    foreign-key-id: "product-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: |
      {{ table.date-time | replace: "[ITEM]","product" | replace: "[ACTION]","last updated" }}

  - name: "body_html"
    type: "string"
    description: "A description of the product."

  - name: "created_at"
    type: "date-time"
    description: |
      {{ table.date-time | replace: "[ITEM]","product" | replace: "[ACTION]","created" }}

  - name: "handle"
    type: "string"
    description: "The human-friendly string for the product, automatically generated from the product's `title`. This is used by Liquid templating to refer to objects."

  - name: "images"
    type: "array"
    description: "The product images associated with the product."
    doc-link: "https://help.shopify.com/en/api/reference/products/product_image"
    subattributes:
      # - name: "admin_graphql_api_id"
      #   type: "string"
      #   description: ""

      - name: "id"
        type: "integer"
        primary-key: true
        description: "The product image ID."

      - name: "alt"
        type: "string"
        description: "The alternative text for the product image."

      - name: "created_at"
        type: "date-time"
        description: |
          {{ table.date-time | replace: "[ITEM]","product image" | replace: "[ACTION]","created" }}

      - name: "height"
        type: "integer"
        description: "The height dimension of the product image."

      - name: "position"
        type: "integer"
        description: "The order of the product image in the list. The first product image is at position `1` and is the main image for the product."

      - name: "src"
        type: "string"
        description: "The location of the product image."

      - name: "updated_at"
        type: "date-time"
        description: |
          {{ table.date-time | replace: "[ITEM]","product image" | replace: "[ACTION]","last updated" }}

      - name: "variant_ids"
        type: "array"
        description: "The variant IDs associated with the product image."
        subattributes:
          - name: "value"
            type: "integer"
            description: "The variant ID."

      - name: "width"
        type: "integer"
        description: "The width dimension of the product image."

  - name: "options"
    type: "array"
    description: "The custom properties associated with the product, like `Size`, `Color`, etc."
    subattributes:
      - name: "id"
        type: "integer"
        primary-key: true
        description: "The custom property ID."

      - name: "name"
        type: "string"
        description: "The name of the custom property."

      - name: "position"
        type: "integer"
        description: "The order of the custom property in the list."

      - name: "product_id"
        type: "integer"
        primary-key: true
        description: "The ID of the product."
        foreign-key-id: "product-id"

      - name: "values"
        type: "array"
        description: "The values of the custom property."
        subattributes:
          - name: "value"
            type: "string"
            description: "The custom property value."

  - name: "product_type"
    type: "string"
    description: "The categorization for the product, used for filtering and searching."

  - name: "published_at"
    type: "date-time"
    description: |
      {{ table.date-time | replace: "[ITEM]","product" | replace: "[ACTION]","published" }}

  - name: "published_scope"
    type: "string"
    description: |
      Indicates whether the product is published to the Point of Sale channel. Possible values are:

      - `web` - The product is published to the Online Store channel but not published to the Point of Sale channel.
      - `global` - The product is published to both the Online Store channel and the Point of Sale channel.

  - name: "tags"
    type: "string"
    description: "The tags associated with the product."

  - name: "template_suffix"
    type: "string"
    description: "The suffix of the Liquid template applied to the product. The default template is `product.liquid`; any additional templates will be `product.suffix.liquid`"

  - name: "title"
    type: "string"
    description: "The product title."

  - name: "variants"
    type: "array"
    description: "The product variants associated with the product, each representing a different version of the product."
    doc-link: "https://help.shopify.com/en/api/reference/products/product_variant"
    subattributes:
      # - name: "admin_graphql_api_id"
      #   type: "string"
      #   description: ""
      - name: "id"
        type: "integer"
        primary-key: true
        description: "The product variant ID."

      - name: "barcode"
        type: "string"
        description: "The barcode, UPC, or ISBN number for the product."

      - name: "compare_at_price"
        type: "string"
        description: "The original price of the item before an adjustment or sale."

      - name: "created_at"
        type: "date-time"
        description: |
          {{ table.date-time | replace: "[ITEM]","product variant" | replace: "[ACTION]","created" }}

      - name: "fulfillment_service"
        type: "string"
        description: |
          The fulfillment service associated with the product variant. Possible values are `manual` or the handle of a [fulfillment service](https://help.shopify.com/api/reference/fulfillmentservice){:target="new"}.

      - name: "grams"
        type: "integer"
        description: "The weight of the product variant in grams."

      - name: "image_id"
        type: "integer"
        description: "The ID for the product image associated with the product variant."

      - name: "inventory_item_id"
        type: "integer"
        description: "The ID for the inventory item."

      - name: "inventory_management"
        type: "string"
        description: |
          The fulfillment service that tracks the number of items in stock for the product variant. Possible values are `shopify` or the handle of [fulfillment service](https://help.shopify.com/api/reference/fulfillmentservice){:target="new"} that has inventory management enabled.

      - name: "inventory_policy"
        type: "string"
        description: |
          Indicates whether customers are allowed to place an order for the product variant when it's out of stock. Possible values are:

          - `deny` - Customers are not allowed to place orders for the product variant if it's out of stock.
          - `continue` - Customers are allowed to place orders for the product variant if it's out of stock.

      - name: "inventory_quantity"
        type: "integer"
        description: "An aggregate of inventory across all locations."

      - name: "old_inventory_quantity"
        type: "integer"
        description: "**This attribute has been deprecated by {{ integration.display_name }}.**"

      - name: "option1"
        type: "string"
        description: &custom-variant-property "A custom property option associated with the product variant."

      - name: "option2"
        type: "string"
        description: *custom-variant-property

      - name: "option3"
        type: "string"
        description: *custom-variant-property

      - name: "position"
        type: "integer"
        description: "The order of the product variant in the list of product variants. The first position in the list is `1`."

      - name: "price"
        type: "string"
        description: "The price of the product variant."

      - name: "requires_shipping"
        type: "boolean"
        description: "Indicates whether a customer needs to provide a shipping address when placing an order for the product variant."

      - name: "sku"
        type: "string"
        description: "The product variant's Stock Keeping Unit (SKU)."

      - name: "tax_code"
        type: "string"
        description: |
          **Only applicable to shops that have the [Avalara AvaTax](https://help.shopify.com/en/manual/taxes/tax-services/taxation){:target="new"} installed**. The Avalara tax code for the product variant.

      - name: "taxable"
        type: "boolean"
        description: "Indicates if a tax is charged when the product variant is sold."

      - name: "title"
        type: "string"
        description: "The title of the product variant."

      - name: "updated_at"
        type: "date-time"
        description: |
          {{ table.date-time | replace: "[ITEM]","product variant" | replace: "[ACTION]","last updated" }}

      - name: "weight"
        type: "number"
        description: "The weight of the product variant in the unit system, specified with `weight_unit`."

      - name: "weight_unit"
        type: "string"
        description: |
          The unit of measurement that applies to the product variant's `weight`. Possible values are:

          - `g` - Grams
          - `kg` - Kilograms
          - `oz` - Ounces
          - `lb` - Pounds

  - name: "vendor"
    type: "string"
    description: "The name of the product's vendor."
---