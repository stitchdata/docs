---
tap: "impact"
version: "1"
key: "conversion-path"

name: "conversion_paths"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/conversion_paths.json"
description: |
  The `{{ table.name }}` table contains info about a campaign's conversions.

  **Note**: Your **Model ID** must be provided [in the integration's settings](#add-stitch-data-source) to replicate data for this table.

replication-method: "Full Table"

api-method:
  name: "Get conversion paths"
  doc-link: "https://developer.impact.com/default/documentation/Rest-Adv-v8#operations-Conversion_Paths-GetConversionPaths"

attributes:
  - name: "campaign_id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "campaign-id"

  - name: "customer_id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "customer-id"

  - name: "model_id"
    type: "integer"
    primary-key: true
    description: ""

  - name: "campaign_name"
    type: "string"
    description: ""

  - name: "channel_count"
    type: "integer"
    description: ""

  - name: "cost"
    type: "number"
    description: ""

  - name: "events"
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "sub_type"
        type: "string"
        description: ""

      - name: "event_date"
        type: "date-time"
        description: ""

      - name: "step"
        type: "integer"
        description: ""

      - name: "position_type"
        type: "string"
        description: ""

      - name: "site_version"
        type: "string"
        description: ""

      - name: "site_category"
        type: "string"
        description: ""

      - name: "landing_page"
        type: "string"
        description: ""

      - name: "customer_status"
        type: "string"
        description: ""

      - name: "customer_post_code"
        type: "string"
        description: ""

      - name: "customer_area"
        type: "string"
        description: ""

      - name: "customer_city"
        type: "string"
        description: ""

      - name: "customer_region"
        type: "string"
        description: ""

      - name: "customer_country"
        type: "string"
        description: ""

      - name: "device_type"
        type: "string"
        description: ""

      - name: "device_family"
        type: "string"
        description: ""

      - name: "browser"
        type: "string"
        description: ""

      - name: "os"
        type: "string"
        description: ""

      - name: "profile_id"
        type: "string"
        description: ""

      - name: "fingerprint"
        type: "string"
        description: ""

      - name: "platform"
        type: "string"
        description: ""

      - name: "media_id"
        type: "integer"
        description: ""
        foreign-key-id: "media-id"

      - name: "media_name"
        type: "string"
        description: ""

      - name: "channel"
        type: "string"
        description: ""

      - name: "ad_distribution_type"
        type: "string"
        description: ""

      - name: "ad_campaign"
        type: "string"
        description: ""

      - name: "ad_group"
        type: "string"
        description: ""

      - name: "ad_id"
        type: "integer"
        description: ""
        foreign-key-id: "ad-id"

      - name: "ad_name"
        type: "string"
        description: ""

      - name: "deal_name"
        type: "string"
        description: ""

      - name: "deal_type"
        type: "string"
        description: ""

      - name: "deal_scope"
        type: "string"
        description: ""

      - name: "keyword"
        type: "string"
        description: ""

      - name: "match_type"
        type: "string"
        description: ""

      - name: "traffic_type"
        type: "string"
        description: ""

      - name: "ad_site_location"
        type: "string"
        description: ""

      - name: "sub_id_1"
        type: "integer"
        description: ""

      - name: "sub_id_2"
        type: "integer"
        description: ""

      - name: "sub_id_3"
        type: "integer"
        description: ""

      - name: "shared_id"
        type: "string"
        description: ""

      - name: "referring_url"
        type: "string"
        description: ""

      - name: "attributed_credit"
        type: "number"
        description: ""

      - name: "attributed_revenue"
        type: "number"
        description: ""

      - name: "action_id"
        type: "string"
        description: ""
        foreign-key-id: "action-id"

      - name: "action_date"
        type: "date-time"
        description: ""

      - name: "action_tracker_id"
        type: "integer"
        description: ""
        foreign-key-id: "action-tracker-id"

      - name: "action_tracker_name"
        type: "string"
        description: ""

      - name: "app_package_name"
        type: "string"
        description: ""

      - name: "app_name"
        type: "string"
        description: ""

      - name: "app_version"
        type: "string"
        description: ""

      - name: "phone_number"
        type: "string"
        description: ""

      - name: "order_id"
        type: "string"
        description: ""

      - name: "promocode"
        type: "string"
        description: ""

      - name: "amount"
        type: "number"
        description: ""

      - name: "payout"
        type: "number"
        description: ""

      - name: "order_margin"
        type: "number"
        description: ""

      - name: "order_discount"
        type: "number"
        description: ""

      - name: "order_shipping"
        type: "number"
        description: ""

      - name: "order_tax"
        type: "number"
        description: ""

      - name: "order_vat"
        type: "number"
        description: ""

      - name: "order_subtotal"
        type: "number"
        description: ""

      - name: "note"
        type: "string"
        description: ""

      - name: "text_1"
        type: "string"
        description: ""

      - name: "text_2"
        type: "string"
        description: ""

      - name: "text_3"
        type: "string"
        description: ""

      - name: "numeric_1"
        type: "number"
        description: ""

      - name: "numeric_2"
        type: "number"
        description: ""

      - name: "numeric_3"
        type: "number"
        description: ""

      - name: "money_1"
        type: "number"
        description: ""

      - name: "money_2"
        type: "number"
        description: ""

      - name: "money_3"
        type: "number"
        description: ""

      - name: "date_1"
        type: "date"
        description: ""

      - name: "date_2"
        type: "date"
        description: ""

      - name: "date_3"
        type: "date"
        description: ""

  - name: "latency"
    type: "number"
    description: ""

  - name: "media_count"
    type: "integer"
    description: ""

  - name: "model_name"
    type: "string"
    description: ""

  - name: "referral_counts"
    type: "array"
    description: ""
    subattributes:
      - name: "count"
        type: "integer"
        description: ""

      - name: "type"
        type: "string"
        description: ""

  - name: "revenue"
    type: "number"
    description: ""

  - name: "steps"
    type: "integer"
    description: ""

  - name: "uri"
    type: "string"
    description: ""
---