---
tap: "twitter-ads"
version: "1"
key: "targeting-location"

name: "targeting_locations"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get-targeting-criteria-locations"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/targeting_locations.json"
description: |
  The `{{ table.name }}` table contains info about location-based targeting criteria for Promoted Products. According to {{ integration.display_name }}'s documentation, geo-targeting is available for Promoted Accounts and Tweets at the country, state/region, city, and postal code levels.

replication-method: "Full Table"

api-method:
  name: "Get targeting location criteria"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get-targeting-criteria-locations"

attributes:
  - name: "targeting_value"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "targeting-location-id"

  - name: "country_code"
    type: "string"
    description: ""

  - name: "location_type"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "targeting_type"
    type: "string"
    description: ""
---