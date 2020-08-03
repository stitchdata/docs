---
tap: "twitter-ads"
version: "1"
key: "card-image-conversation"

name: "cards_image_conversation"
doc-link: "https://developer.twitter.com/en/docs/ads/creatives/api-reference/image-conversation#image-conversation-cards"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/cards_image_conversation.json"
description: |
  The `{{ table.name }}` table contains info about image conversation cards associated with an account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get image conversation cards for an account"
  doc-link: "https://developer.twitter.com/en/docs/ads/creatives/api-reference/image-conversation#image-conversation-cards"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "card-image-conversation-id"

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

  - name: "image_display_height"
    type: "integer"
    description: ""

  - name: "image_display_width"
    type: "integer"
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

  - name: "thank_you_text"
    type: "string"
    description: ""

  - name: "title"
    type: "string"
    description: ""
---