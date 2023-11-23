---
tap: "twitter-ads"
version: "1"
key: "targeting-network-operator"

name: "targeting_network_operators"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get-targeting-criteria-network-operators"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/targeting_network_operators.json"
description: |
  The `{{ table.name }}` table contains info about network operator-based targeting criteria for Promoted Products.

replication-method: "Full Table"

api-method:
  name: "Get network operator targeting criteria"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get-targeting-criteria-network-operators"

attributes:
  - name: "targeting_value"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "targeting-network-operator-id"

  - name: "country_code"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "targeting_type"
    type: "string"
    description: ""
---