---
tap: "twitter-ads"
version: "1"
key: "content-category"

name: "content_categories"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/content-categories#content-categories"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/content_categories.json"
description: |
  The `{{ table.name }}` table contains info about the content categories used as targeting criteria for ad groups.

replication-method: "Full Table"

api-method:
  name: "Get content categories"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/content-categories#content-categories"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "content-category-id"

  - name: "iab_categories"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
        foreign-key-id: "iab-category-id"

  - name: "name"
    type: "string"
    description: ""
---