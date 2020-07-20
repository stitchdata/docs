---
tap: "twitter-ads"
version: "1"
key: "preroll-call-to-action"

name: "preroll_call_to_actions"
doc-link: "https://developer.twitter.com/en/docs/ads/creatives/api-reference/preroll-call-to-actions#preroll-call-to-actions"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/preroll_call_to_actions.json"
description: |
  The `{{ table.name }}` table contains info about the preroll call-to-actions associated with line items (ad groups) associated with an account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get preroll call to actions for an account"
  doc-link: "https://developer.twitter.com/en/docs/ads/creatives/api-reference/preroll-call-to-actions#preroll-call-to-actions"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "preroll-call-to-action-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "account_id"
    type: "string"
    description: ""
    foreign-key-id: "account-id"

  - name: "call_to_action"
    type: "string"
    description: ""

  - name: "call_to_action_url"
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
---