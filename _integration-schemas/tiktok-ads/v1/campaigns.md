---
tap: "tiktok-ads"
version: "1"
key: "campaigns"

name: "campaigns"
doc-link: https://ads.tiktok.com/marketing_api/docs?id=1708582970809346
singer-schema: https://github.com/singer-io/tap-tiktok-ads/tree/master/tap_tiktok_ads/schemas/campaigns.json
description: ""

replication-method: "Key-based Incremental"

table-key-properties: "advertiser_id, campaign_id, modify_time"
valid-replication-keys: "modify_time"

attributes:
  - name: "advertiser_id"
    type: "string"
    description: "Advertiser ID"
    primary-key: true

  - name: "app_id"
    type: "string"
    description: ""

  - name: "app_promotion_type"
    type: "string"
    description: ""

  - name: "bid_type"
    type: "string"
    description: ""

  - name: "budget"
    type: "number"
    description: ""

  - name: "budget_mode"
    type: "string"
    description: ""

  - name: "budget_optimize_on"
    type: "boolean"
    description: ""

  - name: "campaign_app_profile_page_state"
    type: "string"
    description: ""

  - name: "campaign_id"
    type: "string"
    description: "Campaign ID"
    primary-key: true

  - name: "campaign_name"
    type: "string"
    description: ""

  - name: "campaign_product_source"
    type: "string"
    description: ""

  - name: "campaign_type"
    type: "string"
    description: ""

  - name: "create_time"
    type: "string"
    format: "date-time"
    description: ""

  - name: "deep_bid_type"
    type: "string"
    description: ""

  - name: "is_new_structure"
    type: "boolean"
    description: ""

  - name: "is_smart_performance_campaign"
    type: "boolean"
    description: ""

  - name: "modify_time"
    type: "date-time"
    description: "Time at which the campaign was Modified."
    replication-key: true
    primary-key: true

  - name: "objective"
    type: "string"
    description: ""

  - name: "objective_type"
    type: "string"
    description: ""

  - name: "operation_status"
    type: "string"
    description: ""

  - name: "optimization_goal"
    type: "string"
    description: ""

  - name: "rf_campaign_type"
    type: "string"
    description: ""

  - name: "roas_bid"
    type: "number"
    description: ""

  - name: "secondary_status"
    type: "string"
    description: ""

  - name: "special_industries"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""
---