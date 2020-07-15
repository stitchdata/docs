---
tap: "twitter-ads"
version: "1"
key: "targeting-tv-market"

name: "targeting_tv_markets"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get-targeting-criteria-tv-markets"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/targeting_tv_markets.json"
description: |
  The `{{ table.name }}` table contains info about TV markets where TV shows can be targeted. Use the [`targeting_tv_shows`](#targeting_tv_shows) table for info about individual TV shows.

replication-method: "Full Table"

api-method:
  name: "Get TV market targeting criteria"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get-targeting-criteria-tv-markets"

attributes:
  - name: "locale"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "locale-id"

  - name: "country_code"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""
---