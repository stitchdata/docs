---
tap: "impact"
version: "1"
key: "deal"

name: "deals"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/deals.json"
description: |
  The `{{ table.name }}` table contains info about the deals in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get deals"
  doc-link: "https://developer.impact.com/default#operations-Deals-GetDeals"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "deal-id"

  - name: "bogo_buy_image_url"
    type: "string"
    description: ""

  - name: "bogo_buy_name"
    type: "string"
    description: ""

  - name: "bogo_buy_quantity"
    type: "string"
    description: ""

  - name: "bogo_buy_scope"
    type: "string"
    description: ""

  - name: "bogo_get_discount_amount"
    type: "number"
    description: ""

  - name: "bogo_get_discount_currency"
    type: "string"
    description: ""

  - name: "bogo_get_discount_percent"
    type: "integer"
    description: ""

  - name: "bogo_get_discount_type"
    type: "string"
    description: ""

  - name: "bogo_get_image_url"
    type: "string"
    description: ""

  - name: "bogo_get_name"
    type: "string"
    description: ""

  - name: "bogo_get_quantity"
    type: "string"
    description: ""

  - name: "bogo_get_scope"
    type: "string"
    description: ""

  - name: "campaign_id"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-id"

  - name: "categories"
    type: "string"
    description: ""

  - name: "default_promo_code"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "discount_amount"
    type: "number"
    description: ""

  - name: "discount_currency"
    type: "string"
    description: ""

  - name: "discount_maximum_percent"
    type: "integer"
    description: ""

  - name: "discount_percent"
    type: "integer"
    description: ""

  - name: "discount_percent_range_end"
    type: "integer"
    description: ""

  - name: "discount_percent_range_start"
    type: "integer"
    description: ""

  - name: "discount_type"
    type: "string"
    description: ""

  - name: "end_date"
    type: "date-time"
    description: ""

  - name: "gift"
    type: "string"
    description: ""

  - name: "maximum_savings_amount"
    type: "number"
    description: ""

  - name: "maximum_savings_currency"
    type: "string"
    description: ""

  - name: "minimum_purchase_amount"
    type: "number"
    description: ""

  - name: "minimum_purchase_amount_currency"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "products"
    type: "array"
    description: ""
    subattributes:
      - name: "product_after_price_amount"
        type: "number"
        description: ""

      - name: "product_after_price_currency"
        type: "number"
        description: ""

      - name: "product_before_price_amount"
        type: "number"
        description: ""

      - name: "product_before_price_currency"
        type: "number"
        description: ""

      - name: "product_image_url"
        type: "string"
        description: ""

      - name: "product_name"
        type: "string"
        description: ""

  - name: "purchase_limit_quantity"
    type: "string"
    description: ""

  - name: "rebate_amount"
    type: "number"
    description: ""

  - name: "rebate_currency"
    type: "string"
    description: ""

  - name: "restricted_media_partner_groups"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "restricted_media_partners"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "scope"
    type: "string"
    description: ""

  - name: "start_date"
    type: "date-time"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "synch_ads_promo_codes"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "uri"
    type: "string"
    description: ""
---