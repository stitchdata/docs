---
tap: "twitter-ads"
version: "1"
key: "targeting-interest"

name: "targeting_interests"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get-targeting-criteria-interests"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/targeting_interests.json"
description: |
  The `{{ table.name }}` table contains info about the interest-based targeting criteria for Promoted Products.

replication-method: "Full Table"

api-method:
  name: "Get interest targeting criteria"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get-targeting-criteria-interests"

attributes:
  - name: "targeting_value"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "targeting-interest-id"

  - name: "name"
    type: "string"
    description: ""

  - name: "targeting_type"
    type: "string"
    description: ""
---