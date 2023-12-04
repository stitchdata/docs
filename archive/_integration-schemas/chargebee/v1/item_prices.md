---
tap: "chargebee"
version: "1"
key: "item-price"

name: "item_prices"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-chargebee/blob/master/tap_chargebee/schemas/item_model/item_prices.json"
description: |
  The `{{ table.name }}` table contains info about item prices.

  {{ integration.table-type | flatify }}

replication-method: "Key-based Incremental"

api-method:
  name: "List item prices"
  doc-link: "https://apidocs.chargebee.com/docs/api/item_prices?prod_cat_ver=2#list_item_prices"

product-catalog-version: "v2"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The item price ID."
    foreign-key-id: "item-price-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the item price was last updated."

  - name: "accounting_detail"
    type: "object"
    description: ""
    subattributes:
      - name: "accounting_category1"
        type: "string"
        description: ""

      - name: "accounting_category2"
        type: "string"
        description: ""

      - name: "accounting_code"
        type: "string"
        description: ""

      - name: "sku"
        type: "string"
        description: ""

  - name: "billing_cycles"
    type: "integer"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "currency_code"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "external_name"
    type: "string"
    description: ""

  - name: "free_quantity"
    type: "integer"
    description: ""

  - name: "invoice_notes"
    type: "string"
    description: ""

  - name: "is_taxable"
    type: "boolean"
    description: ""

  - name: "item_family_id"
    type: "string"
    description: ""
    foreign-key-id: "item-family-id"

  - name: "item_id"
    type: "string"
    description: ""
    foreign-key-id: "item-id"

  - name: "item_type"
    type: "string"
    description: ""

  - name: "metadata"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "object"
    type: "string"
    description: ""

  - name: "period"
    type: "integer"
    description: ""

  - name: "period_unit"
    type: "string"
    description: ""

  - name: "price"
    type: "integer"
    description: ""

  - name: "pricing_model"
    type: "string"
    description: ""

  - name: "resource_version"
    type: "integer"
    description: ""

  - name: "shipping_period"
    type: "integer"
    description: ""

  - name: "shipping_period_unit"
    type: "string"
    description: ""

  - name: "show_description_in_invoices"
    type: "boolean"
    description: ""

  - name: "show_description_in_quotes"
    type: "boolean"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "tax_detail"
    type: "object"
    description: ""
    subattributes:
      - name: "avalara_sale_type"
        type: "string"
        description: ""

      - name: "avalara_service_type"
        type: "integer"
        description: ""

      - name: "avalara_tax_code"
        type: "string"
        description: ""

      - name: "avalara_transaction_type"
        type: "integer"
        description: ""

      - name: "tax_profile_id"
        type: "string"
        description: ""

      - name: "taxjar_product_code"
        type: "string"
        description: ""

  - name: "tiers"
    type: "array"
    description: ""
    subattributes:
      - name: "ending_unit"
        type: "integer"
        description: ""

      - name: "price"
        type: "integer"
        description: ""

      - name: "starting_unit"
        type: "integer"
        description: ""

  - name: "trial_period"
    type: "integer"
    description: ""

  - name: "trial_period_unit"
    type: "string"
    description: ""
---