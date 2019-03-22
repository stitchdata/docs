---
tap: "yotpo"
version: "1.0"

name: "products"
doc-link: https://apidocs.yotpo.com/reference#introduction-to-products
singer-schema: https://github.com/singer-io/tap-yotpo/blob/master/tap_yotpo/schemas/products.json
description: |
  The `{{ table.name }}` table contains data about products in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: Retrieve All Products
  doc-link: https://apidocs.yotpo.com/reference#retrieve-all-products

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The product ID."
    foreign-key-id: "product-id"

  - name: "updated_at"
    type: "string"
    replication-key: true
    description: "The time the product was last updated."

  - name: "created_at"
    type: "string"
    description: "The time the product was created."

  - name: "average_score"
    type: "number"
    description: "The product's average score, based on reviews."

  - name: "total_reviews"
    type: "number"
    description: "The total number of reviews associated with the product."

  - name: "url"
    type: "string"
    description: "The URL of the product."

  - name: "external_product_id"
    type: "string"
    description: "If applicable, the external ID associated with the product."

  - name: "name"
    type: "string"
    description: "The name of the product."

  - name: "description"
    type: "string"
    description: "The description of the product."

  - name: "product_specs"
    type: "object"
    description: "Details about the product."
    subattributes: 
      - name: "key"
        type: "string"
        description: "The product spec key."

      - name: "value"
        type: "string"
        description: ""

  - name: "category"
    type: "object"
    description: "Details about the categories the product is in."
    subattributes: 
      - name: "id"
        type: "number"
        description: "The ID of the category the product is in."
        # foreign-key-id: "category-id"

      - name: "name"
        type: "string"
        description: "The name of the category the product is in."

  - name: "images"
    type: "object"
    description: "Details about the images associated with the product."
    subattributes: 
      - name: "original"
        type: "string"
        description: "The original image associated with the product."

      - name: "square"
        type: "string"
        description: "The thumbnail version of the original image associated with the product."

      - name: "facebook"
        type: "string"
        description: "The Facebook image associated with the product."

      - name: "facebook_square"
        type: "string"
        description: "The thumbnail version of the image associated with the product."

      - name: "kind"
        type: "string"
        description: ""
---