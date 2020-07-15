---
tap: "twitter-ads"
version: "1"
key: "card-video-app-download"

name: "cards_video_app_download"
doc-link: "https://developer.twitter.com/en/docs/ads/creatives/api-reference/video-app-download#video-app-download-cards"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/cards_video_app_download.json"
description: |
  The `{{ table.name }}` table contains info about the video app download cards associated with an account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get video app download cards for an account"
  doc-link: "https://developer.twitter.com/en/docs/ads/creatives/api-reference/video-app-download#video-app-download-cards"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "card-video-app-download-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "account_id"
    type: "string"
    description: ""
    foreign-key-id: "account-id"

  - name: "app_cta"
    type: "string"
    description: ""

  - name: "card_type"
    type: "string"
    description: ""

  - name: "card_uri"
    type: "string"
    description: ""

  - name: "country_code"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "google_play_app_id"
    type: "string"
    description: ""

  - name: "media_key"
    type: "string"
    description: ""

  - name: "media_url"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "poster_media_url"
    type: "string"
    description: ""

  - name: "video_owner_id"
    type: "string"
    description: ""
    foreign-key-id: "video-owner-id"
---