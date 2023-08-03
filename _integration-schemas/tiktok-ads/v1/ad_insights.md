---
tap: "tiktok-ads"
version: "1"
key: "ad-insights"

name: "ad_insights"
doc-link: https://ads.tiktok.com/marketing_api/docs?id=1707957200780290
singer-schema: https://github.com/singer-io/tap-tiktok-ads/tree/master/tap_tiktok_ads/schemas/ad_insights.json
description: ""

replication-method: "Key-based Incremental"

table-key-properties: "advertiser_id, ad_id, adgroup_id, campaign_id, stat_time_day"
valid-replication-keys: "stat_time_day"

attributes:
  - name: "ad_id"
    type: "string"
    description: "Ad ID"
    primary-key: true

  - name: "ad_name"
    type: "string"
    description: ""

  - name: "ad_text"
    type: "string"
    description: ""

  - name: "adgroup_id"
    type: "string"
    description: "Ad group ID. Supported in Ad level."
    primary-key: true

  - name: "adgroup_name"
    type: "string"
    description: ""

  - name: "advertiser_id"
    type: "string"
    description: "Advertiser ID"
    primary-key: true

  - name: "app_promotion_type"
    type: "string"
    description: ""

  - name: "average_video_play"
    type: "number"
    description: ""

  - name: "average_video_play_per_user"
    type: "number"
    description: ""

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
    type: "string"
    description: "Campaign ID. Supported in Ad Group and Ad level."
    primary-key: true

  - name: "campaign_name"
    type: "string"
    description: ""

  - name: "clicks"
    type: "integer"
    description: ""

  - name: "clicks_on_music_disc"
    type: "integer"
    description: ""

  - name: "comments"
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

  - name: "cost_per_1000_reached"
    type: "string"
    description: ""

  - name: "cost_per_100_reached"
    type: "number"
    description: ""

  - name: "cost_per_conversion"
    type: "number"
    description: ""

  - name: "cost_per_result"
    type: "number"
    description: ""

  - name: "cost_per_secondary_goal_result"
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

  - name: "dpa_target_audience_type"
    type: "string"
    description: ""

  - name: "follows"
    type: "integer"
    description: ""

  - name: "frequency"
    type: "number"
    description: ""

  - name: "gross_impressions"
    type: "string"
    description: ""

  - name: "image_mode"
    type: "string"
    description: ""

  - name: "impressions"
    type: "integer"
    description: ""

  - name: "is_smart_creative"
    type: "boolean"
    description: ""

  - name: "likes"
    type: "integer"
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

  - name: "placement_type"
    type: "string"
    description: ""

  - name: "profile_visits"
    type: "integer"
    description: ""

  - name: "profile_visits_rate"
    type: "number"
    description: ""

  - name: "promotion_type"
    type: "string"
    description: ""

  - name: "reach"
    type: "integer"
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

  - name: "secondary_goal_result"
    type: "integer"
    description: ""

  - name: "secondary_goal_result_rate"
    type: "number"
    description: ""

  - name: "shares"
    type: "integer"
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
    primary-key: true
    replication-key: true

  - name: "tt_app_id"
    type: "string"
    description: ""

  - name: "tt_app_name"
    type: "string"
    description: ""

  - name: "video_play_actions"
    type: "integer"
    description: ""

  - name: "video_views_p100"
    type: "integer"
    description: ""

  - name: "video_views_p25"
    type: "integer"
    description: ""

  - name: "video_views_p50"
    type: "integer"
    description: ""

  - name: "video_views_p75"
    type: "integer"
    description: ""

  - name: "video_watched_2s"
    type: "integer"
    description: ""

  - name: "video_watched_6s"
    type: "integer"
    description: ""
---