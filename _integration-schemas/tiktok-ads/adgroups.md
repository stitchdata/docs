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
  - name: "action_v2"
    type: array"
    description: "A list of action category objects."
    subattributes:
    - name: "action_categories"
      type: array"
      description: "IDs of the action categories (behaviors) or hashtags that you want to target. This field is valid only when TikTok placement is the only placement selected."
      subattributes:
      - name: "items"
        type: integer"
        description: "ID of the action category"

    - name: "action_period"
      type: integer"
      description: "The time period to include actions from."

    - name: "action_scene"
      type: string"
      description: "Where you can collect information about user actions. Enum: VIDEO_RELATED, CREATOR_RELATED, HASHTAG_RELATED."

    - name: "user_actions"
      type: array"
      description: "Video-related actions."
      subattributes:
      - name: "items"
        type: string"
        description: "Video-related action."


  - name: "adgroup_id"
    type: integer"
    description: "Ad group ID"

  - name: "adgroup_name"
    type: string"
    description: "Ad group Name"
    primary-key: true

  - name: "advertiser_id"
    type: integer"
    description: "Advertiser ID"
    primary-key: true

  - name: "age"
    type: array"
    description: "Age groups you want to target. For enum values, see (Enumeration - Age Group)[https://ads.tiktok.com/marketing_api/docs?id=1701890985340929]."
    subattributes:
    - name: "items"
      type: string"
      description: "Age group you want to target."

  - name: "android_osv"
    type: string"
    description: "Minimum Android version. For enum values, see (Enumeration - Minimum Android Version)[https://ads.tiktok.com/marketing_api/docs?id=1701890985340929]."

  - name: "app_download_url"
    type: string"
    description: "App download link"

  - name: "app_id"
    type: integer"
    description: "The Application ID of the promoted app. You can get app_id by using the /app/list/ endpoint."

  - name: "audience"
    type: array"
    description: "A list of audience IDs"
    subattributes:
    - name: "items"
      type: integer"
      description: "Audience ID"

  - name: "audience_type"
    type: string"
    description: "App retargeting audience type. For enum values, see (Enumeration - App Retargeting Audience Type)[https://ads.tiktok.com/marketing_api/docs?id=1701890985340929]."

  - name: "bid"
    type: number"
    description: "Bid price. The maximum cost per result you are willing to bid (for Bid Cap bidding strategy), or an average cost per result that you want to achieve (for Cost Cap bidding strategy)."

  - name: "bid_type"
    type: string"
    description: "Bidding strategy that determines how the system manages your cost per result, spends your budget, and how it delivers ads.
    See (Enumeration - Bidding Strategy)[https://ads.tiktok.com/marketing_api/docs?id=1701890985340929]."

  - name: "billing_event"
    type: string"
    description: "Bid method. See (Enumeration - Bid method)[https://ads.tiktok.com/marketing_api/docs?id=1701890985340929] for optional values."

  - name: "brand_safety"
    type: string"
    description: "Brand safety type. Enum values:
    1. THIRD_PARTY: Use a third-party brand safety solution. You also need to pass in a value to the brand_safety_partner field.
    2. LIMITED_INVENTORY: Use TikTok's brand safety solution. Currently, the only supported safety level is Limited Inventory, which is a strict brand safety level. It would exclude all identifiable risky content. To get the countries and regions that your ads can be deployed to based on your brand safety settings, use the /tools/regions/ endpoint."

  - name: "brand_safety_partner"
    type: string"
    description: "Brand safety partner. Available only when brand_safety is THIRD_PARTY. Enum values: IAS, OPEN_SLATE. To get the countries and regions that your ads can be deployed to based on your brand safety settings, use the /tools/regions/ endpoint. You need to pass in the brand safety type and brand safety partner."

  - name: "budget"
    type: number"
    description: "Ad budget. Returns 0.0 when Campaign Budget Optimization (budget_optimize_switch) is on."

  - name: "budget_mode"
    type: string"
    description: "Budget mode. If Campaign Budget Optimization is enabled, BUDGET_MODE_INFINITE will be returned. For more information about budget modes, see (Budget Settings)[https://ads.tiktok.com/marketing_api/docs?id=1701890928827393]."

  - name: "buy_impression"
    type: integer"
    description: "Impressions to be purchased. Returned when objective_type of the related campaign is RF_REACH."

  - name: "buy_reach"
    type: integer"
    description: "Purchased user reach. Returned when objective_type of the related campaign is RF_REACH."

  - name: "campaign_id"
    type: integer"
    description: "Campaign ID"
    primary-key: true

  - name: "carriers_v2"
    type: array"
    description: "Carriers that you want to target. A carrier is valid only when the in_use field for the carrier is true. For enum values (carrier_v2_id), see (Get carriers)[https://ads.tiktok.com/marketing_api/docs?id=1701890992039937]."
    subattributes:
    - name: "items"
      type: integer"
      description: "Carrier that you want to target."

  - name: "catalog_authorized_bc"
    type: integer"
    description: "For catalogs in Business Center, this field returns the ID of the Business Center that a catalog belongs to."

  - name: "catalog_id"
    type: integer"
    description: "Catalog ID。Return when the corresponding campaign objective_type is CATALOG_SALES."

  - name: "connection_type"
    type: array"
    description: "Device connection types that you want to target. Default: unlimited. For enum values, see (Enumeration - Connection Type)[https://ads.tiktok.com/marketing_api/docs?id=1701890985340929]."
    subattributes:
    - name: "items"
      type: string"
      description: "Device connection type that you want to target."

  - name: "conversion_bid"
    type: number"
    description: "Where you can set a target cost per conversion for oCPM(Optimized Cost per Mille)."

  - name: "conversion_window"
    type: string"
    description: "The time frame when you would like a conversion to happen after a user clicks on or views your ad. Your ad delivery will be optimized using the conversion data during the time frame you select. This setting will not impact your attribution data. For enum values, see (Enumeration - Conversion Window)[https://ads.tiktok.com/marketing_api/docs?id=1701890985340929]."

  - name: "cpv_video_duration"
    type: string"
    description: "Optimized video playback duration. Optional values include: SIX_SECONDS (video playback 6 seconds) and TWO_SECONDS (video playback 2 seconds)"

  - name: "create_time"
    type: string"
    format: "date-time"
    description: "Time at which the ad group was created."

  - name: "creative_material_mode"
    type: string"
    description: "The strategy that your creatives will be delivered. Note: When you choose automated ad, your creative materials will automatically be combined for delivery. Tiktok Ads' smart optimization algorithm is applied and will be used to achieve the best ad performance during delivery. Enum values: CUSTOM(custom), DYNAMIC(automated)"

  - name: "daily_retention_ratio"
    type: number"
    description: "Day 2 retention ratio. Formula: daily_retention_ratio = conversion_bid/deep_cpabid. Value range is (0,1]. Only valid when placement is PLACEMENT_PANGLE and deep_external_action is NEXT_DAY_OPEN."

  - name: "dayparting"
    type: string"
    description: "Ad delivery arrangement, in the format of a string that consists of 48 x 7 characters. Each character is mapped to a 30-minute timeframe from Monday to Sunday. Each character can be set to either 0 or 1. 1 represents delivery in the 30-minute timeframe, and 0 stands for non-delivery in the 30-minute timeframe. The first character is mapped to 0:01-0:30 of Monday; The second character is mapped to 0:31-1:00 of Monday, and the last character represents 23:31-0:00 Sunday. Note : Not specified, all-0, or all-1 are considered as full-time delivery."

  - name: "deep_bid_type"
    type: string"
    description: "Bidding strategy for in-app events. For enum values and their decriptions, see (Enumeration - Deep-level Bidding Strategy)[https://ads.tiktok.com/marketing_api/docs?id=1701890985340929]."

  - name: "deep_cpabid"
    type: number"
    description: "Specify bid price in this field after you've chosen a bidding strategy for in-app events, for example VO_MIN."

  - name: "deep_external_action"
    type: string"
    description: "The secondary goal when optimization goal (optimize_goal) is Install (INSTALL) or Value (VALUE). For enum values, see (Conversion events - Secondary-goal events)[https://ads.tiktok.com/marketing_api/docs?id=1701890988826626]."

  - name: "device_models"
    type: array"
    description: "List of device model IDs. For more details about device models, see (Enumeration-Device Models)[https://ads.tiktok.com/marketing_api/docs?id=1701890985340929]."
    subattributes:
    - name: "items"
      type: integer"
      description: "Device model ID"

  - name: "device_price"
    type: array"
    description: "Targeting device price range. 10000 means 1000+. The numbers must be in multiples of 50. Important: The upper limit you set will be added by 50 and the resulting new number will be used as the actual upper limit for device targeting. The actual upper limit is shown in the ad group settings in TikTok Ads Manager. If you set and get the price range of [0, 250], it actually means [0, 300]."
    subattributes:
    - name: "items"
      type: integer"
      description: "Device price."

  - name: "dpa_retargeting_type"
    type: string"
    description: "The types of ad redirection in the catalog. Returned when the corresponding campaign objective_type is CATALOG_SALES."

  - name: "enable_inventory_filter"
    type: boolean"
    description: "Inventory filtering (filtering security videos, hides unsafe videos), valid only for the PLACEMENT_TIKTOK placement. Optional values are: true to filter, false not to filter."

  - name: "excluded_audience"
    type: array"
    description: "A list of excluded audience IDs."
    subattributes:
    - name: "items"
      type: integer"
      description: "Audience ID"

  - name: "external_action"
    type: string"
    description: "Conversion event for the ad group. See (Conversion events)[https://ads.tiktok.com/marketing_api/docs?id=1701890988826626] for more."

  - name: "external_type"
    type: string"
    description: "Promotion type and you can decide where you'd like to promote your products using this field. For value definitions, see (Enumeration - Promotion Type)[https://ads.tiktok.com/marketing_api/docs?id=1701890985340929]."

  - name: "frequency"
    type: integer"
    description: "frequency, together with frequency_schedule, controls how often people see your ad (only available for REACH ads). For example, frequency = 2 frequency_schedule = 3 means 'show ads no more than twice every 3 day'."

  - name: "frequency_schedule"
    type: integer"
    description: "frequency, together with frequency, controls how often people see your ad (only available for REACH ads). See frequency fields for more"

  - name: "gender"
    type: string"
    description: "Gender that you want to target. Enum: GENDER_FEMALE,GENDER_MALE,GENDER_UNLIMITED"

  - name: "interest_category_v2"
    type: array"
    description: "Interest classification. If the interest is specified, users that do not meet interest target will be excluded during delivery. Do not specify if you wish to target everyone. Use /tools/interest_category/ endpoint to get the complete list of interest categories."
    subattributes:
    - name: "items"
      type: integer"
      description: "Interest category."

  - name: "interest_keywords"
    type: array"
    description: "IDs of interest keywords that you want to use to target audience. You can get interest keywords IDs by using the /tools/interest_keyword/recommend/ endpoint. For details, see (Get interest keywords)[https://ads.tiktok.com/marketing_api/docs?id=1707864878515202]."
    subattributes:
    - name: "items"
      type: integer"
      description: "ID of interest keywords that you want to use to target audience."

  - name: "ios_osv"
    type: string"
    description: "Audience minimum ios version. See (Appendix-OS Version)[https://ads.tiktok.com/marketing_api/docs?id=1701890995018753] for details."

  - name: "ios_quota_type"
    type: string"
    description: ""

  - name: "ios_target_device"
    type: string"
    description: "The iOS devices that you want to target.
    1. UNSET: This is the previous default value of the field.
    2. IOS14_MINUS: Devices with iOS 14.4 or earlier version that are not affected by the iOS 14 privacy update. This is the default value for ad groups that are created after the introduction of this field.
    3. IOS14_PLUS: Devices with iOS 14.5 and above. The iOS 14 privacy update has been enforced in this group of devices."

  - name: "is_comment_disable"
    type: boolean"
    description: "Whether to allow comments on your ads on TikTok. Enum values: 0 (allow), 1 (restrict). The default value is allow"

  - name: "is_hfss"
    type: boolean"
    description: "Whether the promoted product is HFSS foods (foods that are high in fat, salt, or sugar)"

  - name: "is_new_structure"
    type: boolean"
    description: "Whether the campaign is a new structure"

  - name: "is_share_disable"
    type: boolean"
    description: "Whether sharing to third-party platforms is disabled for ads in this ad group. Only valid for R&F ads."

  - name: "languages"
    type: array"
    description: "Codes of the languages that you want to target. For the list of languages codes supported, see (Enumeration - Language Code)[https://ads.tiktok.com/marketing_api/docs?id=1701890985340929]."
    subattributes:
    - name: "items"
      type: string"
      description: "Code of the language that you want to target."

  - name: "location"
    type: array"
    description: "IDs of the locations that you want to target. For enum values, see (Location IDs)[https://ads.tiktok.com/marketing_api/docs?id=1701890989574146]."
    subattributes:
    - name: "items"
      type: integer"
      description: "ID of the location that you want to target."

  - name: "modify_time"
    type: string"
    format: "date-time"
    description: "Time at which the ad group was Modified."
    replication-key: true
    primary-key: true

  - name: "operation_system"
    type: array"
    description: "Device operating systems that you want to target. Only one value is allowed. Enum: ANDROID, IOS"
    subattributes:
    - name: "items"
      type: string"
      description: "Device operating system that you want to target."

  - name: "opt_status"
    type: string"
    description: "Operational status. Enum: DISABLE (ad group is disabled), ENABLE (ad group is enabled), FROZEN (terminated and cannot be used again)"

  - name: "optimize_goal"
    type: string"
    description: "The measurable results that you'd like to drive your ads with. For enum values, see (Appendix - Optimization Goal)[https://ads.tiktok.com/marketing_api/docs?id=1701890985340929]."

  - name: "pacing"
    type: string"
    description: "You can choose between PACING_MODE_SMOOTH and PACING_MODE_FAST. For PACING_MODE_SMOOTH, the budget is allocated evenly within the scheduled time. PACING_MODE_FAST would consume budget and produce results as soon as possible. When Campaign Budget Optimization (budget_optimize_switch) is on, your setting will be ignored and it will be set as PACING_MODE_SMOOTH. Otherwise, this field is required."

  - name: "package"
    type: string"
    description: ""

  - name: "pangle_audience_package_exclude"
    type: array"
    description: "IDs of the Pangle audiences that you want to include. Valid only for Pangle placement. You can get audience IDs (package_id) by using the /pangle_flow_package/get/ endpoint. You need to set bind_type to INCLUDE. Do not specify this field and pangle_audience_package_exclude at the same time."
    subattributes:
    - name: "items"
      type: integer"
      description: "ID of the Pangle audience that you want to include."

  - name: "pangle_audience_package_include"
    type: array"
    description: "IDs of the Pangle audiences that you want to exclude. Valid only for Pangle placement. You can get audience IDs (package_id) by using the /pangle_flow_package/get/ endpoint. You need to set bind_type to EXCLUDE. Do not specify this field and pangle_audience_package_include at the same time."
    subattributes:
    - name: "items"
      type: integer"
      description: "ID of the Pangle audience that you want to exclude."

  - name: "pangle_block_app_list_id"
    type: array"
    description: "Pangle app block list ID."
    subattributes:
    - name: "items"
      type: integer"
      description: "Pangle app block list ID (single)."

  - name: "pixel_id"
    type: integer"
    description: "Pixel ID. Only application for landing pages."

  - name: "placement"
    type: array"
    description: "The apps where you want to deliver your ads. For enum values, see (Enumeration - Placement)[https://ads.tiktok.com/marketing_api/docs?id=1701890985340929]. If placement_type of the adgroup is PLACEMENT_TYPE_AUTOMATIC (Automatic placement), NONE will be returned for this field."
    subattributes:
    - name: "items"
      type: string"
      description: "The app where you want to deliver your ads."

  - name: "placement_type"
    type: string"
    description: "The placement strategy that decides where your ads will be shown. Allowed values: PLACEMENT_TYPE_AUTOMATIC (automatic placement), PLACEMENT_TYPE_NORMAL (manual placement)"

  - name: "product_set_id"
    type: integer"
    description: "ProductSet ID of the catalog. 0 means selecting all product sets. Return when the corresponding campaign objective_type is CATALOG_SALES."

  - name: "promotion_website_type"
    type: string"
    description: "Instant page type in your ad group. Currently, the only supported type is TIKTOK_NATIVE_PAGE, which stands for TikTok instant pages. null means no instant pages are used in the ad group."

  - name: "rf_buy_type"
    type: string"
    description: "Billing method of Reach & Frequency ad groups. For more details, see (Enumeration - Reach & Frequency Buy Type)[https://ads.tiktok.com/marketing_api/docs?id=1701890985340929]. Returned when objective_type of the related campaign is RF_REACH."

  - name: "rf_predict_cpr"
    type: integer"
    description: "The estimated cost per mile reach. Returned when objective_type of the related campaign is RF_REACH."

  - name: "rf_predict_frequency"
    type: integer"
    description: "The estimated show frequency. Returned when objective_type of the related campaign is RF_REACH."

  - name: "roas_bid"
    type: number"
    description: "ROAS goal for Value Optimization."

  - name: "schedule_end_time"
    type: string"
    format: "date-time"
    description: "Ad delivery end time (UTC+0). Format should be YYYY-MM-DD HH:MM:SS"

  - name: "schedule_start_time"
    type: string"
    format: "date-time"
    description: "Ad delivery start time (UTC+0). Format should be YYYY-MM-DD HH:MM:SS"

  - name: "schedule_type"
    type: string"
    description: "The schedule type can be either SCHEDULE_START_END or SCHEDULE_FROM_NOW. If you choose SCHEDULE_START_END, you need to specify a start time and an end time. If you choose SCHEDULE_FROM_NOW, you only need to specify a start time."

  - name: "skip_learning_phase"
    type: integer"
    description: "Whether to skip the learning stage. Optional values include: 0 (not skip), 1 (skip)"

  - name: "split_test_adgroup_ids"
    type: array"
    description: ""
    subattributes:
    - name: "items"
      type: integer"
      description: ""

  - name: "statistic_type"
    type: string"
    description: "conversion bid statistic type, bid for EVERYTIME (Each Purchase)/ NONE (Unique Purchase)"

  - name: "status"
    type: string"
    description: "Ad group status（secondary status). For enum values, see (Enumeration -Ad Group Status - Secondary Status)[https://ads.tiktok.com/marketing_api/docs?id=1701890985340929]. Note: This field is not returned in the sandbox environment because the ad group is not actually delivered."

  - name: "targeting_expansion"
    type: object"
    description: "Settings about targeting expansion"
    subattributes:
    - name: "expansion_types"
      type: array"
      description: "The target audience types that you want to expand"
      subattributes:
      - name: "items"
        type: string"
        description: "The target audience type that you want to expand"

    - name: "enable_expansion"
      type: boolean"
      description: "Whether to enable targeting expansion"


  - name: "video_download"
    type: string"
    description: "Whether users can download your video ads on TikTok. Allowed values: ALLOW_DOWNLOAD ,PREVENT_DOWNLOAD Default: ALLOW_DOWNLOAD."
---