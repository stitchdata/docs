---
tap: "platformpurple"
version: "1.0"

name: "products"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-platformpurple/blob/master/tap_platformpurple/schemas/products.json"
description: ""

replication-method: ""

attributes:
  - name: "productID"
    type: "integer"
    primary-key: true
    description: "THe product ID."
    foreign-key-id: "product-id"

  - name: "byLine"
    type: "string"
    description: "The product by line."

  - name: "clientProductSKU"
    type: "string"
    description: ""

  - name: "duration"
    type: "integer"
    description: ""

  - name: "productName"
    type: "string"
    description: "The product name."

  - name: "productPrice"
    type: "string"
    description: "The product price."

  - name: "productSKU"
    type: "string"
    description: "The product SKU."

  - name: "productType"
    type: "string"
    description: "The product type."

  - name: "searchString"
    type: "string"
    description: ""
---