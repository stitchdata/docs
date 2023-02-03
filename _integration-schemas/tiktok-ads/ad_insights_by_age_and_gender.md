---
tap: "tiktok-ads"
version: "1"
key: "ad-insights-by-age-and-gender"

name: "ad_insights_by_age_and_gender"
doc-link: https://ads.tiktok.com/marketing_api/docs?id=1707957217727489
singer-schema: https://github.com/singer-io/tap-tiktok-ads/tree/master/tap_tiktok_ads/schemas/ad_insights_by_age_and_gender.json
description: ""

replication-method: "Key-based Incremental"

table-key-properties: "advertiser_id, ad_id, adgroup_id, campaign_id, stat_time_day, age, gender"
valid-replication-keys: "stat_time_day"

attributes:
  - name: "ad_id"
    type: "integer"
    description: "Ad ID"
    primary-key: true

  - name: "ad_name"
    type: "string"
    description: "Ad name. Available at Ad level."

  - name: "ad_text"
    type: "string"
    description: "Ad title. Available in Ad level."

  - name: "adgroup_id"
    type: "integer"
    description: "Ad group ID. Avaialble at Ad level."
    primary-key: true

  - name: "adgroup_name"
    type: "string"
    description: "Ad group name. Available at Ad Group and Ad levels."

  - name: "advertiser_id"
    type: "integer"
    description: "Advertiser ID"
    primary-key: true

  - name: "age"
    type: "string"
    description: ""
    primary-key: true

  - name: "campaign_id"
    type: "integer"
    description: "Campaign ID. Available at Ad Group and Ad levels."
    primary-key: true

  - name: "campaign_name"
    type: "string"
    description: "Campaign name. Available at Campaign, Ad Group and Ad levels."

  - name: "clicks"
    type: "integer"
    description: "The number of clicks on your ads."

  - name: "conversion"
    type: "integer"
    description: "The number of times your ad achieved an outcome, based on the secondary goal you selected. As one campaign may have a number of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)"

  - name: "conversion_rate"
    type: "number"
    description: "The percentage of results you received out of all the clicks of your ads.(The total count is calculated based on the time each ad impression occurred.)"

  - name: "cost_per_conversion"
    type: "number"
    description: "The average amount of money you've spent on a conversion.(The total count is calculated based on the time each ad impression occurred.)"

  - name: "cost_per_result"
    type: "number"
    description: "The average cost for each result from your ads. As one campaign may have a number of different optimization goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view the cost per result. (The total count is calculated based on the time each ad impression occurred.)"

  - name: "cpc"
    type: "number"
    description: "The average amount of money you've spent on a click."

  - name: "cpm"
    type: "number"
    description: "The average amount of money you've spent per 1,000 impressions."

  - name: "ctr"
    type: "number"
    description: "The percentage of times people saw your ad and performed a click."

  - name: "dpa_target_audience_type"
    type: "string"
    description: "The Audience that DPA products target. Supported at Adgroup or Ad levels in both synchronous and asynchronous reports."

  - name: "gender"
    type: "string"
    description: ""
    primary-key: true

  - name: "impressions"
    type: "integer"
    description: "The number of times your ads were on screen."

  - name: "mobile_app_id"
    type: "string"
    description: "Mobile App ID. Examples are, App Store: https://apps.apple.com/us/app/angry-birds/id343200656; Google Play：https://play.google.com/store/apps/details?id=com.rovio.angrybirds. Available at Ad Group and Ad levels. Returned if the promotion type of one Ad Group is App."

  - name: "promotion_type"
    type: "string"
    description: "It can be app, website, or others. Supported at Adgroup and Ad levels in both synchronous and asynchronous reports."

  - name: "real_time_conversion"
    type: "integer"
    description: ""

  - name: "real_time_conversion_rate"
    type: "number"
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

  - name: "spend"
    type: "number"
    description: ""

  - name: "stat_time_day"
    type: "string"
    format: "date-time"
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