---
tap: "twitter-ads"
version: "1"
key: "promoted-account"

name: "promoted_accounts"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/promoted-accounts#promoted-accounts"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/promoted_accounts.json"
description: |
  The `{{ table.name }}` table contains info about the promoted accounts associated with line items (ad groups) associated with an account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get promoted accounts"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/promoted-accounts#promoted-accounts"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "promoted-account-id"

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

  - name: "user_id"
    type: "string"
    description: ""
    foreign-key-id: "user-id"
---