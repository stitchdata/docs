---
tap: "twitter-ads"
version: "1"
key: "scheduled-promoted-tweet"

name: "scheduled_promoted_tweets"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/scheduled-promoted-tweets#scheduled-promoted-tweets"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/scheduled_promoted_tweets.json"
description: |
  The `{{ table.name }}` table contains info about the scheduled promoted Tweets associated with an account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get scheduled promoted Tweets"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/scheduled-promoted-tweets#scheduled-promoted-tweets"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "scheduled-promoted-tweet-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "account_id"
    type: "string"
    description: ""
    foreign-key-id: "account-id"

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "line_item_id"
    type: "string"
    description: ""
    foreign-key-id: "ad-group-id"

  - name: "scheduled_tweet_id"
    type: "string"
    description: ""
    # foreign-key-id: "scheduled-tweet-id"

  - name: "tweet_id"
    type: "string"
    description: ""
    foreign-key-id: "tweet-id"
---