---
tap: "twitter-ads"
version: "1"
key: "targeting-language"

name: "targeting_languages"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get-targeting-criteria-languages"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/targeting_languages.json"
description: |
  The `{{ table.name }}` table contains info about the language-based targeting criteria for Promoted Products.

replication-method: "Full Table"

api-method:
  name: "Get language targeting criteria"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get-targeting-criteria-languages"

attributes:
  - name: "targeting_value"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "targeting-language-id"

  - name: "name"
    type: "string"
    description: ""

  - name: "targeting_type"
    type: "string"
    description: ""
---