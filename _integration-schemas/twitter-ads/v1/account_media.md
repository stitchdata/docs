---
tap: "twitter-ads"
version: "1"
key: "account-media"

name: "account_media"
doc-link: "https://developer.twitter.com/en/docs/ads/creatives/api-reference/account-media#account-media"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/account_media.json"
description: |
  The `{{ table.name }}` table contains info about the account media associated with an account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get account media for an account"
  doc-link: "https://developer.twitter.com/en/docs/ads/creatives/api-reference/account-media#account-media"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "account-media-id"

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

  - name: "currency"
    type: "string"
    description: ""

  - name: "daily_budget_amount_local_micro"
    type: "integer"
    description: ""

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "duration_in_days"
    type: "integer"
    description: ""

  - name: "end_time"
    type: "date-time"
    description: ""

  - name: "entity_status"
    type: "string"
    description: ""

  - name: "frequency_cap"
    type: "integer"
    description: ""

  - name: "funding_instrument_id"
    type: "string"
    description: ""
    foreign-key-id: "funding-instrument-id"

  - name: "name"
    type: "string"
    description: ""

  - name: "reasons_not_servable"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "servable"
    type: "boolean"
    description: ""

  - name: "standard_delivery"
    type: "boolean"
    description: ""

  - name: "start_time"
    type: "date-time"
    description: ""

  - name: "total_budget_amount_local_micro"
    type: "integer"
    description: ""
---