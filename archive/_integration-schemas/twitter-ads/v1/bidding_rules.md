---
tap: "twitter-ads"
version: "1"
key: "bidding-rule"

name: "bidding_rules"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/bidding-rules#bidding-rules"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/bidding_rules.json"
description: |
  The `{{ table.name }}` table contains info about the bidding rules for currencies.

replication-method: "Full Table"

api-method:
  name: "Get bidding rules"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/bidding-rules#bidding-rules"

attributes:
  - name: "currency"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "currency-id"

  - name: "maximum_cpe_bid_local_micro"
    type: "integer"
    description: ""

  - name: "minimum_cpe_bid_local_micro"
    type: "integer"
    description: ""

  - name: "minimum_denomination"
    type: "integer"
    description: ""
---