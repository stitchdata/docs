---
tap: "twitter-ads"
version: "1"
key: "targeting-platform-version"

name: "targeting_platform_versions"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get-targeting-criteria-platform-versions"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/targeting_platform_versions.json"
description: |
  The `{{ table.name }}` table contains info about mobile OS-version based targeting criteria for Promoted Products.

replication-method: "Full Table"

api-method:
  name: "Get platform version targeting criteria"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get-targeting-criteria-platform-versions"

attributes:
  - name: "targeting_value"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "targeting-platform-version-id"

  - name: "name"
    type: "string"
    description: ""

  - name: "number"
    type: "string"
    description: ""

  - name: "os_type"
    type: "string"
    description: ""

  - name: "targeting_type"
    type: "string"
    description: ""
---