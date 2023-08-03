---
tap: "tiktok-ads"
version: "1"
key: "ads"

name: "ads"
doc-link: https://ads.tiktok.com/marketing_api/docs?id=1708572923161602
singer-schema: https://github.com/singer-io/tap-tiktok-ads/tree/master/tap_tiktok_ads/schemas/ads.json
description: ""

replication-method: "Key-based Incremental"

table-key-properties: "advertiser_id, campaign_id, adgroup_id, ad_id, modify_time"
valid-replication-keys: "modify_time"

attributes:
  - name: "ad_format"
    type: "string"
    description: ""

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
    description: "Ad group ID"
    primary-key: true

  - name: "adgroup_name"
    type: "string"
    description: ""

  - name: "advertiser_id"
    type: "string"
    description: "Advertiser ID"
    primary-key: true

  - name: "app_name"
    type: "string"
    description: ""

  - name: "brand_safety_vast_url"
    type: "string"
    description: ""

  - name: "call_to_action"
    type: "string"
    description: ""

  - name: "campaign_id"
    type: "string"
    description: "Campaign ID"
    primary-key: true

  - name: "campaign_name"
    type: "string"
    description: ""

  - name: "card_id"
    type: "string"
    description: ""

  - name: "carousel_image_index"
    type: "integer"
    description: ""

  - name: "catalog_id"
    type: "string"
    description: ""

  - name: "click_tracking_url"
    type: "string"
    description: ""

  - name: "create_time"
    type: "string"
    format: "date-time"
    description: ""

  - name: "creative_authorized"
    type: "boolean"
    description: ""

  - name: "deeplink"
    type: "string"
    description: ""

  - name: "deeplink_type"
    type: "string"
    description: ""

  - name: "display_name"
    type: "string"
    description: ""

  - name: "dynamic_destination"
    type: "string"
    description: ""

  - name: "dynamic_format"
    type: "string"
    description: ""

  - name: "fallback_type"
    type: "string"
    description: ""

  - name: "image_ids"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "image_mode"
    type: "string"
    description: ""

  - name: "impression_tracking_url"
    type: "string"
    description: ""

  - name: "is_aco"
    type: "boolean"
    description: ""

  - name: "is_new_structure"
    type: "boolean"
    description: ""

  - name: "item_duet_status"
    type: "string"
    description: ""

  - name: "item_group_ids"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "item_stitch_status"
    type: "string"
    description: ""

  - name: "landing_page_url"
    type: "string"
    description: ""

  - name: "landing_page_urls"
    type: "string"
    description: ""

  - name: "modify_time"
    type: "date-time"
    description: "Time at which the ad was Modified."
    replication-key: true
    primary-key: true

  - name: "music_id"
    type: "string"
    description: ""

  - name: "operation_status"
    type: "string"
    description: ""

  - name: "page_id"
    type: "number"
    description: ""

  - name: "playable_url"
    type: "string"
    description: ""

  - name: "product_set_id"
    type: "string"
    description: ""

  - name: "product_specific_type"
    type: "string"
    description: ""

  - name: "profile_image_url"
    type: "string"
    description: ""

  - name: "promotional_music_disabled"
    type: "boolean"
    description: ""

  - name: "secondary_status"
    type: "string"
    description: ""

  - name: "shopping_ads_fallback_type"
    type: "string"
    description: ""

  - name: "shopping_ads_video_package_id"
    type: "string"
    description: ""

  - name: "shopping_deeplink_type"
    type: "string"
    description: ""

  - name: "showcase_products"
    type: "array"
    description: ""
    subattributes:
    - name: "item_group_id"
      type: "string"
      description: ""

    - name: "store_id"
      type: "string"
      description: ""

    - name: "catalog_id"
      type: "string"
      description: ""


  - name: "sku_ids"
    type: "string"
    description: ""

  - name: "tiktok_item_id"
    type: "string"
    description: ""

  - name: "tracking_app_id"
    type: "string"
    description: ""

  - name: "tracking_offline_event_set_ids"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "utm_params"
    type: "array"
    description: ""
    subattributes:
    - name: "key"
      type: "string"
      description: ""

    - name: "value"
      type: "string"
      description: ""


  - name: "vast_moat_enabled"
    type: "boolean"
    description: ""

  - name: "vertical_video_strategy"
    type: "string"
    description: ""

  - name: "video_id"
    type: "string"
    description: ""

  - name: "viewability_postbid_partner"
    type: "string"
    description: ""

  - name: "viewability_vast_url"
    type: "string"
    description: ""
---