---
tap: "twitter-ads"
version: "1"
key: "targeting-app-store-category"

name: "targeting_app_store_categories"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get-targeting-criteria-conversations"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/targeting_app_store_categories.json"
description: |
  The `{{ table.name }}` table contains info about the app store targeting categories associated with promoted products.

replication-method: "Full Table"

api-method:
  name: "Get app store categories"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get-targeting-criteria-conversations"

attributes:
  - name: "targeting_value"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "targeting-app-store-category-id"

  - name: "name"
    type: "string"
    description: ""

  - name: "os_type"
    type: "string"
    description: ""

  - name: "targeting_type"
    type: "string"
    description: ""
---