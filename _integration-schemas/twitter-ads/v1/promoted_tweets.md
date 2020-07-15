---
tap: "twitter-ads"
version: "1"
key: "promoted-tweet"

name: "promoted_tweets"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/promoted-tweets#promoted-tweets"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/promoted_tweets.json"
description: |
  The `{{ table.name }}` table contains info about references to Tweets associated with line items (ad groups) associated with an account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get promoted tweets"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/promoted-tweets#promoted-tweets"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "promoted-tweet-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "account_id"
    type: "string"
    description: ""
    foreign-key-id: "account-id"

  - name: "approval_status"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "entity_status"
    type: "string"
    description: ""

  - name: "line_item_id"
    type: "string"
    description: ""
    foreign-key-id: "ad-group-id"

  - name: "tweet_id"
    type: "string"
    description: ""
    foreign-key-id: "tweet-id"
---