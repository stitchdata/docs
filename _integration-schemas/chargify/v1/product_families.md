---
tap: "chargify"
version: "1"
key: "product-family"

name: "product_families"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-chargify/blob/master/tap_chargify/schemas/product_families.json"
description: |
  The `{{ table.name }}` table contains info about product families in your {{ integration.display_name }} instance. Product families house your products, components, and coupons and are used to categorize products, product levels, or service offerings to your subscribers.

replication-method: "Full Table"

api-method:
  name: "Read product families for a site"
  doc-link: "https://reference.chargify.com/v1/product-families/list-product-family-via-site"
  
attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The product family ID."
    foreign-key-id: "product-family-id"

  - name: "accounting_code"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "handle"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""
---