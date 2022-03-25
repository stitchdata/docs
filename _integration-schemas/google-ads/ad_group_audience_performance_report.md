---
tap: "google-ads"
version: "0"

name: "ad_group_audience_performance_report"
description: |
  The `{{ table.name }}` table contains all statistics aggregated at the ad group level.

  [This is a **Report** table](#replication). See the **Replication** section for information on how data is replicated and loaded for this table.

replication-method: "Key-based Incremental"
loading-behavior: "Append-Only"

attribution-window: true

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: "{{ system-column.record-hash-google-ads }}"

  - name: "date"
    type: "date-time"
    replication-key: true
    description: "The day the record pertains to."

  - name: "customer_id"
    type: "integer"
    description: "The ID of the Ads account that the record belongs to."
    foreign-key-id: "customer_id"

  - name: "ad_group_id"
    type: "integer"
    description: "The ID of the ad group that the record belongs to."
    foreign-key-id: "ad_group_id"
    
  - name: "active_view_cpm"
    type: "singer.decimal"
    description: ""
  - name: "active_view_ctr"
    type: "singer.decimal"
    description: ""
  - name: "active_view_impressions"
    type: "integer"
    description: ""
  - name: "active_view_measurability"
    type: "singer.decimal"
    description: ""
  - name: "active_view_measurable_cost_micros"
    type: "integer"
    description: ""
  - name: "active_view_measurable_impressions"
    type: "integer"
    description: ""
  - name: "active_view_viewability"
    type: "singer.decimal"
    description: ""
  - name: "ad_group_base_ad_group"
    type: "object, string"
    description: ""
  - name: "ad_group_campaign"
    type: "object, string"
    description: ""
  - name: "ad_group_criterion_bid_modifier"
    type: "singer.decimal"
    description: ""
  - name: "ad_group_criterion_criterion_id"
    type: "integer"
    description: ""
  - name: "ad_group_criterion_effective_cpc_bid_micros"
    type: "integer"
    description: ""
  - name: "ad_group_criterion_effective_cpc_bid_source"
    type: "string"
    description: ""
  - name: "ad_group_criterion_effective_cpm_bid_micros"
    type: "integer"
    description: ""
  - name: "ad_group_criterion_effective_cpm_bid_source"
    type: "string"
    description: ""
  - name: "ad_group_criterion_final_mobile_urls"
    type: "string"
    description: ""
  - name: "ad_group_criterion_final_urls"
    type: "string"
    description: ""
  - name: "ad_group_criterion_status"
    type: "string"
    description: ""
  - name: "ad_group_name"
    type: "string"
    description: ""
  - name: "ad_group_status"
    type: "string"
    description: ""
  - name: "ad_group_targeting_setting"
    type: "object"
    description: ""
    subattributes:
      - name: "target_restrictions"
        type: "object, string"
        description: ""
        subattributes: *id001
  - name: "ad_group_tracking_url_template"
    type: "string"
    description: ""
  - name: "ad_group_url_custom_parameters"
    type: "object, string"
    description: ""
  - name: "ad_network_type"
    type: "string"
    description: ""
  - name: "all_conversions"
    type: "singer.decimal"
    description: ""
  - name: "all_conversions_from_interactions_rate"
    type: "singer.decimal"
    description: ""
  - name: "all_conversions_value"
    type: "singer.decimal"
    description: ""
  - name: "average_cost"
    type: "singer.decimal"
    description: ""
  - name: "average_cpc"
    type: "singer.decimal"
    description: ""
  - name: "average_cpe"
    type: "singer.decimal"
    description: ""
  - name: "average_cpm"
    type: "singer.decimal"
    description: ""
  - name: "average_cpv"
    type: "singer.decimal"
    description: ""
  - name: "bidding_strategy_name"
    type: "string"
    description: ""
  - name: "campaign_base_campaign"
    type: "object, string"
    description: ""
  - name: "campaign_bidding_strategy"
    type: "object, string"
    description: ""
  - name: "campaign_bidding_strategy_type"
    type: "string"
    description: ""
  - name: "campaign_name"
    type: "string"
    description: ""
  - name: "campaign_status"
    type: "string"
    description: ""
  - name: "click_type"
    type: "string"
    description: ""
  - name: "clicks"
    type: "integer"
    description: ""
  - name: "conversion_action"
    type: "object, string"
    description: ""
  - name: "conversion_action_category"
    type: "string"
    description: ""
  - name: "conversion_action_name"
    type: "string"
    description: ""
  - name: "conversions"
    type: "singer.decimal"
    description: ""
  - name: "conversions_from_interactions_rate"
    type: "singer.decimal"
    description: ""
  - name: "conversions_value"
    type: "singer.decimal"
    description: ""
  - name: "cost_micros"
    type: "integer"
    description: ""
  - name: "cost_per_all_conversions"
    type: "singer.decimal"
    description: ""
  - name: "cost_per_conversion"
    type: "singer.decimal"
    description: ""
  - name: "cross_device_conversions"
    type: "singer.decimal"
    description: ""
  - name: "ctr"
    type: "singer.decimal"
    description: ""
  - name: "customer_currency_code"
    type: "string"
    description: ""
  - name: "customer_descriptive_name"
    type: "string"
    description: ""
  - name: "customer_time_zone"
    type: "string"
    description: ""
  - name: "date"
    type: "date-time"
    description: ""
  - name: "day_of_week"
    type: "string"
    description: ""
  - name: "device"
    type: "string"
    description: ""
  - name: "engagement_rate"
    type: "singer.decimal"
    description: ""
  - name: "engagements"
    type: "integer"
    description: ""
  - name: "external_conversion_source"
    type: "string"
    description: ""
  - name: "gmail_forwards"
    type: "integer"
    description: ""
  - name: "gmail_saves"
    type: "integer"
    description: ""
  - name: "gmail_secondary_clicks"
    type: "integer"
    description: ""
  - name: "impressions"
    type: "integer"
    description: ""
  - name: "interaction_event_types"
    type: "string"
    description: ""
  - name: "interaction_rate"
    type: "singer.decimal"
    description: ""
  - name: "interactions"
    type: "integer"
    description: ""
  - name: "month"
    type: "date-time"
    description: ""
  - name: "month_of_year"
    type: "string"
    description: ""
  - name: "quarter"
    type: "date-time"
    description: ""
  - name: "slot"
    type: "string"
    description: ""
  - name: "value_per_all_conversions"
    type: "singer.decimal"
    description: ""
  - name: "value_per_conversion"
    type: "singer.decimal"
    description: ""
  - name: "video_quartile_p100_rate"
    type: "singer.decimal"
    description: ""
  - name: "video_quartile_p25_rate"
    type: "singer.decimal"
    description: ""
  - name: "video_quartile_p50_rate"
    type: "singer.decimal"
    description: ""
  - name: "video_quartile_p75_rate"
    type: "singer.decimal"
    description: ""
  - name: "video_view_rate"
    type: "singer.decimal"
    description: ""
  - name: "video_views"
    type: "integer"
    description: ""
  - name: "view_through_conversions"
    type: "integer"
    description: ""
  - name: "week"
    type: "date-time"
    description: ""
  - name: "year"
    type: "integer"
    description: ""
---