---
tap: "twitter-ads"
version: "1"
key: "advertiser-business-category"

name: "advertiser_business_categories"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/advertiser-business-categories#advertiser-business-categories"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/advertiser_business_categories.json"
description: |
  The `{{ table.name }}` table contains info about the advertiser business categories associated with an advertiser's ad groups.

replication-method: "Full Table"

api-method:
  name: "Get advertiser business categories for an account"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/advertiser-business-categories#advertiser-business-categories"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "advertiser-business-category-id"

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