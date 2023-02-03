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
    type: "integer"
    description: "Advertiser ID"
    primary-key: true

  - name: "bid_type"
    type: "string"
    description: "Bidding strategy on the campaign level. Return only when Campaign Budget Optimization is enabled."

  - name: "budget"
    type: "number"
    description: "Campaign budget"

  - name: "budget_mode"
    type: "string"
    description: "Budget mode. See [Enumerations-Budget Mode](https://ads.tiktok.com/marketing_api/docs?id=1737174886619138)."

  - name: "budget_optimize_switch"
    type: "number"
    description: "Whether Campaign Budget Optimization is enabled. Return only when Campaign Budget Optimization is enabled. For details about Campaign Budget Optimization (CBO), see [Campaign Budget Optimization](https://ads.tiktok.com/marketing_api/docs?id=1703428725527554)."

  - name: "campaign_id"
    type: "integer"
    description: "Campaign ID"
    primary-key: true

  - name: "campaign_name"
    type: "string"
    description: "Campaign name"

  - name: "campaign_type"
    type: "string"
    description: "Campaign Type, indicates the campaign is a regular campaign or iOS 14 campaign. Enum values: REGULAR_CAMPAIGN and IOS14_CAMPAIGN."

  - name: "create_time"
    type: "string"
    format: "date-time"
    description: "Time at which the campaign was created."

  - name: "is_new_structure"
    type: "boolean"
    description: "Whether the campaign is a new structure (for the same campaign, the structure of campaign, ad groups and ads are the same)"

  - name: "modify_time"
    type: "string"
    format: "date-time"
    description: "Time at which the campaign was Modified."
    replication-key: true
    primary-key: true

  - name: "objective"
    type: "string"
    description: "Campaign type (application or landing page). Enum values: APP(application), LANDING_PAGE(Landing page)"

  - name: "objective_type"
    type: "string"
    description: "Advertising objective. Enum values: APP_PROMOTION, WEB_CONVERSIONS,APP_INSTALL, CONVERSIONS, REACH, TRAFFIC, VIDEO_VIEWS, CATALOG_SALES, ENGAGEMENT, LEAD_GENERATION, SHOP_PURCHASES,RF_REACH, RF_TRAFFIC, RF_VIDEO_VIEW."

  - name: "opt_status"
    type: "string"
    description: "Operation status. Enum values: DISABLE, ENABLE"

  - name: "optimize_goal"
    type: "string"
    description: "Optimization goal. Return only when Campaign Budget Optimization is enabled."

  - name: "split_test_variable"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: "Campaign status (Secondary status). For enum values, see [Enumeration-Campaign Status - Secondary Status](https://ads.tiktok.com/marketing_api/docs?id=1701890985340929). Note: This field is not returned in the sandbox environment because the campaign is not actually delivered."
---