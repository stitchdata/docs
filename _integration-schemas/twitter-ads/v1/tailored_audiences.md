---
tap: "twitter-ads"
version: "1"
key: "tailored-audience"

name: "tailored_audiences"
doc-link: "https://developer.twitter.com/en/docs/ads/audiences/api-reference/tailored-audiences#tailored-audiences"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/tailored_audiences.json"
description: |
  The `{{ table.name }}` table contains info about the Tailored Audiences associated with an account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get Tailored Audiences"
  doc-link: "https://developer.twitter.com/en/docs/ads/audiences/api-reference/tailored-audiences#tailored-audiences"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "tailored-audience-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "account_id"
    type: "string"
    description: ""
    foreign-key-id: "account-id"

  - name: "audience_size"
    type: "integer"
    description: ""

  - name: "audience_type"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "is_owner"
    type: "boolean"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "partner_source"
    type: "string"
    description: ""

  - name: "permission_level"
    type: "string"
    description: ""

  - name: "reasons_not_targetable"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "targetable"
    type: "boolean"
    description: ""

  - name: "targetable_types"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
---