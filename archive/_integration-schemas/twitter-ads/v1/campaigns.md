---
tap: "twitter-ads"
version: "1"
key: "campaign"

name: "campaigns"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/campaigns#campaigns"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/campaigns.json"
description: |
  The `{{ table.name }}` table contains info about the campaigns associated with an account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get campaigns for an account"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/campaigns#campaigns"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "campaign-id"

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