---
tap: "chargify"
version: "1"
key: "price-point"

name: "price_points"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-chargify/blob/master/tap_chargify/schemas/price_points.json"
description: |
  The `{{ table.name }}` table contains info about product price points in your {{ integration.display_name }} instance.

replication-method: "Full Table"

api-method:
  name: "Read product price points"
  doc-link: "https://reference.chargify.com/v1/products-price-points/read-product-price-points"
  
attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The price point ID."
    foreign-key-id: "price-point-id"

  - name: "archived_at"
    type: "date-time"
    description: ""

  - name: "component_id"
    type: "integer"
    description: ""
    foreign-key-id: "component-id"

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "default"
    type: "boolean"
    description: ""

  - name: "handle"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "prices"
    type: "array"
    description: ""
    subattributes:
      - name: "component_id"
        type: "integer"
        description: ""
        foreign-key-id: "component-id"

      - name: "ending_quantity"
        type: "integer"
        description: ""

      - name: "id"
        type: "integer"
        description: ""

      - name: "starting_quantity"
        type: "integer"
        description: ""

      - name: "unit_price"
        type: "string"
        description: ""

  - name: "pricing_scheme"
    type: "string"
    description: ""

  - name: "updated_at"
    type: "date-time"
    description: ""
---