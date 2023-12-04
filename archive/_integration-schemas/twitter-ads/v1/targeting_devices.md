---
tap: "twitter-ads"
version: "1"
key: "targeting-device"

name: "targeting_devices"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get-targeting-criteria-devices"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/targeting_devices.json"
description: |
  The `{{ table.name }}` table contains info about the device-based targeting criteria for Promoted Products.

replication-method: "Full Table"

api-method:
  name: "Get targeting device criteria"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get-targeting-criteria-devices"

attributes:
  - name: "targeting_value"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "targeting-device-id"

  - name: "manufacturer"
    type: "string"
    description: ""

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