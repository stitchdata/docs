---
tap: "snapchat-ads"
version: "1"
key: ""

name: "ad_squad_stats_hourly"
doc-link: https://developers.snapchat.com/api/docs/#get-ad-squad-stats
singer-schema: https://github.com/singer-io/tap-snapchat-ads/blob/master/tap_snapchat_ads/schemas/shared/stats.json
description: "This stream retrieves stats for the specified Ad Squad at HOUR granularity"

replication-method: "Key-based Incremental"

table-key-properties: "id, start_time"
valid-replication-keys: "end_time"

attributes:
  - name: "android_installs"
    type: "integer"
    description: "Number of Android App Installs"

  - name: "android_installs_app"
    type: "integer"
    description: ""

  - name: "android_installs_web"
    type: "integer"
    description: ""

  - name: "attachment_avg_view_time_millis"
    type: "integer"
    description: "Average Attachment View Time (milli-seconds)"

  - name: "attachment_frequency"
    type: "number"
    description: "Average number of Attachment Views per User Reached"

  - name: "attachment_impressions"
    type: "integer"
    description: ""

  - name: "attachment_quartile_1"
    type: "integer"
    description: "Long Form Video Views to 25%"

  - name: "attachment_quartile_2"
    type: "integer"
    description: "Long Form Video Views to 50%"

  - name: "attachment_quartile_3"
    type: "integer"
    description: "Long Form Video Views to 75%"

  - name: "attachment_total_view_time_millis"
    type: "integer"
    description: "Total Attachment View Time (milli-seconds)"

  - name: "attachment_uniques"
    type: "integer"
    description: "Number of unique attachment impressions"

  - name: "attachment_view_completion"
    type: "integer"
    description: "Long Form Video Views to completion"

  - name: "avg_screen_time_millis"
    type: "integer"
    description: "Average Top Snap view time across all impressions"

  - name: "avg_view_time_millis"
    type: "integer"
    description: "Use avg_screen_time_millis instead. Average Top Snap view time per User Reached"

  - name: "conversion_achievement_unlocked"
    type: "integer"
    description: "Number of attributed `ACHIEVEMENT_UNLOCKED` conversion events"

  - name: "conversion_achievement_unlocked_app"
    type: "integer"
    description: ""

  - name: "conversion_achievement_unlocked_web"
    type: "integer"
    description: ""

  - name: "conversion_ad_click"
    type: "integer"
    description: "Number of attributed `AD_CLICK` conversion events"

  - name: "conversion_ad_click_app"
    type: "integer"
    description: ""

  - name: "conversion_ad_click_web"
    type: "integer"
    description: ""

  - name: "conversion_ad_view"
    type: "integer"
    description: "Number of attributed `AD_VIEW` conversion events"

  - name: "conversion_ad_view_app"
    type: "integer"
    description: ""

  - name: "conversion_ad_view_web"
    type: "integer"
    description: ""

  - name: "conversion_add_billing"
    type: "integer"
    description: "Number of attributed `ADD_BILLING` conversion events"

  - name: "conversion_add_billing_app"
    type: "integer"
    description: ""

  - name: "conversion_add_billing_web"
    type: "integer"
    description: ""

  - name: "conversion_add_cart"
    type: "integer"
    description: "Number of attributed `ADD_CART` conversion events"

  - name: "conversion_add_cart_app"
    type: "integer"
    description: ""

  - name: "conversion_add_cart_web"
    type: "integer"
    description: ""

  - name: "conversion_add_to_wishlist"
    type: "integer"
    description: "Number of attributed `ADD_TO_WISHLIST` conversion events"

  - name: "conversion_add_to_wishlist_app"
    type: "integer"
    description: ""

  - name: "conversion_add_to_wishlist_web"
    type: "integer"
    description: ""

  - name: "conversion_app_opens"
    type: "integer"
    description: "Number of attributed `APP_OPEN` conversion events"

  - name: "conversion_app_opens_app"
    type: "integer"
    description: ""

  - name: "conversion_app_opens_web"
    type: "integer"
    description: ""

  - name: "conversion_complete_tutorial"
    type: "integer"
    description: "Number of attributed `COMPLETE_TUTORIAL` conversion events"

  - name: "conversion_complete_tutorial_app"
    type: "integer"
    description: ""

  - name: "conversion_complete_tutorial_web"
    type: "integer"
    description: ""

  - name: "conversion_invite"
    type: "integer"
    description: "Number of attributed `INVITE` conversion events"

  - name: "conversion_invite_app"
    type: "integer"
    description: ""

  - name: "conversion_invite_web"
    type: "integer"
    description: ""

  - name: "conversion_level_completes"
    type: "integer"
    description: "Number of attributed `LEVEL_COMPLETE` conversion events**"

  - name: "conversion_level_completes_app"
    type: "integer"
    description: ""

  - name: "conversion_level_completes_web"
    type: "integer"
    description: ""

  - name: "conversion_list_view"
    type: "integer"
    description: "Number of attributed `LIST_VIEW` conversion events++"

  - name: "conversion_list_view_app"
    type: "integer"
    description: ""

  - name: "conversion_list_view_web"
    type: "integer"
    description: ""

  - name: "conversion_login"
    type: "integer"
    description: "Number of attributed `LOGIN` conversion events"

  - name: "conversion_login_app"
    type: "integer"
    description: ""

  - name: "conversion_login_web"
    type: "integer"
    description: ""

  - name: "conversion_page_views"
    type: "integer"
    description: "Number of attributed `PAGE_VIEW` conversion events**"

  - name: "conversion_page_views_app"
    type: "integer"
    description: ""

  - name: "conversion_page_views_web"
    type: "integer"
    description: ""

  - name: "conversion_purchases"
    type: "integer"
    description: "Number of attributed `PURCHASE` conversion events"

  - name: "conversion_purchases_app"
    type: "integer"
    description: ""

  - name: "conversion_purchases_value"
    type: "integer"
    description: "Value of attributed `PURCHASE` conversion events (microcurrency in Ad Account’s currency)"

  - name: "conversion_purchases_value_app"
    type: "integer"
    description: ""

  - name: "conversion_purchases_value_web"
    type: "integer"
    description: ""

  - name: "conversion_purchases_web"
    type: "integer"
    description: ""

  - name: "conversion_rate"
    type: "integer"
    description: "Number of attributed `RATE` conversion events"

  - name: "conversion_rate_app"
    type: "integer"
    description: ""

  - name: "conversion_rate_web"
    type: "integer"
    description: ""

  - name: "conversion_reserve"
    type: "integer"
    description: "Number of attributed `CONVERSION_RESERVE` conversion events++"

  - name: "conversion_reserve_app"
    type: "integer"
    description: ""

  - name: "conversion_reserve_web"
    type: "integer"
    description: ""

  - name: "conversion_save"
    type: "integer"
    description: "Number of attributed `SAVE` conversion events"

  - name: "conversion_save_app"
    type: "integer"
    description: ""

  - name: "conversion_save_web"
    type: "integer"
    description: ""

  - name: "conversion_searches"
    type: "integer"
    description: "Number of attributed `SEARCH` conversion events"

  - name: "conversion_searches_app"
    type: "integer"
    description: ""

  - name: "conversion_searches_web"
    type: "integer"
    description: ""

  - name: "conversion_share"
    type: "integer"
    description: "Number of attributed `CONVERSION_SHARE` conversion events"

  - name: "conversion_share_app"
    type: "integer"
    description: ""

  - name: "conversion_share_web"
    type: "integer"
    description: ""

  - name: "conversion_sign_ups"
    type: "integer"
    description: "Number of attributed `SIGN_UP` conversion events"

  - name: "conversion_sign_ups_app"
    type: "integer"
    description: ""

  - name: "conversion_sign_ups_web"
    type: "integer"
    description: ""

  - name: "conversion_spend_credits"
    type: "integer"
    description: "Number of attributed `CONVERSION_SPEND_CREDITS` conversion events"

  - name: "conversion_spend_credits_app"
    type: "integer"
    description: ""

  - name: "conversion_spend_credits_web"
    type: "integer"
    description: ""

  - name: "conversion_start_checkout"
    type: "integer"
    description: "Number of attributed `START_CHECKOUT` conversion events"

  - name: "conversion_start_checkout_app"
    type: "integer"
    description: ""

  - name: "conversion_start_checkout_web"
    type: "integer"
    description: ""

  - name: "conversion_start_trial"
    type: "integer"
    description: "Number of attributed `CONVERSION_START_TRIAL` conversion events"

  - name: "conversion_start_trial_app"
    type: "integer"
    description: ""

  - name: "conversion_start_trial_web"
    type: "integer"
    description: ""

  - name: "conversion_subscribe"
    type: "integer"
    description: "Number of attributed `SUBSCRIBE` conversion events"

  - name: "conversion_subscribe_app"
    type: "integer"
    description: ""

  - name: "conversion_subscribe_web"
    type: "integer"
    description: ""

  - name: "conversion_view_content"
    type: "integer"
    description: "Number of attributed `VIEW_CONTENT` conversion events"

  - name: "conversion_view_content_app"
    type: "integer"
    description: ""

  - name: "conversion_view_content_web"
    type: "integer"
    description: ""

  - name: "custom_event_1"
    type: "integer"
    description: "Number of attributed `CUSTOM_EVENT_1` conversion events"

  - name: "custom_event_1_app"
    type: "integer"
    description: ""

  - name: "custom_event_1_web"
    type: "integer"
    description: ""

  - name: "custom_event_2"
    type: "integer"
    description: "Number of attributed `CUSTOM_EVENT_2` conversion events++"

  - name: "custom_event_2_app"
    type: "integer"
    description: ""

  - name: "custom_event_2_web"
    type: "integer"
    description: ""

  - name: "custom_event_3"
    type: "integer"
    description: "Number of attributed `CUSTOM_EVENT_3` conversion events++"

  - name: "custom_event_3_app"
    type: "integer"
    description: ""

  - name: "custom_event_3_web"
    type: "integer"
    description: ""

  - name: "custom_event_4"
    type: "integer"
    description: "Number of attributed `CUSTOM_EVENT_4` conversion events++"

  - name: "custom_event_4_app"
    type: "integer"
    description: ""

  - name: "custom_event_4_web"
    type: "integer"
    description: ""

  - name: "custom_event_5"
    type: "integer"
    description: "Number of attributed `CUSTOM_EVENT_5` conversion events++"

  - name: "custom_event_5_app"
    type: "integer"
    description: ""

  - name: "custom_event_5_web"
    type: "integer"
    description: ""

  - name: "end_time"
    type: "date-time"
    description: "End Time (ISO 8601)"
    replication-key: true

  - name: "finalized_data_end_time"
    type: "date-time"
    description: "This attribute defines the time up until when non-conversion reporting metrics are finalized. You can query for all metrics before this time including uniques and reach and they will have the final numbers. For any time after the finalized_data_end_time the metrics are still undergoing de-duplication and finalization and may change accordingly"

  - name: "frequency"
    type: "number"
    description: "Average number of Impressions per User Reached"

  - name: "granularity"
    type: "string"
    description: "Metrics granularity. Example: HOUR"

  - name: "id"
    primary-key: true
    type: "string"
    description: "AD Squad ID"

  - name: "impressions"
    type: "integer"
    description: "Impression Count"

  - name: "ios_installs"
    type: "integer"
    description: "Number of iOS App Installs"

  - name: "ios_installs_app"
    type: "integer"
    description: ""

  - name: "ios_installs_web"
    type: "integer"
    description: ""

  - name: "quartile_1"
    type: "integer"
    description: "Video Views to 25%"

  - name: "quartile_2"
    type: "integer"
    description: "Video Views to 50%"

  - name: "quartile_3"
    type: "integer"
    description: "Video Views to 75%"

  - name: "screen_time_millis"
    type: "integer"
    description: "Total Time Spent on top Snap Ad (milliseconds)"

  - name: "spend"
    type: "integer"
    description: "Amount Spent (micro-currency)"

  - name: "start_time"
    type: "date-time"
    description: "End Time (ISO 8601)"
    primary-key: true

  - name: "swipe_up_attribution_window"
    type: "string"
    description: "Attribution window for swipe ups"

  - name: "swipe_up_percent"
    type: "integer"
    description: ""

  - name: "swipes"
    type: "integer"
    description: "% of Impressions that Swiped-Up"

  - name: "total_installs"
    type: "integer"
    description: "Total number of App Installs"

  - name: "total_installs_app"
    type: "integer"
    description: ""

  - name: "total_installs_web"
    type: "integer"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "uniques"
    type: "integer"
    description: "Number of unique impressions"

  - name: "video_views"
    type: "integer"
    description: "The total number of impressions that meet the qualifying video view criteria of at least 2 seconds of consecutive watch time or a swipe up action on the Top Snap"

  - name: "video_views_15s"
    type: "integer"
    description: "The total number of impressions that meet the qualifying video view criteria of at least 15 seconds, or 97% completion if it’s shorter than 15 seconds, or a swipe up action on the ad"

  - name: "video_views_time_based"
    type: "integer"
    description: "The total number of impressions that meet the qualifying video view criteria of at least 2 seconds, not including swipe ups"

  - name: "view_attribution_window"
    type: "string"
    description: "Attribution window for views"

  - name: "view_completion"
    type: "integer"
    description: "Video Views to completion"

  - name: "view_time_millis"
    type: "integer"
    description: "Use screen_time_millis instead. Total Time Spent on top Snap Ad (milliseconds)"
---