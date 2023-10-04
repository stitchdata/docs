---
tap: "tiktok-ads"
version: "1"
key: "adgroups"

name: "adgroups"
doc-link: https://ads.tiktok.com/marketing_api/docs?id=1708503489590273
singer-schema: https://github.com/singer-io/tap-tiktok-ads/tree/master/tap_tiktok_ads/schemas/adgroups.json
description: ""

replication-method: "Key-based Incremental"

table-key-properties: "advertiser_id, campaign_id, adgroup_id, modify_time"
valid-replication-keys: "modify_time"

attributes:
  - name: "actions"
    type: "array"
    description: ""
    subattributes:
    - name: "action_category_ids"
      type: "array"
      description: ""
      subattributes:
      - name: "items"
        type: "string"
        description: ""

    - name: "action_period"
      type: "number"
      description: ""

    - name: "action_scene"
      type: "string"
      description: ""

    - name: "video_user_actions"
      type: "array"
      description: ""
      subattributes:
      - name: "items"
        type: "string"
        description: ""


  - name: "adgroup_app_profile_page_state"
    type: "string"
    description: ""

  - name: "adgroup_id"
    type: "string"
    description: "Ad group ID"
    primary-key: true

  - name: "adgroup_name"
    type: "string"
    description: ""

  - name: "advertiser_id"
    type: "string"
    description: "Advertiser ID"
    primary-key: true

  - name: "age_groups"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "app_download_url"
    type: "string"
    description: ""

  - name: "app_id"
    type: "string"
    description: ""

  - name: "audience"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "integer"
      description: ""

  - name: "audience_type"
    type: "string"
    description: ""

  - name: "bid_price"
    type: "number"
    description: ""

  - name: "bid_type"
    type: "string"
    description: ""

  - name: "billing_event"
    type: "string"
    description: ""

  - name: "brand_safety_partner"
    type: "string"
    description: ""

  - name: "brand_safety_type"
    type: "string"
    description: ""

  - name: "budget"
    type: "number"
    description: ""

  - name: "budget_mode"
    type: "string"
    description: ""

  - name: "campaign_id"
    type: "string"
    description: "Campaign ID"
    primary-key: true

  - name: "carriers_v2"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "integer"
      description: ""

  - name: "catalog_authorized_bc"
    type: "integer"
    description: ""

  - name: "catalog_id"
    type: "string"
    description: ""

  - name: "conversion_bid_price"
    type: "number"
    description: ""

  - name: "conversion_window"
    type: "string"
    description: ""

  - name: "cpv_video_duration"
    type: "string"
    description: ""

  - name: "create_time"
    type: "string"
    format: "date-time"
    description: ""

  - name: "creative_material_mode"
    type: "string"
    description: ""

  - name: "dayparting"
    type: "string"
    description: ""

  - name: "deep_bid_type"
    type: "string"
    description: ""

  - name: "deep_cpa_bid"
    type: "number"
    description: ""

  - name: "delivery_mode"
    type: "string"
    description: ""

  - name: "device_models"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "integer"
      description: ""

  - name: "device_price_ranges"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "number"
      description: ""

  - name: "excluded_audience"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "integer"
      description: ""

  - name: "excluded_custom_actions"
    type: "array"
    description: ""
    subattributes:
    - name: "code"
      type: "string"
      description: ""

    - name: "days"
      type: "integer"
      description: ""


  - name: "frequency"
    type: "integer"
    description: ""

  - name: "frequency_schedule"
    type: "integer"
    description: ""

  - name: "gender"
    type: "string"
    description: ""

  - name: "included_custom_actions"
    type: "array"
    description: ""
    subattributes:
    - name: "code"
      type: "string"
      description: ""

    - name: "days"
      type: "integer"
      description: ""


  - name: "interest_category_v2"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "integer"
      description: ""

  - name: "interest_keywords"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "integer"
      description: ""

  - name: "inventory_filter_enabled"
    type: "boolean"
    description: ""

  - name: "ios14_targeting"
    type: "string"
    description: ""

  - name: "ios_quota_type"
    type: "string"
    description: ""

  - name: "is_comment_disable"
    type: "boolean"
    description: ""

  - name: "is_hfss"
    type: "boolean"
    description: ""

  - name: "is_new_structure"
    type: "boolean"
    description: ""

  - name: "languages"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "location"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "integer"
      description: ""

  - name: "min_android_version"
    type: "string"
    description: ""

  - name: "min_ios_version"
    type: "string"
    description: ""

  - name: "modify_time"
    type: "date-time"
    description: "Time at which the ad group was Modified."
    replication-key: true
    primary-key: true

  - name: "network_types"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "next_day_retention"
    type: "number"
    description: ""

  - name: "operating_systems"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "operation_status"
    type: "string"
    description: ""

  - name: "optimization_event"
    type: "string"
    description: ""

  - name: "optimization_goal"
    type: "string"
    description: ""

  - name: "pacing"
    type: "string"
    description: ""

  - name: "package"
    type: "string"
    description: ""

  - name: "pangle_audience_package_exclude"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "integer"
      description: ""

  - name: "pangle_audience_package_include"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "integer"
      description: ""

  - name: "pangle_block_app_list_id"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "integer"
      description: ""

  - name: "pixel_id"
    type: "string"
    description: ""

  - name: "placement_type"
    type: "string"
    description: ""

  - name: "placements"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "product_set_id"
    type: "string"
    description: ""

  - name: "promotion_type"
    type: "string"
    description: ""

  - name: "promotion_website_type"
    type: "string"
    description: ""

  - name: "purchased_impression"
    type: "number"
    description: ""

  - name: "purchased_reach"
    type: "number"
    description: ""

  - name: "rf_estimated_cpr"
    type: "number"
    description: ""

  - name: "rf_estimated_frequency"
    type: "number"
    description: ""

  - name: "rf_purchased_type"
    type: "string"
    description: ""

  - name: "roas_bid"
    type: "number"
    description: ""

  - name: "schedule_end_time"
    type: "string"
    format: "date-time"
    description: ""

  - name: "schedule_start_time"
    type: "string"
    format: "date-time"
    description: ""

  - name: "schedule_type"
    type: "string"
    description: ""

  - name: "secondary_optimization_event"
    type: "string"
    description: ""

  - name: "secondary_status"
    type: "string"
    description: ""

  - name: "share_disabled"
    type: "boolean"
    description: ""

  - name: "shopping_ads_retargeting_type"
    type: "string"
    description: ""

  - name: "skip_learning_phase"
    type: "boolean"
    description: ""

  - name: "statistic_type"
    type: "string"
    description: ""

  - name: "targeting_expansion"
    type: "object"
    description: ""
    subattributes:
    - name: "expansion_types"
      type: "array"
      description: ""
      subattributes:
      - name: "items"
        type: "string"
        description: ""

    - name: "expansion_enabled"
      type: "boolean"
      description: ""


  - name: "video_download"
    type: "string"
    description: ""
---