---
tap: "impact"
version: "1"
key: "ad"

name: "ads"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/ads.json"
description: |
  The `{{ table.name }}` table contains info about ads.

replication-method: "Full Table"

api-method:
  name: "List ads"
  doc-link: "https://developer.impact.com/default#operations-Ads-ListAds"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "ad-id"

  - name: "ad_code_template"
    type: "string"
    description: ""

  - name: "ad_type"
    type: "string"
    description: ""

  - name: "allow_deep_linking"
    type: "boolean"
    description: ""

  - name: "banner_alternative_tag"
    type: "string"
    description: ""

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
    type: "number"
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

  - name: "campaign_name"
    type: "string"
    description: ""

  - name: "coupon_allow_custom_promo_code"
    type: "boolean"
    description: ""

  - name: "coupon_link_name"
    type: "string"
    description: ""

  - name: "custom_ad_serving_url"
    type: "string"
    description: ""

  - name: "customisation_charge"
    type: "number"
    description: ""

  - name: "deal_categories"
    type: "string"
    description: ""

  - name: "deal_default_promo_code"
    type: "string"
    description: ""

  - name: "deal_description"
    type: "string"
    description: ""

  - name: "deal_end_date"
    type: "date-time"
    description: ""

  - name: "deal_id"
    type: "string"
    description: ""
    foreign-key-id: "deal-id"

  - name: "deal_name"
    type: "string"
    description: ""

  - name: "deal_products"
    type: "array"
    description: ""
    subattributes:
      - name: "product_after_price_amount"
        type: "number"
        description: ""

      - name: "product_after_price_currency"
        type: "string"
        description: ""

      - name: "product_before_price_amount"
        type: "number"
        description: ""

      - name: "product_before_price_currency"
        type: "string"
        description: ""

      - name: "product_image_url"
        type: "string"
        description: ""

      - name: "product_name"
        type: "string"
        description: ""

  - name: "deal_restricted_media_partner_groups"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "deal_restricted_media_partners"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "deal_scope"
    type: "string"
    description: ""

  - name: "deal_start_date"
    type: "date-time"
    description: ""

  - name: "deal_state"
    type: "string"
    description: ""

  - name: "deal_type"
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
    type: "number"
    description: ""

  - name: "discount_percent"
    type: "number"
    description: ""

  - name: "discount_percent_range_end"
    type: "number"
    description: ""

  - name: "discount_percent_range_start"
    type: "number"
    description: ""

  - name: "discount_type"
    type: "string"
    description: ""

  - name: "get_html_code_type"
    type: "string"
    description: ""

  - name: "gift"
    type: "string"
    description: ""

  - name: "iab_ad_unit"
    type: "string"
    description: ""

  - name: "labels"
    type: "string"
    description: ""

  - name: "landing_page"
    type: "string"
    description: ""

  - name: "language"
    type: "string"
    description: ""

  - name: "limited_time_end_date"
    type: "date-time"
    description: ""

  - name: "limited_time_start_date"
    type: "date-time"
    description: ""

  - name: "link_text"
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

  - name: "mobile_ready"
    type: "boolean"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "phone_tracking"
    type: "boolean"
    description: ""

  - name: "promo_code_tracking"
    type: "boolean"
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

  - name: "season"
    type: "string"
    description: ""

  - name: "synch_ads_promo_codes"
    type: "string"
    description: ""

  - name: "third_party_servable_ad_creative_height"
    type: "string"
    description: ""

  - name: "third_party_servable_ad_creative_width"
    type: "string"
    description: ""

  - name: "top_seller"
    type: "boolean"
    description: ""

  - name: "uri"
    type: "string"
    description: ""
---