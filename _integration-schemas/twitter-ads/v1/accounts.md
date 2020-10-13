---
tap: "twitter-ads"
version: "1"
key: "account"

name: "accounts"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/accounts#accounts"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/accounts.json"
description: |
  The `{{ table.name }}` table contains info about the advertising-enabled accounts the user authenticating the integration has access to.

replication-method: "Key-based Incremental"

api-method:
  name: "Get accounts"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/accounts#accounts"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "account-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "approval_status"
    type: "string"
    description: ""

  - name: "business_id"
    type: "string"
    description: ""
    # foreign-key-id: "business-id"

  - name: "business_name"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "industry_type"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "salt"
    type: "string"
    description: ""

  - name: "timezone"
    type: "string"
    description: ""

  - name: "timezone_switch_at"
    type: "date-time"
    description: ""
---