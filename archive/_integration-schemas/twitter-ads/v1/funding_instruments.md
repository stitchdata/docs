---
tap: "twitter-ads"
version: "1"
key: "funding-instrument"

name: "funding_instruments"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/funding-instruments#funding-instruments"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/funding_instruments.json"
description: |
  The `{{ table.name }}` table contains info about the funding instruments associated with an account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get funding instruments for an account"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/funding-instruments#funding-instruments"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "funding-instrument-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "able_to_fund"
    type: "boolean"
    description: ""

  - name: "account_id"
    type: "string"
    description: ""
    foreign-key-id: "account-id"

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "credit_limit_local_micro"
    type: "integer"
    description: ""

  - name: "credit_remaining_local_micro"
    type: "integer"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "end_time"
    type: "date-time"
    description: ""

  - name: "entity_status"
    type: "string"
    description: ""

  - name: "funded_amount_local_micro"
    type: "integer"
    description: ""

  - name: "io_header"
    type: "string"
    description: ""

  - name: "reasons_not_able_to_fund"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "start_time"
    type: "date-time"
    description: ""

  - name: "type"
    type: "string"
    description: ""
---