---
tap: "twitter-ads"
version: "1"
key: "card-website"

name: "cards_website"
doc-link: "https://developer.twitter.com/en/docs/ads/creatives/api-reference/website#website-cards"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/cards_website.json"
description: |
  The `{{ table.name }}` table contains info about the website cards associated with an account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get website cards for an account"
  doc-link: "https://developer.twitter.com/en/docs/ads/creatives/api-reference/website#website-cards"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "card-website-id"

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

  - name: "website_dest_url"
    type: "string"
    description: ""

  - name: "website_display_url"
    type: "string"
    description: ""

  - name: "website_shortened_url"
    type: "string"
    description: ""

  - name: "website_title"
    type: "string"
    description: ""

  - name: "website_url"
    type: "string"
    description: ""
---