---
tap: "twitter-ads"
version: "1"
key: "targeting-platform"

name: "targeting_platforms"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get-targeting-criteria-platforms"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/targeting_platforms.json"
description: |
  The `{{ table.name }}` table contains info about platform-based targeting criteria for Promoted Products.

replication-method: "Full Table"

api-method:
  name: "Get platform targeting criteria"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get-targeting-criteria-platforms"

attributes:
  - name: "targeting_value"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "targeting-platform-id"

  - name: "name"
    type: "string"
    description: ""

  - name: "targeting_type"
    type: "string"
    description: ""
---