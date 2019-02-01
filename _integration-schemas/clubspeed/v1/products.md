---
tap: "clubspeed"
version: "1.0"

name: "products"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/products.json"
description: |
  The `{{ table.name }}` table contains info about products.

replication-method: "Full Table"

attributes:
  - name: "productId"
    type: "integer"
    primary-key: true
    description: "The product ID."
    foreign-key-id: "product-id"

  - name: "deleted"
    type: "boolean"
    description: "Indicates whether the product has been soft deleted."

  - name: "description"
    type: "string"
    description: "The description of the product."

  - name: "enabled"
    type: "boolean"
    description: "Indicates whether the product is currently enabled."

  - name: "g_Points"
    type: "number"
    description: "The amount of gift card points provided when this product is purchased."

  - name: "p_Points"
    type: "number"
    description: "The number of points provided when this product is purchased."

  - name: "price1"
    type: "number"
    description: "The price of the product."

  - name: "price2"
    type: "number"
    description: ""

  - name: "priceCadet"
    type: "number"
    description: ""

  - name: "productClassId"
    type: "integer"
    description: "The ID of the reporting product class for the product."
    foreign-key-id: "product-class-id"

  - name: "productType"
    type: "integer"
    description: |
      The type of the product. Possible values are:

      - `1` - Regular
      - `2` - Point
      - `3` - Food
      - `4` - Reservation
      - `5` - GameCard
      - `6` - Membership
      - `7` - Gift Card
      - `8` - Entitle

  - name: "r_Points"
    type: "number"
    description: "The amount of reservation points provided when this product is purchased."

  - name: "taxId"
    type: "integer"
    description: "The tax ID for the product."
    foreign-key-id: "tax-id"
---