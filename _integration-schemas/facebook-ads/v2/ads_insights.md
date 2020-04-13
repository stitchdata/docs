---
tap: "facebook-ads"
version: "2"

name: "ads_insights"
doc-link: https://developers.facebook.com/docs/marketing-api/insights/fields/
singer-schema: https://github.com/singer-io/tap-facebook/blob/master/tap_facebook/schemas/ads_insights.json
description: |
  The `ads_insights` table contains entries for each campaign/set/ad combination for each day, along with detailed statistics.

  **Note**: Data for deleted ads, adsets, and campaigns will not appear in this table even if the **Include data from deleted campaigns, ads, and adsets** option in the integration's settings is enabled.

  #### Segmented insights data

  To analyze data that's been segmented by various characteristics, consider tracking some of the other `ads_insights` tables in this integration. The following tables contain the same fields as this one (`ads_insights`), but include additional dimensions to segment the data:

  - [`ads_insights_age_and_gender`](#ads_insights_age_and_gender) - Data segmented by age and gender
  - [`ads_insights_country`](#ads_insights_country) - Data segmented by country
  - [`ads_insights_dma`](#ads_insights_dma) - Data segmented by DMA (Designated Market Area)
  - [`ads_insights_platform_and_device`](#ads_insights_platform_and_device) - Data segmented by platform and device
  - [`ads_insights_region`](#ads_insights_region) - Data segmented by region

replication-method: "Key-based Incremental"
attribution-window: true

attributes: 
  - name: "ad_id"
    type: "string"
    primary-key: true
    description: "The ID of the ad."
    foreign-key-id: "ad-id"

  - name: "adset_id"
    type: "string"
    primary-key: true
    description: "The ID of the ad set. An ad set is a group of ads that share the same budget, schedule, delivery optimization, and targeting."
    foreign-key-id: "adset-id"

  - name: "campaign_id"
    type: "string"
    primary-key: true
    description: "The ID of the campaign. Campaigns contain ad sets and ads."
    foreign-key-id: "campaign-id"

  - name: "date_start"
    type: "date-time"
    primary-key: true
    replication-key: true
    description: "The start date."

  - name: "date_stop"
    type: "date-time"
    description: "The end date."

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
    subattributes:
      - name: "action_target_id"
        type: "string"
        description: "The ID of the destination where people go after clicking on the ad. This could be your Facebook Page, an external URL for your conversion pixel, or an app configured with the Facebook SDK."

      - name: "action_type"
        type: "string"
        description: |
          {{ integration.cost-per-action-type.description | flatify }}

          **Note**: As of July 2018, Facebook has deprecated the following `action` types:

          {{ integration.cost-per-unique-action-type.deprecated-july-2018 | flatify }}

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

  - name: "account_id"
    type: "string"
    description: "The ID number of your ad account."
    foreign-key-id: "account-id"

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
    subattributes:
      - name: "value"
        type: "string"
        description: *action-type-value-description

      - name: "action_type"
        type: "string"
        description: |
          {{ integration.cost-per-action-type.description | flatify }}

          **Note**: Facebook has deprecated some values for this field. They are as follows:

          In July 2018:

          {{ integration.cost-per-unique-action-type.deprecated-july-2018 | flatify }}

          In October 2018:

          {{ integration.cost-per-unique-action-type.deprecated-october-2018 | flatify }}

  - name: "inline_post_engagement"
    type: "integer"
    description: "The total number of actions that people take involving the ad. Inline post engagements use a fixed 1-day-click attribution window."

  - name: "relevance_score"
    type: "object"
    description: "Details about the relevance score of the ad."
    subattributes:
      - name: "status"
        type: "string"
        description: |
          The status of the ad's relevance score.

          **Note:** Relevance scores are shown after ads receive more than 500 impressions. In addition, relevance scores are only applicable to ads and will not appear for ad sets and campaigns.

      - name: "score"
        type: "number"
        description: |
          A 1-10 rating that estimates how well the target audience is responding to the ad.

          Facebook's documentation states that: _"10 means we (Facebook) estimate the ad is highly relevant and 1 means we (Facebook) estimate it’s not very relevant."_

  - name: "inline_link_clicks"
    type: "integer"
    description: "The number of clicks on links to select destinations or experiences, on or off Facebook-owned properties. Inline link clicks use a fixed 1-day-click attribution window."

  - name: "cpc"
    type: "number"
    description: "The average cost for each click (all)."

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
    description: |
      Details about the average cost of a relevant action.

    doc-link: https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats/
    subattributes:
      - name: "value"
        type: "string"
        description: *action-type-value-description

      - name: "action_type"
        type: "string"
        description: |
          {{ integration.cost-per-action-type.description | flatify }}

          **Note**: Facebook has deprecated some values for this field. They are as follows:

          In July 2018:

          {{ integration.cost-per-action-type.deprecated-july-2018 | flatify }}

          In October 2018:

          {{ integration.cost-per-action-type.deprecated-october-2018 | flatify }}

  - name: "unique_link_clicks_ctr"
    type: "number"
    description: "The percentage of people who saw the ad and performed a link click."

  - name: "spend"
    type: "number"
    description: "The estimated total amount of money spent on the campaign, ad set, or ad during its schedule."

  - name: "cost_per_unique_click"
    type: "number"
    description: "The average cost of each unique click (all)."

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
---