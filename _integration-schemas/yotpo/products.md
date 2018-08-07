---
tap: "yotpo"
version: "1.0"

name: "products"
doc-link: https://apidocs.yotpo.com/reference#introduction-to-products
singer-schema: https://github.com/singer-io/tap-yotpo/blob/master/tap_yotpo/schemas/products.json
description: |
  The `products` table contains data about products in the Yotpo system

replication-method: "Key-based Incremental"

api-method:
  name: Retrieve All Products
  doc-link: https://apidocs.yotpo.com/reference#retrieve-all-products

attributes:

  - name: "id"
    type: "integer"
    primary-key: true
    description: ""

  - name: "created_at"
    type: "string"
    description: ""

  - name: "updated_at"
    type: "string"
    description: ""

  - name: "average_score"
    type: "number"
    description: ""

  - name: "total_reviews"
    type: "number"
    description: ""

  - name: "url"
    type: "string"
    description: ""

  - name: "external_product_id"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "product_specs"
    type: "object"
    description: ""

    object-attributes: 
    - name: "key"
      type: "string"
      description: ""

    - name: "value"
      type: "string"
      description: ""

  - name: "category"
    type: "object"
    description: ""

    object-attributes: 
    - name: "id"
      type: "number"
      description: ""

    - name: "name"
      type: "string"
      description: ""

  - name: "images"
    type: "object"
    description: ""

    object-attributes: 
    - name: "original"
      type: "string"
      description: ""

    - name: "square"
      type: "string"
      description: ""

    - name: "facebook"
      type: "string"
      description: ""

    - name: "facebook_square"
      type: "string"
      description: ""

    - name: "kind"
      type: "string"
      description: ""
---
