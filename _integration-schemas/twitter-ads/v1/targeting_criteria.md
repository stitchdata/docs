---
tap: "twitter-ads"
version: "1"
key: "targeting-criteria"

name: "targeting_criteria"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-criteria#targeting-criteria"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/targeting_criteria.json"
description: |
  The `{{ table.name }}` table contains info about the targeting criteria associated with an account.

replication-method: "Full Table"

api-method:
  name: "Get targeting criteria for an account"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-criteria#targeting-criteria"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "targeting-criteria-id"

  - name: "line_item_id"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "ad-group-id"

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

  - name: "name"
    type: "string"
    description: ""

  - name: "operator_type"
    type: "string"
    description: ""

  - name: "tailored_audience_expansion"
    type: "boolean"
    description: ""

  - name: "tailored_audience_type"
    type: "string"
    description: ""

  - name: "targeting_type"
    type: "string"
    description: ""

  - name: "targeting_value"
    type: "string"
    description: ""

  - name: "updated_at"
    type: "date-time"
    description: ""
---