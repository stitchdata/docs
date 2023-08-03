---
tap: "tiktok-ads"
version: "1"
key: "ad-insights-by-country"

name: "ad_insights_by_country"
doc-link: https://ads.tiktok.com/marketing_api/docs?id=1707957217727489
singer-schema: https://github.com/singer-io/tap-tiktok-ads/tree/master/tap_tiktok_ads/schemas/ad_insights_by_country.json
description: ""

replication-method: "Key-based Incremental"

table-key-properties: "advertiser_id, ad_id, adgroup_id, campaign_id, stat_time_day, country_code"
valid-replication-keys: "stat_time_day"

attributes:
  - name: "ad_id"
    type: "integer"
    description: "Ad ID"
    primary-key: true

  - name: "ad_name"
    type: "string"
    description: ""

  - name: "ad_text"
    type: "string"
    description: ""

  - name: "adgroup_id"
    type: "integer"
    description: "Ad group ID. Avaialble at Ad level."
    primary-key: true

  - name: "adgroup_name"
    type: "string"
    description: ""

  - name: "advertiser_id"
    type: "integer"
    description: "Advertiser ID"
    primary-key: true

  - name: "bid"
    type: "string"
    description: ""

  - name: "bid_strategy"
    type: "string"
    description: ""

  - name: "billing_event"
    type: "string"
    description: ""

  - name: "budget"
    type: "string"
    description: ""

  - name: "call_to_action"
    type: "string"
    description: ""

  - name: "campaign_budget"
    type: "string"
    description: ""

  - name: "campaign_dedicate_type"
    type: "string"
    description: ""

  - name: "campaign_id"
    type: "integer"
    description: "Campaign ID. Available at Ad Group and Ad levels."
    primary-key: true

  - name: "campaign_name"
    type: "string"
    description: ""

  - name: "clicks"
    type: "integer"
    description: ""

  - name: "conversion"
    type: "integer"
    description: ""

  - name: "conversion_rate"
    type: "number"
    description: ""

  - name: "conversion_rate_v2"
    type: "string"
    description: ""

  - name: "cost_per_conversion"
    type: "number"
    description: ""

  - name: "cost_per_result"
    type: "number"
    description: ""

  - name: "country_code"
    type: "string"
    description: ""
    primary-key: true

  - name: "cpc"
    type: "number"
    description: ""

  - name: "cpm"
    type: "number"
    description: ""

  - name: "ctr"
    type: "number"
    description: ""

  - name: "dpa_target_audience_type"
    type: "string"
    description: ""

  - name: "gross_impressions"
    type: "string"
    description: ""

  - name: "impressions"
    type: "integer"
    description: ""

  - name: "is_smart_creative"
    type: "boolean"
    description: ""

  - name: "mobile_app_id"
    type: "string"
    description: ""

  - name: "objective_type"
    type: "string"
    description: ""

  - name: "opt_status"
    type: "string"
    description: ""

  - name: "promotion_type"
    type: "string"
    description: ""

  - name: "real_time_conversion"
    type: "integer"
    description: ""

  - name: "real_time_conversion_rate"
    type: "number"
    description: ""

  - name: "real_time_conversion_rate_v2"
    type: "string"
    description: ""

  - name: "real_time_cost_per_conversion"
    type: "number"
    description: ""

  - name: "real_time_cost_per_result"
    type: "number"
    description: ""

  - name: "real_time_result"
    type: "integer"
    description: ""

  - name: "real_time_result_rate"
    type: "number"
    description: ""

  - name: "result"
    type: "integer"
    description: ""

  - name: "result_rate"
    type: "number"
    description: ""

  - name: "rf_campaign_type"
    type: "string"
    description: ""

  - name: "smart_target"
    type: "string"
    description: ""

  - name: "spend"
    type: "number"
    description: ""

  - name: "split_test"
    type: "string"
    description: ""

  - name: "stat_time_day"
    type: "date-time"
    description: ""
    replication-key: true
    primary-key: true

  - name: "tt_app_id"
    type: "string"
    description: ""

  - name: "tt_app_name"
    type: "string"
    description: ""

  - name: "user_action"
    type: "string"
    description: ""
---