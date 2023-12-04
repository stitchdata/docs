---
tap: "twitter-ads"
version: "1"
key: "card-video-conversation"

name: "cards_video_conversation"
doc-link: "https://developer.twitter.com/en/docs/ads/creatives/api-reference/video-conversation#video-conversation-cards"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/cards_video_conversation.json"
description: |
  The `{{ table.name }}` table contains info about the video conversation cards associated with an account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get video conversation cards for an account"
  doc-link: "https://developer.twitter.com/en/docs/ads/creatives/api-reference/video-conversation#video-conversation-cards"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "card-video-conversation-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "account_id"
    type: "string"
    description: ""
    foreign-key-id: "account-id"

  - name: "card_type"
    type: "string"
    description: ""

  - name: "card_uri"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "first_cta"
    type: "string"
    description: ""

  - name: "first_cta_tweet"
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

  - name: "thank_you_text"
    type: "string"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "video_height"
    type: "integer"
    description: ""

  - name: "video_owner_id"
    type: "string"
    description: ""
    foreign-key-id: "video-owner-id"

  - name: "video_width"
    type: "integer"
    description: ""
---