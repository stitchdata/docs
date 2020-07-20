---
tap: "twitter-ads"
version: "1"
key: "line-item"

name: "line_items"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/line-items#line-items"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/line_items.json"
description: |
  The `{{ table.name }}` table contains info about the line items (ad groups) associated with an account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get line items for an account"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/line-items#line-items"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "ad-group-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "account_id"
    type: "string"
    description: ""
    foreign-key-id: "account-id"

  - name: "advertiser_domain"
    type: "string"
    description: ""

  - name: "advertiser_user_id"
    type: "integer"
    description: ""
    # foreign-key-id: "advertiser-user-id"

  - name: "automatically_select_bid"
    type: "boolean"
    description: ""

  - name: "bid_amount_local_micro"
    type: "integer"
    description: ""

  - name: "bid_type"
    type: "string"
    description: ""

  - name: "bid_unit"
    type: "string"
    description: ""

  - name: "campaign_id"
    type: "string"
    description: ""
    foreign-key-id: "campaign-id"

  - name: "categories"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "charge_by"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "creative_source"
    type: "string"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "end_time"
    type: "date-time"
    description: ""

  - name: "entity_status"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "objective"
    type: "string"
    description: ""

  - name: "optimization"
    type: "string"
    description: ""

  - name: "placements"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "primary_web_event_tag"
    type: "string"
    description: ""

  - name: "product_type"
    type: "string"
    description: ""

  - name: "start_time"
    type: "date-time"
    description: ""

  - name: "target_cpa_local_micro"
    type: "integer"
    description: ""

  - name: "total_budget_amount_local_micro"
    type: "integer"
    description: ""

  - name: "tracking_tags"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
---