---
tap: "chargify"
version: "1"
key: "product"

name: "products"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-chargify/blob/master/tap_chargify/schemas/products.json"
description: |
  The `{{ table.name }}` table contains info about the prodcts in your {{ integration.display_name }} instance.

replication-method: "Full Table"

api-method:
  name: "List products for a product family"
  doc-link: "https://reference.chargify.com/v1/products/list-products"
  
attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The product ID."
    foreign-key-id: "product-id"

  - name: "accounting_code"
    type: "string"
    description: ""

  - name: "archived_at"
    type: "date-time"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "expiration_interval"
    type: "string"
    description: ""

  - name: "expiration_interval_unit"
    type: "string"
    description: ""

  - name: "handle"
    type: "string"
    description: ""

  - name: "initial_charge_after_trial"
    type: "boolean"
    description: ""

  - name: "initial_charge_in_cents"
    type: "integer"
    description: ""

  - name: "interval"
    type: "integer"
    description: ""

  - name: "interval_unit"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "price_in_cents"
    type: "integer"
    description: ""

  - name: "product_family"
    type: "object"
    description: ""
    subattributes:
      - name: "accounting_code"
        type: "string"
        description: ""

      - name: "description"
        type: "string"
        description: ""

      - name: "handle"
        type: "string"
        description: ""

      - name: "id"
        type: "number"
        description: ""
        foreign-key-id: "product-family-id"

      - name: "name"
        type: "string"
        description: ""

  - name: "public_signup_pages"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "anything"
        description: ""

  - name: "request_credit_card"
    type: "boolean"
    description: ""

  - name: "require_credit_card"
    type: "boolean"
    description: ""

  - name: "return_params"
    type: "string"
    description: ""

  - name: "tax_code"
    type: "string"
    description: ""

  - name: "taxable"
    type: "boolean"
    description: ""

  - name: "trial_interval"
    type: "integer"
    description: ""

  - name: "trial_interval_unit"
    type: "string"
    description: ""

  - name: "trial_price_in_cents"
    type: "integer"
    description: ""

  - name: "update_return_params"
    type: "string"
    description: ""

  - name: "update_return_url"
    type: "string"
    description: ""

  - name: "updated_at"
    type: "date-time"
    description: ""

  - name: "version_number"
    type: "integer"
    description: ""
---