---
tap: "twitter-ads"
version: "1"
key: "promotable-user"

name: "promotable_users"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/promotable-users#promotable-users"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/promotable_users.json"
description: |
  The `{{ table.name }}` table contains info about the promotable users associated with an account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get promotable users for an account"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/promotable-users#promotable-users"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "promotable-user-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "promotable_user_type"
    type: "string"
    description: ""

  - name: "user_id"
    type: "string"
    description: ""
    foreign-key-id: "user-id"
---