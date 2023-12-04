---
tap: "twitter-ads"
version: "1"
key: "iab-category"

name: "iab_categories"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/iab-categories#iab-categories"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/iab_categories.json"
description: |
  The `{{ table.name }}` table contains info about the app categories associated with ad groups.

replication-method: "Full Table"

api-method:
  name: "Get IAB categories"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/iab-categories#iab-categories"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "iab-category-id"

  - name: "name"
    type: "string"
    description: ""

  - name: "parent_id"
    type: "string"
    description: ""
---