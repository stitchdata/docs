---
tap: "twitter-ads"
version: "1"
key: "line-item-app"

name: "line_item_apps"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/line-item-apps#line-item-apps"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/line_item_apps.json"
description: |
  The `{{ table.name }}` table contains info about the apps associated with line items associated with an account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get line item apps for an account"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/line-item-apps#line-item-apps"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "line-item-app-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "account_id"
    type: "string"
    description: ""
    foreign-key-id: "account-id"

  - name: "app_store_identifier"
    type: "string"
    description: ""

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

  - name: "os_type"
    type: "string"
    description: ""
---