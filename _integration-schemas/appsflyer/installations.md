---
tap: "appsflyer"
# version: "1.0"

name: "installations"
doc-link: https://support.appsflyer.com/hc/en-us/articles/208387843-Raw-Data-Reports-V5-
singer-schema: https://github.com/singer-io/tap-appsflyer/blob/master/tap_appsflyer/schemas/raw_data/installations.json
description: |
  The `installations` table contains information about iOS and Android app installations.

replication-method: "Key-based Incremental"

attributes:
  - name: "appsflyer_id"
    type: "string"
    primary-key: true
    description: "The unique ID for the event."

  - name: "event_time"
    type: "string"
    primary-key: true
    description: "The time the event occurred."

  - name: "event_name"
    type: "string"
    primary-key: true
    description: "The name of the event."

  - name: "advertising_id"
    type: "string"
    description: "A user-resettable, unique, anonymous ID for advertising provided by Google Play services."

  - name: "android_id"
    type: "string"
    description: "For Android, the customer's Android device ID."

  - name: "app_id"
    type: "string"
    description: "The ID of the app that was installed."

  - name: "app_version"
    type: "string"
    description: "The version of the app that was installed."

  - name: "app_name"
    type: "string"
    description: "The name of the app that was installed."

  - name: "af_ad"
    type: "string"
    description: "**For link tracking**. The name of the ad."

  - name: "af_ad_id"
    type: "string"
    description: "**For link tracking**. The ad ID."

  - name: "af_ad_type"
    type: "string"
    description: |
      **For link tracking**. The type of ad. Possible values are:

      - `search_text`
      - `banner`
      - `interstitial`
      - `video`
      - `rewarded_video`
      - `playable`
      - `sponsored_content`
      - `audio`

  - name: "af_adset"
    type: "string"
    description: "**For link tracking**. The adset name, provided by the advertiser."

  - name: "af_adset_id"
    type: "string"
    description: "**For link tracking**. The adset ID."

  - name: "af_attribution_lookback"
    type: "string"
    description: |
      **For link tracking**. The time period for which {{ integration.display_name }} attributes installs to the media source, following the lead's view of an add. Possible values are:

      - 1 to 48 hours (`1h-48h`)
      - 1 to 7 days (`1d - 7d`)

  - name: "af_c_id"
    type: "string"
    description: "**For link tracking**. The campaign ID."

  - name: "af_channel"
    type: "string"
    description: "**For link tracking**. The channel of the media source, such as YouTube for Google, Instagram for Facebook, etc."

  - name: "af_cost_currency"
    type: "string"
    description: "**For link tracking**. The currency that `af_cost_value` is in. Refer to [XE.com](http://www.xe.com/symbols.php#section1) for a list of possible values."

  - name: "af_cost_model"
    type: "string"
    description: |
      **For link tracking**. The cost model of the ad. Possible values are:

      - `CPC`
      - `CPA`
      - `CPM`
      - `Other`

      **Note:** AppsFlyer currently calculates all cost according to `CPA`, regardless of the value in this field.

  - name: "af_cost_value"
    type: "string"
    description: "**For link tracking**. The cost in original currency."

  - name: "af_reengagement_window"
    type: "string"
    description: "**For link tracking**. The number of days in which an event can be attributed to a re-targeting campaign."

  - name: "af_keywords"
    type: "string"
    description: "**For link tracking**. The keywords list for text-targeted campaigns."

  - name: "af_prt"
    type: "string"
    description: "**For link tracking**. The agency account name."

  - name: "af_siteid"
    type: "string"
    description: "**For link tracking**. The ad network publisher ID."

  - name: "af_sub1"
    type: "string"
    description: "**For link tracking**. A custom parameter, defined by you."

  - name: "af_sub2"
    type: "string"
    description: "**For link tracking**. A custom parameter, defined by you."

  - name: "af_sub3"
    type: "string"
    description: "**For link tracking**. A custom parameter, defined by you."

  - name: "af_sub4"
    type: "string"
    description: "**For link tracking**. A custom parameter, defined by you."

  - name: "af_sub5"
    type: "string"
    description: "**For link tracking**. A custom parameter, defined by you."

  - name: "af_sub_siteid"
    type: "string"
    description: "**For link tracking**. The ad sub-network/publisher ID."

  - name: "attributed_touch_type"
    type: "string"
    description: "The type of the touch {{ integration.display_name }} attributed to."

  - name: "attributed_touch_time"
    type: "string"
    description: "The time of the touch {{ integration.display_name }} attributed to."

  - name: "bundle_id"
    type: "string"
    description: "The bundle ID, used to match a single app or a group of apps (for iOS)."

  - name: "campaign"
    type: "string"
    description: "**For link tracking**. The campaign name."

  - name: "carrier"
    type: "string"
    description: "The name of the cellular network operator."

  - name: "city"
    type: "string"
    description: "The city, based on IP address (`ip`)."

  - name: "contributor1_af_prt"
    type: "string"
    description: "The contribution parter."

  - name: "contributor1_media_source"
    type: "string"
    description: "The media source of the contributor."

  - name: "contributor1_campaign"
    type: "string"
    description: "The campaign of the contributor."

  - name: "contributor1_touch_type"
    type: "string"
    description: |
      The type of the touch. Possible values are:

      - `click`
      - `impression`
      - `tv`

  - name: "contributor1_touch_time"
    type: "string"
    description: "The time of the touch."

  - name: "contributor2_af_prt"
    type: "string"
    description: "The second contribution partner."

  - name: "contributor2_media_source"
    type: "string"
    description: "The media source of the second contributor."

  - name: "contributor2_campaign"
    type: "string"
    description: "The campaign of the second contributor."

  - name: "contributor2_touch_type"
    type: "string"
    description: |
      The type of the touch. Possible values are:

      - `click`
      - `impression`
      - `tv`

  - name: "contributor2_touch_time"
    type: "string"
    description: "The time of the touch."

  - name: "contributor3_af_prt"
    type: "string"
    description: "The third contribution partner."

  - name: "contributor3_media_source"
    type: "string"
    description: "The media source of the third contributor."

  - name: "contributor3_campaign"
    type: "string"
    description: "The campaign of the third contributor."

  - name: "contributor3_touch_type"
    type: "string"
    description: |
      The type of touch. Possible values are:

      - `click`
      - `impression`
      - `tv`

  - name: "contributor3_touch_time"
    type: "string"
    description: "The time of the touch."

  - name: "country_code"
    type: "string"
    description: "The customer's country code."

  - name: "customer_user_id"
    type: "integer"
    description: "The customer's user ID."

  - name: "device_type"
    type: "string"
    description: "The commercial model name of the customer's device. For example: `iPhone7`"

  - name: "dma"
    type: "string"
    description: "The Designated Market Area, or the geographical areas in the US where local TV viewing is measured by the Nielsen company."

  - name: "event_revenue"
    type: "string"
    description: "The revenue created as a result of the event."

  - name: "event_revenue_usd"
    type: "string"
    description: "The amount of the revenue created, in USD."

  - name: "event_revenue_currency"
    type: "string"
    description: "The amount of the revenue in local currency."

  - name: "event_source"
    type: "string"
    description: |
      The source of the event. Possible values are `SDK` or `S2S` (Server to Server).

  - name: "event_value"
    type: "string"
    description: "The value of the event."

  - name: "http_referrer"
    type: "string"
    description: "The address of the webpage that linked to the AppsFlyer click URL."

  - name: "idfa"
    type: "string"
    description: "For iOS, the device IDFA."

  - name: "idfv"
    type: "string"
    description: "The app-level identifier for a specific vendor."

  - name: "install_time"
    type: "string"
    description: "The time of the first launch after installation took place."

  - name: "imei"
    type: "string"
    description: "For Android and iOS, the IMEI of the customer's device."

  - name: "ip"
    type: "string"
    description: "The customer's IP address."

  - name: "is_primary_attribution"
    type: "boolean"
    description: |
      During a re-engagement window, {{ integration.display_name }} can attribute to either the original media source (prior to the re-engagement) or to the re-engagement media source. While the event is within the re-engagement window, the original media source will not be the primary attribution. Outside of the re-engagement window, it will be the primary attribution.

  - name: "is_receipt_validated"
    type: "boolean"
    description: "If `true`, the receipt for the purchase was validated."
    doc-link: https://www.appsflyer.com/mobile-fraud-glossary/receipt-validation/

  - name: "is_retargeting"
    type: "boolean"
    description: "**For link tracking**. Indicates if a click or impression event is considered from a retargeting campaign."

  - name: "language"
    type: "string"
    description: "The language the customer's device uses."

  - name: "media_source"
    type: "string"
    description: "The regular networks (excluding FB) that appear on the link."

  - name: "operator"
    type: "string"
    description: "The name of the SIM provider for the customer's device."

  - name: "original_url"
    type: "string"
    description: "The click/impression URL."

  - name: "os_version"
    type: "string"
    description: "The version of the operating system the customer's device uses."

  - name: "platform"
    type: "string"
    description: |
      The platform of the customer's device. Possible values are:

      - `iOS`
      - `Android`
      - `Windows`
      - `Mobile`

  - name: "postal_code"
    type: "string"
    description: "The customer's postal code, based on IP address (`ip`)."

  - name: "region"
    type: "string"
    description: "The customer's region, based on IP address (`ip`)."

  - name: "retargeting_conversion_type"
    type: "string"
    description: "**For link tracking**. The re-engagement/re-attribution type."

  - name: "sdk_version"
    type: "string"
    description: "The version of the AppsFlyer SDK."

  - name: "state"
    type: "string"
    description: "The customer's state, based on IP address (`ip`)."

  - name: "user_agent"
    type: "string"
    description: "The user agent for the URL."

  - name: "wifi"
    type: "boolean"
    description: "If `true`, the installation occurred over WiFi."
---