---
tap: "tiktok-ads"
version: "1"
key: ""

name: "campaign_insights_by_province"
doc-link: 
singer-schema: https://github.com/singer-io/tap-tiktok-ads/tree/master/tap_tiktok_ads/schemas/campaign_insights_by_province.json
description: ""

replication-method: "Key-based Incremental"

table-key-properties: "advertiser_id, campaign_id, stat_time_day, province_id"
valid-replication-keys: "stat_time_day"

attributes:
  - name: "advertiser_id"
    type: "string"
    description: "Advertiser ID"
    primary-key: true

  - name: "campaign_budget"
    type: "string"
    description: ""

  - name: "campaign_dedicate_type"
    type: "string"
    description: ""

  - name: "campaign_id"
    type: "string"
    description: "Campaign ID"
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

  - name: "cpc"
    type: "number"
    description: ""

  - name: "cpm"
    type: "number"
    description: ""

  - name: "ctr"
    type: "number"
    description: ""

  - name: "gross_impressions"
    type: "string"
    description: ""

  - name: "impressions"
    type: "integer"
    description: ""

  - name: "objective_type"
    type: "string"
    description: ""

  - name: "province_id"
    type: "string"
    description: "Province ID"
    primary-key: true

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

  - name: "spend"
    type: "number"
    description: ""

  - name: "split_test"
    type: "string"
    description: ""

  - name: "stat_time_day"
    type: "date-time"
    description: ""
    primary-key: true
    replication-key: true
---