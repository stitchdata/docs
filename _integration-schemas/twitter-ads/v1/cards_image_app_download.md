---
tap: "twitter-ads"
version: "1"
key: "card-image-app-download"

name: "cards_image_app_download"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/cards_image_app_download.json"
description: |
  The `{{ table.name }}` table contains info about image app download cards associated with an account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get image app download cards for an account"
  doc-link: "https://developer.twitter.com/en/docs/ads/creatives/api-reference/image-app-download#image-app-download-cards"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "card-image-app-download-id"

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
---