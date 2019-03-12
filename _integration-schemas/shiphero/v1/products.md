---
tap: "shiphero"
version: "1.0"

name: "products"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-shiphero/blob/master/tap_shiphero/schemas/products.json"
description: |
  The `{{ table.name }}` table contains info about the products in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"
api-method:
    name: "Get products"
    doc-link: "https://shipheropublic.docs.apiary.io/#reference/products/get-product/get-product"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "product-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the product was last updated."

  - name: "account_id"
    type: "integer"
    description: ""

  - name: "active"
    type: "boolean"
    description: "Indicates if the product is active."

  - name: "barcode"
    type: "string"
    description: "The product's barcode."

  - name: "brand"
    type: "string"
    description: "The brand of the product."

  - name: "country_of_manufacture"
    type: "string"
    description: "The country of manufucture for the product."

  - name: "created_at"
    type: "date-time"
    description: "The time the product was created."

  - name: "custom"
    type: "integer"
    description: ""

  - name: "customs_description"
    type: "string"
    description: "The description of the product for customs."

  - name: "customs_value"
    type: "number"
    description: "The value of the product for customs."

  - name: "do_not_count"
    type: "boolean"
    description: ""

  - name: "dropship"
    type: "integer"
    description: ""

  - name: "final_sale"
    type: "boolean"
    description: "Indicates if the product is final sale."

  - name: "height"
    type: "number"
    description: "The height of the product."

  - name: "ignore_on_customs"
    type: "boolean"
    description: ""

  - name: "ignore_on_invoice"
    type: "boolean"
    description: ""

  - name: "images"
    type: "array"
    description: "Images associated with the product."
    array-attributes:
      - name: "sort"
        type: "integer"
        description: "The sort order of the image."

      - name: "url"
        type: "string"
        description: "The URL of the image."

  - name: "kit"
    type: "boolean"
    description: "The kit associated with the product."

  - name: "kit_build"
    type: "boolean"
    description: ""

  - name: "kit_components"
    type: "array"
    description: "The components of the kit associated with the order."
    array-attributes:
      - name: "quantity"
        type: "integer"
        description: "The quantity."

      - name: "sku"
        type: "string"
        description: "The SKU."

  - name: "length"
    type: "number"
    description: "The length of the product."

  - name: "name"
    type: "string"
    description: "The name of the product."

  - name: "no_air"
    type: "boolean"
    description: ""

  - name: "option"
    type: "string"
    description: ""

  - name: "price"
    type: "number"
    description: "The price of the product."

  - name: "product_note"
    type: "string"
    description: ""

  - name: "reorder_amount"
    type: "integer"
    description: ""

  - name: "reorder_level"
    type: "integer"
    description: ""

  - name: "reserve_inventory"
    type: "integer"
    description: ""

  - name: "sku"
    type: "string"
    description: "The SKU of the product."

  - name: "tags"
    type: "array"
    description: "Tags associated with the product."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The tag."

  - name: "tariff_code"
    type: "string"
    description: ""

  - name: "thumbnail"
    type: "string"
    description: ""

  - name: "value"
    type: "number"
    description: ""

  - name: "value_currency"
    type: "string"
    description: ""

  - name: "virtual"
    type: "boolean"
    description: "Indicates if the product is digital."

  - name: "warehouses"
    type: "array"
    description: "Details about the warehoues associated with the product."
    array-attributes:
      - name: "id"
        type: "integer"
        primary-key: true
        description: "The warehouse ID."
        foreign-key-id: "warehouse-id"

      - name: "active"
        type: "number"
        description: "Indicates if the warehouse is active."

      - name: "allocated"
        type: "integer"
        description: ""

      - name: "available"
        type: "number"
        description: ""

      - name: "backorder"
        type: "integer"
        description: ""

      - name: "customs_value"
        type: "number"
        description: ""

      - name: "inventory_bin"
        type: "string"
        description: ""

      - name: "inventory_overstock_bin"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "on_hand"
        type: "integer"
        description: ""

      - name: "price"
        type: "number"
        description: ""

      - name: "purchase_orders"
        type: "array"
        description: ""
        array-attributes:
          - name: "expected_date"
            type: "date-time"
            description: ""

          - name: "po_id"
            type: "string"
            description: ""

          - name: "quantity"
            type: "integer"
            description: ""

          - name: "quantity_received"
            type: "integer"
            description: ""

          - name: "sell_ahead"
            type: "integer"
            description: ""

      - name: "sell_ahead"
        type: "number"
        description: ""

      - name: "value"
        type: "number"
        description: ""

      - name: "value_currency"
        type: "string"
        description: ""

      - name: "warehouse"
        type: "string"
        description: ""

      - name: "warehouse_id"
        type: "integer"
        description: ""

  - name: "weight"
    type: "number"
    description: "The weight of the product."

  - name: "weight_in_oz"
    type: "number"
    description: "The weight of the product in ounces."

  - name: "width"
    type: "number"
    description: "The width of the product."
---