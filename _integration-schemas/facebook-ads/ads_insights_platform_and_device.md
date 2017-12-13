---
tap: "facebook-ads"
version: 1.0

name: "ads_insights_platform_and_device"
doc-link: https://developers.facebook.com/docs/marketing-api/insights/fields/
singer-schema: https://github.com/singer-io/tap-facebook/blob/master/tap_facebook/schemas/ads_insights_platform_and_device.json
description: |
  The `ads_insights_country` table contains entries for each campaign/set/ad combination for each day, along with detailed statistics, segmented by publisher platform, platform position, and device.

  **Note:** This table contains the same fields as the [`ads_insights`](#ads_insights) table, with the exception of the following fields:

  - `publisher_platform`
  - `platform_position`
  - `impression_device`

replication-method: "Incremental"
attribution-window: true

attributes: 
  - name: "ad_id"
    type: "string"
    primary-key: true
    description: "The ID of the ad."

  - name: "adset_id"
    type: "string"
    primary-key: true
    description: "The ID of the ad set. An ad set is a group of ads that share the same budget, schedule, delivery optimization, and targeting."

  - name: "campaign_id"
    type: "string"
    primary-key: true
    description: "The ID of the campaign. Campaigns contain ad sets and ads."

  - name: "date_start"
    type: "date-time"
    primary-key: true
    replication-key: true
    description: "The start date of the ad."

  - name: "publisher_platform"
    type: "string"
    primary-key: true
    description: "The publishing platform by which the data is segmented. Ex: `facebook` or `instagram`"

  - name: "platform_position"
    type: "string"
    primary-key: true
    description: "The platform position by which the data is segmented."

  - name: "impression_device"
    type: "string"
    primary-key: true
    description: "The type of device by which the data is segmented."

  - name: "date_stop"
    type: "date-time"
    description: "The end date of the ad."

  - name: "ad_name"
    type: "integer"
    description: "The name of the ad."

  - name: "adset_name"
    type: "string"
    description: "The name of the adset."

  - name: "campaign_name"
    type: "integer"
    description: "The name of the campaign."

  - name: "clicks"
    type: "integer"
    description: "The number of clicks on your ads."

  - name: "website_ctr"
    type: "array"
    description: "The percentage of times people saw the ad and performed a link click."
    doc-link: https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats/
    array-attributes:
      - name: "action_target_id"
        type: "string"
        description: "The ID of the destination where people go after clicking on the ad. This could be your Facebook Page, an external URL for your conversion pixel, or an app configured with the Facebook SDK."

      - name: "action_type"
        type: "string"
        description: &action-type-description |
          The kind of actions taken on the ad, Page, app, or event after your ad was served to someone, even if they didn't click on it.

          Action types include Page likes, app installs, conversions, event responses, and more.

      - name: "value"
        type: "number"
        description: &action-type-value-description |
          The metric value of the default attribution window.

      - name: "action_destination"
        type: "string"
        description: "The destination where people go after clicking on the ad. This could be your Facebook Page, an external URL for your conversion pixel, or an app configured with the Facebook SDK."

  - name: "unique_inline_link_click_ctr"
    type: "number"
    description: "The percentage of times people saw the ad and performed a link click. Inline click-through rate uses a fixed 1-day-click attribution window."

  - name: "frequency"
    type: "number"
    description: "The average number of times each person saw your ad."

  - name: "total_actions"
    type: "integer"
    description: "The total number of actions people took that are attributed to the ad. Actions may include engagement, clicks, or conversions."

  - name: "account_id"
    type: "string"
    description: "The ID number of your ad account."

  - name: "account_name"
    type: "string"
    description: "The name of your ad account."

  - name: "canvas_avg_view_time"
    type: "number"
    description: "The average total time, in seconds, that people spent viewing a Facebook Canvas."

  - name: "unique_inline_link_clicks"
    type: "integer"
    description: "The number of people who performed an inline link click."

  - name: "cost_per_unique_action_type"
    type: "array"
    description: "Details about the average cost of unique actions."
    doc-link: https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats/
    array-attributes:
      - name: "value"
        type: "string"
        description: *action-type-value-description

      - name: "action_type"
        type: "string"
        description: *action-type-description

  - name: "social_reach"
    type: "integer"
    description: "The number of people who saw the ad when displayed with social information, which shows other Facebook friends who engaged with the Facebook Page or ad."

  - name: "inline_post_engagement"
    type: "integer"
    description: "The total number of actions that people take involving the ad. Inline post engagements use a fixed 1-day-click attribution window."

  - name: "relevance_score"
    type: "object"
    description: "Details about the relevance score of the ad."
    object-attributes:
      - name: "status"
        type: "string"
        description: |
          The status of the ad's relevance score.

          **Note:** Relevance scores are shown after ads receive more than 500 impressions. In addition, relevance scores are only applicable to ads and will not appear for ad sets and campaigns.

      - name: "negative_feedback"
        type: "string"
        description: "A string that indicates the level of negative feedback received about the ad. Ex: `LOW`"

      - name: "positive_feedback"
        type: "string"
        description: "A string that indicates the level of positive feedback received about the ad. Ex: `HIGH`"

      - name: "score"
        type: "number"
        description: |
          A 1-10 rating that estimates how well the target audience is responding to the ad.

          Facebook's documentation states that: _"10 means we (Facebook) estimate the ad is highly relevant and 1 means we (Facebook) estimate it’s not very relevant."_

  - name: "social_clicks"
    type: "integer"
    description: "The number of clicks (all) when the ad was displayed with social information, which shows other Facebook friends who engaged with the Facebook Page or ad."

  - name: "inline_link_clicks"
    type: "integer"
    description: "The number of clicks on links to select destinations or experiences, on or off Facebook-owned properties. Inline link clicks use a fixed 1-day-click attribution window."

  - name: "unique_social_clicks"
    type: "integer"
    description: "The number of clicks on links to select destinations or experiences, on or off Facebook-owned properties. Inline link clicks use a fixed 1-day-click attribution window."

  - name: "cpc"
    type: "number"
    description: "The average cost for each click (all)."

  - name: "unique_social_clicks"
    type: "integer"
    description: "The number of people who performed a click (all) on the ad when it was displayed with social information, which shows other Facebook friends who engaged with the Page or ad."

  - name: "call_to_action_clicks"
    type: "integer"
    description: "The number of times people clicked the call-to-action button on the ad."

  - name: "cost_per_total_action"
    type: "number"
    description: "The average cost for a relevant action."

  - name: "cost_per_unique_inline_link_click"
    type: "number"
    description: "The average cost of each unique inline link click."

  - name: "cpm"
    type: "number"
    description: "The average cost for 1,000 impressions."

  - name: "cost_per_inline_post_engagement"
    type: "number"
    description: "The average cost of each inline post engagement."

  - name: "inline_link_click_ctr"
    type: "number"
    description: "The percentage of time people saw your ads and performed an inline link click."

  - name: "cpp"
    type: "number"
    description: "The average cost to reach 1,000 people."

  - name: "cost_per_action_type"
    type: "array"
    description: "Details about the average cost of a relevant action."
    doc-link: https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats/
    array-attributes:
      - name: "value"
        type: "string"
        description: *action-type-value-description

      - name: "action_type"
        type: "string"
        description: *action-type-description

  - name: "unique_link_clicks_ctr"
    type: "number"
    description: "The percentage of people who saw the ad and performed a link click."

  - name: "social_reach"
    type: "number"
    description: "The number of people who saw the ad when displayed with social information, which shows other Facebook friends who engaged with the Facebook Page or ad."

  - name: "spend"
    type: "number"
    description: "The estimated total amount of money spent on the campaign, ad set, or ad during its schedule."

  - name: "cost_per_unique_click"
    type: "number"
    description: "The average cost of each unique click (all)."

  - name: "total_action_value"
    type: "number"
    description: "The total value of all conversions contributed to the ad."

  - name: "unique_clicks"
    type: "integer"
    description: "The number of people who performed a click (all)."

  - name: "social_spend"
    type: "number"
    description: "The total amount spent so far for the ad showed with social information. Ex: `Stitch Data likes this.`"

  - name: "reach"
    type: "integer"
    description: |
      The number of people who saw the ad at least once.

      `reach` is different than `impressions`, which may include multiple views of the ads by the same people.

  - name: "canvas_avg_view_percent"
    type: "number"
    description: "The average percentage of the Facebook Canvas that people saw."

  - name: "social_impressions"
    type: "integer"
    description: "The number of times the ad was viewed when displayed with social information, which shows Facebook friends who engaged with the Facebook Page or ad."

  - name: "objective"
    type: "string"
    description: "The objective selected for the campaign. This reflects the goal you want to achieve with your advertising."

  - name: "impressions"
    type: "integer"
    description: "The number of times the ad was on screen."

  - name: "unique_ctr"
    type: "number"
    description: "The percentage of people who saw your ad and performed a unique click (all)."

  - name: "cost_per_inline_link_click"
    type: "number"
    description: "The average cost of each inline link click."

  - name: "ctr"
    type: "number"
    description: "The percentage of times people saw your ad and performed a click (all)."

  - name: "total_unique_actions"
    type: "integer"
    description: "The number of people who took an action that was attributed to the ad."
---