---
tap: "yotpo"
version: "2"
key: ""

name: "products"
doc-link: https://apidocs.yotpo.com/reference#introduction-to-products
singer-schema: https://github.com/singer-io/tap-yotpo/tree/master/tap_yotpo/schemas/products.json
description: |
  The `{{ table.name }}` table contains data about products in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: Retrieve All Products
  doc-link: https://apidocs.yotpo.com/reference#retrieve-all-products

attributes:
  - name: "yotpo_id"
    type: "integer"
    primary-key: true
    description: "The Yotpo ID for the product."
    foreign-key-id: "product-id"

  - name: "brand"
    type: "string"
    description: ""

  - name: "compare_at_price"
    type: "number"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "custom_properties"
    type: "object"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "external_created_at"
    type: "date-time"
    description: ""

  - name: "external_id"
    type: "string"
    description: ""

  - name: "external_updated_at"
    type: "date-time"
    description: ""

  - name: "group_name"
    type: "string"
    description: ""

  - name: "gtins"
    type: "array"
    description: ""
    subattributes:
      - name: "declared_type"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""

      - name: "detected_type"
        type: "string"
        description: ""


  - name: "handle"
    type: "string"
    description: ""

  - name: "image_url"
    type: "string"
    description: ""

  - name: "inventory_quantity"
    type: "integer"
    description: ""

  - name: "is_discontinued"
    type: "boolean"
    description: ""

  - name: "is_valid_url_format"
    type: "boolean"
    description: ""

  - name: "mpn"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "price"
    type: "number"
    description: ""

  - name: "sku"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "updated_at"
    type: "date-time"
    description: ""

  - name: "url"
    type: "string"
    description: ""  
---