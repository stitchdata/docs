---
tap: "chargify"
version: "1"
key: "component"

name: "components"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-chargify/blob/master/tap_chargify/schemas/components.json"
description: |
  The `{{ table.name }}` table contains info about components associated with a product family in {{ integration.display_name }}.

replication-method: "Full Table"

api-method:
  name: "Read components for a product family"
  doc-link: "https://reference.chargify.com/v1/components/list-components-for-a-product-family"
  
attributes:
  - name: "id"
    type: "number"
    primary-key: true
    description: "The component ID."
    foreign-key-id: "component-id"

  - name: "archived"
    type: "boolean"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "default_price_point_id"
    type: "number"
    description: ""
    foreign-key-id: "price-point-id"

  - name: "description"
    type: "string"
    description: ""

  - name: "downgrade_credit"
    type: "string"
    description: ""

  - name: "handle"
    type: "string"
    description: ""

  - name: "kind"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "price_per_unit_in_cents"
    type: "string"
    description: ""

  - name: "price_point_count"
    type: "number"
    description: ""

  - name: "price_points_url"
    type: "string"
    description: ""

  - name: "pricing_scheme"
    type: "string"
    description: ""

  - name: "product_family_id"
    type: "number"
    description: ""
    foreign-key-id: "product-family-id"

  - name: "recurring"
    type: "boolean"
    description: ""

  - name: "tax_code"
    type: "string"
    description: ""

  - name: "taxable"
    type: "boolean"
    description: ""

  - name: "unit_name"
    type: "string"
    description: ""

  - name: "unit_price"
    type: "number"
    description: ""

  - name: "upgrade_charge"
    type: "string"
    description: ""
---