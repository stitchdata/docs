---
tap: "tiktok-ads"
version: "1"
key: "ad-insights"

name: "ad_insights"
doc-link: https://ads.tiktok.com/marketing_api/docs?id=1707957200780290
singer-schema: https://github.com/singer-io/tap-tiktok-ads/tree/master/tap_tiktok_ads/schemas/ad_insights.json
description: ""

replication-method: "Key-based Incremental"

table-key-properties: "advertiser_id, ad_id, adgroup_id, campaign_id, stat_time_day"
valid-replication-keys: "stat_time_day"

attributes:
  - name: "ad_id"
    type: integer"
    description: "Ad ID"
    primary-key: true

  - name: "ad_name"
    type: string"
    description: "Ad name. Supported in Ad level."

  - name: "ad_text"
    type: string"
    description: "Ad title. Supported in Ad level."

  - name: "adgroup_id"
    type: integer"
    description: "Ad group ID. Supported in Ad level."
    primary-key: true

  - name: "adgroup_name"
    type: string"
    description: "Ad group name. Supported in Ad Group and Ad level."

  - name: "advertiser_id"
    type: integer"
    description: "Advertiser ID"
    primary-key: true

  - name: "average_video_play"
    type: number"
    description: "Video Average Watch Time Per Video View. The average time your video was played per single video view, including any time spent replaying the video."

  - name: "average_video_play_per_user"
    type: number"
    description: "Video Average Watch Time Per Person. The average time your video was played per person, including any time spent replaying the video. This metric is estimated."

  - name: "campaign_id"
    type: integer"
    description: "Campaign ID. Supported in Ad Group and Ad level."
    primary-key: true

  - name: "campaign_name"
    type: string"
    description: "Campaign name. Supported in Campaign, Ad Group and Ad level."

  - name: "clicks"
    type: integer"
    description: "The number of clicks on your ads."

  - name: "clicks_on_music_disc"
    type: integer"
    description: "The number of clicks on the official music in your Boosted TikTok ad during the campaign. Available only if you are on the allowlist for the Boosted TikTok feature."

  - name: "comments"
    type: integer"
    description: "Paid Comments. The number of comments your video creative received within 1 day of a user seeing a paid ad."

  - name: "conversion"
    type: integer"
    description: "The number of times your ad achieved an outcome, based on the secondary goal you selected. As one campaign may have a number of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)"

  - name: "conversion_rate"
    type: number"
    description: "CPA. The average amount of money you've spent on a conversion.(The total count is calculated based on the time each ad impression occurred.)"

  - name: "cost_per_1000_reached"
    type: string"
    description: "The average cost to reach 1,000 unique users. This metric is estimated."

  - name: "cost_per_100_reached"
    type: number"
    description: "The average cost to reach 100 unique users. This metric is estimated."

  - name: "cost_per_conversion"
    type: number"
    description: "The average amount of money you've spent on a conversion.(The total count is calculated based on the time each ad impression occurred.)"

  - name: "cost_per_result"
    type: number"
    description: "The average cost for each result from your ads. As one campaign may have a number of different optimization goals, this metric is not supported at advertiser level or campaign level. Please go to ad groups or ads to view the cost per result. (The total count is calculated based on the time each ad impression occurred.)"

  - name: "cost_per_secondary_goal_result"
    type: number"
    description: "The average cost for each secondary goal result from your adverts. As one campaign may have a number of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)"

  - name: "cpc"
    type: number"
    description: "The average amount of money you've spent on a click."

  - name: "cpm"
    type: number"
    description: "The average amount of money you've spent per 1,000 impressions."

  - name: "ctr"
    type: number"
    description: "The percentage of times people saw your ad and performed a click."

  - name: "dpa_target_audience_type"
    type: string"
    description: "The Audience that DPA products target. Supported at Adgroup or Ad levels in both synchronous and asynchronous reports."

  - name: "follows"
    type: integer"
    description: "The number of new followers that were gained within 1 day of a user seeing a paid ad. This metric is only for Boosted TikToks."

  - name: "frequency"
    type: number"
    description: "The average number of times each person saw your ad."

  - name: "impressions"
    type: integer"
    description: "The number of times your ads were on screen."

  - name: "likes"
    type: integer"
    description: "Paid Likes. The number of likes your video creative received within 1 day of a user seeing a paid ad."

  - name: "mobile_app_id"
    type: string"
    description: "Mobile App ID. Examples are, App Store: https://apps.apple.com/us/app/angry-birds/id343200656; Google Play：https://play.google.com/store/apps/details?id=com.rovio.angrybirds. Supported in Ad Group and Ad level. Returned if the promotion type of one Ad Group is App."

  - name: "placement"
    type: string"
    description: "Placement. Supported in Ad Group and Ad level."

  - name: "profile_visits"
    type: integer"
    description: "The number of profile visits the ad drove during the campaign. This metric is only for Boosted TikToks."

  - name: "profile_visits_rate"
    type: number"
    description: "The rate of profile visits per impression the paid ad drove during the campaign. This metric is only for Boosted TikToks."

  - name: "promotion_type"
    type: string"
    description: "It can be app, website, or others. Supported at Adgroup and Ad levels in both synchronous and asynchronous reports."

  - name: "reach"
    type: integer"
    description: "The number of unique users who saw your ads at least once. This metric is estimated."

  - name: "real_time_conversion"
    type: integer"
    description: "The number of times your ad achieved an outcome, based on the objective and settings you selected. (The total count is based on when the conversion actually happened.)"

  - name: "real_time_conversion_rate"
    type: number"
    description: "The percentage of results you received out of all the clicks of your ads. (The total count is based on when the conversion actually happened.)"

  - name: "real_time_cost_per_conversion"
    type: number"
    description: "The average amount of money you've spent on a conversion. (The total count is based on when the conversion actually happened.)"

  - name: "real_time_cost_per_result"
    type: number"
    description: "As a campaign may have different optimization goals, tthis metric is not supported at advertiser level or campaign level. Please go to the ad group section to view the cost per Result. (The total count is based on when the conversion actually happened.)"

  - name: "real_time_result"
    type: integer"
    description: "The number of times your ad achieved an outcome, based on the optimization goal you selected. As a campaign may have different optimization goals, this metric is not supported at advertiser level or campaign level. Please go to the ad group section to view the result. (The total count is based on when the conversion actually happened.)"

  - name: "real_time_result_rate"
    type: number"
    description: "As a campaign may have different optimization goals, this metric is not supported at advertiser level or campaign level. Please go to the ad group section to view the Result Rate. (The total count is based on when the conversion actually happened.)"

  - name: "result"
    type: integer"
    description: "The number of times your ad achieved an outcome, based on the optimization goal you selected. As one campaign may have a number of different optimization goals, this metric is not supported at advertiser level or campaign level. Please go to ad groups or ads to view the results. (The total count is calculated based on the time each ad impression occurred.)"

  - name: "result_rate"
    type: number"
    description: "The percentage of results you achieved out of all of the views/clicks on your ads. As one campaign may have a number of different optimization goals, this metric is not supported at advertiser level or campaign level. Please go to ad groups or ads to view the result rate. (The total count is calculated based on the time each ad impression occurred.)"

  - name: "secondary_goal_result"
    type: integer"
    description: "The number of times your ad achieved an outcome, based on the secondary goal you selected. As one campaign may have a number of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)"

  - name: "secondary_goal_result_rate"
    type: number"
    description: "The percentage of secondary goal results you achieved out of all of the installs of your adverts. As one campaign may have a number of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. The total count is calculated based on the time each ad impression occurred.."

  - name: "shares"
    type: integer"
    description: "Paid Shares. The number of shares your video creative received within 1 day of a user seeing a paid ad."

  - name: "spend"
    type: number"
    description: "Total Cost. The estimated total amount of money you've spent on your campaign, ad group or ad during its schedule."

  - name: "stat_time_day"
    type: string"
    format: "date-time"
    description: ""
    replication-key: true
    primary-key: true

  - name: "tt_app_id"
    type: string"
    description: "TikTok App ID. TikTok App ID, the App ID you used when creating an Ad Group. Supported in Ad Group and Ad level. Returned if the promotion type of one Ad Group is App."

  - name: "tt_app_name"
    type: string"
    description: "TikTok App Name. The name of your TikTok App. Supported in Ad Group and Ad level. Returned if the promotion type of one Ad Group is App."

  - name: "video_play_actions"
    type: integer"
    description: "Video Views. The number of times your video starts to play. Replays will not be counted."

  - name: "video_views_p100"
    type: integer"
    description: "Video Views at 100%. The number of times your video was played at 100% of its length. Replays will not be counted."

  - name: "video_views_p25"
    type: integer"
    description: "Video Views at 25%. The number of times your video was played at 25% of its length. Replays will not be counted."

  - name: "video_views_p50"
    type: integer"
    description: "Video Views at 50%. The number of times your video was played at 50% of its length. Replays will not be counted."

  - name: "video_views_p75"
    type: integer"
    description: "Video Views at 75%. The number of times your video was played at 75% of its length. Replays will not be counted."

  - name: "video_watched_2s"
    type: integer"
    description: "2-Second Video Views. The number of times your video played for at least 2 seconds. Replays will not be counted."

  - name: "video_watched_6s"
    type: integer"
    description: "6-Second Video Views. The number of times your video played for at least 6 seconds, or completely played. Replays will not be counted."


