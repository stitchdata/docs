---
tap: "twitter-ads"
version: "1"
key: "card-poll"

name: "cards_poll"
doc-link: "https://developer.twitter.com/en/docs/ads/creatives/api-reference/poll#poll-cards"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/cards_poll.json"
description: |
  The `{{ table.name }}` table contains info about poll cards associated with an account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get poll cards for an account"
  doc-link: "https://developer.twitter.com/en/docs/ads/creatives/api-reference/poll#poll-cards"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "card-poll-id"

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

  - name: "content_duration_seconds"
    type: "integer"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "duration_in_minutes"
    type: "integer"
    description: ""

  - name: "end_time"
    type: "date-time"
    description: ""

  - name: "first_choice"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "second_choice"
    type: "string"
    description: ""

  - name: "start_time"
    type: "date-time"
    description: ""

  - name: "video_height"
    type: "integer"
    description: ""

  - name: "video_hls_url"
    type: "string"
    description: ""

  - name: "video_poster_height"
    type: "integer"
    description: ""

  - name: "video_poster_url"
    type: "string"
    description: ""

  - name: "video_poster_width"
    type: "integer"
    description: ""

  - name: "video_url"
    type: "string"
    description: ""

  - name: "video_width"
    type: "integer"
    description: ""
---