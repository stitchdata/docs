---
tap: "twitter-ads"
version: "1"
key: "media-creative"

name: "media_creatives"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/media-creatives#media-creatives"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/media_creatives.json"
description: |
  The `{{ table.name }}` table contains info about the media creatives associated with an account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get media creatives for an account"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/media-creatives#media-creatives"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "media-creative-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "account_id"
    type: "string"
    description: ""
    foreign-key-id: "account-id"

  - name: "account_media_id"
    type: "string"
    description: ""
    foreign-key-id: "account-media-id"

  - name: "approval_status"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "landing_url"
    type: "string"
    description: ""

  - name: "line_item_id"
    type: "string"
    description: ""
    foreign-key-id: "ad-group-id"

  - name: "serving_status"
    type: "string"
    description: ""
---