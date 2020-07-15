---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "twitter-ads"

version: "1"

foreign-keys:
  - id: "account-id"
    table: "accounts"
    attribute: "account_id"
    all-foreign-keys:
      - table: "account_media"
      - table: "accounts"
        join-on: "id"
      - table: "campaigns"
      - table: "cards_image_app_download"
      - table: "cards_image_conversation"
      - table: "cards_image_direct_message"
      - table: "cards_poll"
      - table: "cards_video_app_download"
      - table: "cards_video_conversation"
      - table: "cards_video_direct_message"
      - table: "cards_video_website"
      - table: "cards_website"
      - table: "funding_instruments"
      - table: "line_item_apps"
      - table: "line_items"
      - table: "media_creatives"
      - table: "preroll_call_to_actions"
      - table: "promoted_accounts"
      - table: "promoted_tweets"
      - table: "scheduled_promoted_tweets"
      - table: "tailored_audiences"
      - table: "targeting_criteria"
      - table: "tweets"

  - id: "account-media-id"
    table: "account_media"
    attribute: "account_media_id"
    all-foreign-keys:
      - table: "media_creatives"
      - table: "account_media"
        join-on: "id"

  - id: "ad-group-id"
    table: "line_items"
    attribute: "line_item_id"
    all-foreign-keys:
      - table: "line_item_apps"
      - table: "media_creatives"
      - table: "preroll_call_to_actions"
      - table: "promoted_accounts"
      - table: "promoted_tweets"
      - table: "scheduled_promoted_tweets"
      - table: "targeting_criteria"

  - id: "campaign-id"
    table: "campaigns"
    attribute: "campaign_id"
    all-foreign-keys:
      - table: "campaigns"
        join-on: "id"
      - table: "line_items"

  - id: "funding-instrument-id"
    table: "funding_instruments"
    attribute: "funding_instrument_id"
    all-foreign-keys:
      - table: "account_media"
      - table: "campaigns"
      - table: "funding_instruments"
        join-on: "id"

  - id: "iab-category-id"
    table: "iab_categories"
    attribute: "value"
    all-foreign-keys:
      - table: "advertiser_business_categories"
        subattribute: "iab_categories"
      - table: "content_categories"
        subattribute: "iab_categories"
      - table: "iab_categories"
        join-on: "id"

  - id: "line-item-app-id"
    table: "line_item_apps"
    attribute: "line_item_app_id"
    all-foreign-keys:
      - table: "line_item_apps"

  - id: "tweet-id"
    table: "tweets"
    attribute: "tweet_id"
    all-foreign-keys:
      - table: "promoted_tweets"
      - table: "scheduled_promoted_tweets"
      - table: "tweets"

  - id: "user-id"
    table: ""
    attribute: "user_id"
    all-foreign-keys:
      - table: "cards_image_direct_message"
        join-on: "recipient_user_id"
      - table: "cards_video_direct_message"
        join-on: "recipient_user_id"
      - table: "promotable_users"
      - table: "promoted_accounts"
      - table: "tweets"
        subattribute: "entities.user_mentions"
        join-on: "id"
      - table: "tweets"
        join-on: "in_reply_to_user_id"
      - table: "tweets"
        subattribute: "users"
        join-on: "id"

  - id: "video-owner-id"
    table: ""
    attribute: "video_owner_id"
    all-foreign-keys:
      - table: "cards_video_app_download"
      - table: "cards_video_conversation"
      - table: "cards_video_direct_message"
      - table: "cards_video_website"
---