---
tap: "google-ads"
version: "1"

name: "campaigns"
doc-link: https://developers.google.com/google-ads/api/reference/rpc/v12/CampaignService
singer-schema: https://github.com/singer-io/tap-google-ads/blob/main/tap_google_ads/schemas/campaigns.json
description: |
  The `{{ table.name }}` table contains detailed info about your Google Ads campaigns.

  [This is a **Core Object** table](#replication).

replication-method: "Full Table"
attribution-window: true

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the campaign."
    foreign-key-id: "campaign-id"

  - name: "accessible_bidding_strategy"
    type: "object, string"
    description: ""
  - name: "accessible_bidding_strategy_id"
    type: "integer"
    description: ""
  - name: "ad_serving_optimization_status"
    type: "string"
    description: ""
  - name: "advertising_channel_sub_type"
    type: "string"
    description: ""
  - name: "advertising_channel_type"
    type: "string"
    description: ""
  - name: "app_campaign_setting"
    type: "object"
    description: ""
    subattributes:
      - name: "app_id"
        type: "string"
        description: ""
      - name: "app_store"
        type: "string"
        description: ""
      - name: "bidding_strategy_goal_type"
        type: "string"
        description: ""
  - name: "audience_setting"
    type: "object"
    description: ""
    subattributes:
      - name: "use_audience_grouped"
        type: "boolean"
        description: ""
  - name: "base_campaign"
    type: "object, string"
    description: ""
  - name: "bidding_strategy"
    type: "object, string"
    description: ""
  - name: "bidding_strategy_id"
    type: "integer"
    description: ""
  - name: "bidding_strategy_type"
    type: "string"
    description: ""
  - name: "campaign_budget"
    type: "object, string"
    description: ""
  - name: "campaign_budget_id"
    type: "integer"
    description: ""
  - name: "commission"
    type: "object"
    description: ""
    subattributes:
      - name: "commission_rate_micros"
        type: "integer"
        description: ""
  - name: "customer_id"
    type: "integer"
    description: ""
  - name: "dynamic_search_ads_setting"
    type: "object"
    description: ""
    subattributes:
      - name: "domain_name"
        type: "string"
        description: ""
      - name: "feeds"
        type: "object, string"
        description: ""
      - name: "language_code"
        type: "string"
        description: ""
      - name: "use_supplied_urls_only"
        type: "boolean"
        description: ""
  - name: "end_date"
    type: "date-time"
    description: ""
  - name: "excluded_parent_asset_field_types"
    type: "string"
    description: ""
  - name: "experiment_type"
    type: "string"
    description: ""
  - name: "final_url_suffix"
    type: "string"
    description: ""
  - name: "frequency_caps"
    type: "object, string"
    description: ""
  - name: "geo_target_type_setting"
    type: "object"
    description: ""
    subattributes:
      - name: "negative_geo_target_type"
        type: "string"
        description: ""
      - name: "positive_geo_target_type"
        type: "string"
        description: ""
  - name: "hotel_setting"
    type: "object"
    description: ""
    subattributes:
      - name: "hotel_center_id"
        type: "integer"
        description: ""
  - name: "labels"
    type: "object, string"
    description: ""
  - name: "local_campaign_setting"
    type: "object"
    description: ""
    subattributes:
      - name: "location_source_type"
        type: "string"
        description: ""
  - name: "manual_cpc"
    type: "object"
    description: ""
    subattributes:
      - name: "enhanced_cpc_enabled"
        type: "boolean"
        description: ""
  - name: "manual_cpm"
    type: "object, string"
    description: ""
  - name: "manual_cpv"
    type: "object, string"
    description: ""
  - name: "maximize_conversion_value"
    type: "object"
    description: ""
    subattributes:
      - name: "target_roas"
        type: "singer.decimal"
        description: ""
  - name: "maximize_conversions"
    type: "object"
    description: ""
    subattributes:
      - name: "target_cpa"
        type: "integer"
        description: ""
  - name: "name"
    type: "string"
    description: ""
  - name: "network_settings"
    type: "object"
    description: ""
    subattributes:
      - name: "target_content_network"
        type: "boolean"
        description: ""
      - name: "target_google_search"
        type: "boolean"
        description: ""
      - name: "target_partner_search_network"
        type: "boolean"
        description: ""
      - name: "target_search_network"
        type: "boolean"
        description: ""
  - name: "optimization_goal_setting"
    type: "object"
    description: ""
    subattributes:
      - name: "optimization_goal_types"
        type: "string"
        description: ""
  - name: "optimization_score"
    type: "singer.decimal"
    description: ""
  - name: "payment_mode"
    type: "string"
    description: ""
  - name: "percent_cpc"
    type: "object"
    description: ""
    subattributes:
      - name: "cpc_bid_ceiling_micros"
        type: "integer"
        description: ""
      - name: "enhanced_cpc_enabled"
        type: "boolean"
        description: ""
  - name: "real_time_bidding_setting"
    type: "object"
    description: ""
    subattributes:
      - name: "opt_in"
        type: "boolean"
        description: ""
  - name: "resource_name"
    type: "object, string"
    description: ""
  - name: "selective_optimization"
    type: "object"
    description: ""
    subattributes:
      - name: "conversion_actions"
        type: "object, string"
        description: ""
  - name: "serving_status"
    type: "string"
    description: ""
  - name: "shopping_setting"
    type: "object"
    description: ""
    subattributes:
      - name: "campaign_priority"
        type: "integer"
        description: ""
      - name: "enable_local"
        type: "boolean"
        description: ""
      - name: "merchant_id"
        type: "integer"
        description: ""
      - name: "sales_country"
        type: "string"
        description: ""
      - name: "use_vehicle_inventory"
        type: "boolean"
        description: ""
  - name: "start_date"
    type: "date-time"
    description: ""
  - name: "status"
    type: "string"
    description: ""
  - name: "target_cpa"
    type: "object"
    description: ""
    subattributes:
      - name: "cpc_bid_ceiling_micros"
        type: "integer"
        description: ""
      - name: "cpc_bid_floor_micros"
        type: "integer"
        description: ""
      - name: "target_cpa_micros"
        type: "integer"
        description: ""
  - name: "target_cpm"
    type: "object, string"
    description: ""
  - name: "target_impression_share"
    type: "object"
    description: ""
    subattributes:
      - name: "cpc_bid_ceiling_micros"
        type: "integer"
        description: ""
      - name: "location"
        type: "string"
        description: ""
      - name: "location_fraction_micros"
        type: "integer"
        description: ""
  - name: "target_roas"
    type: "object"
    description: ""
    subattributes:
      - name: "cpc_bid_ceiling_micros"
        type: "integer"
        description: ""
      - name: "cpc_bid_floor_micros"
        type: "integer"
        description: ""
      - name: "target_roas"
        type: "singer.decimal"
        description: ""
  - name: "target_spend"
    type: "object"
    description: ""
    subattributes:
      - name: "cpc_bid_ceiling_micros"
        type: "integer"
        description: ""
      - name: "target_spend_micros"
        type: "integer"
        description: ""
  - name: "targeting_setting"
    type: "object"
    description: ""
    subattributes:
      - name: "target_restrictions"
        type: "object, string"
        description: ""
  - name: "tracking_setting"
    type: "object"
    description: ""
    subattributes:
      - name: "tracking_url"
        type: "string"
        description: ""
  - name: "tracking_url_template"
    type: "string"
    description: ""
  - name: "url_custom_parameters"
    type: "object, string"
    description: ""
  - name: "url_expansion_opt_out"
    type: "boolean"
    description: ""
  - name: "vanity_pharma"
    type: "object"
    description: ""
    subattributes:
      - name: "vanity_pharma_display_url_mode"
        type: "string"
        description: ""
      - name: "vanity_pharma_text"
        type: "string"
        description: ""
  - name: "video_brand_safety_suitability"
    type: "string"
    description: ""
---