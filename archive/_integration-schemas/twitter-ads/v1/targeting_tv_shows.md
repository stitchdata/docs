---
tap: "twitter-ads"
version: "1"
key: "targeting-tv-show"

name: "targeting_tv_shows"
doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get-targeting-criteria-tv-shows"
singer-schema: "https://github.com/singer-io/tap-twitter-ads/blob/master/tap_twitter_ads/schemas/targeting_tv_shows.json"
description: |
  The `{{ table.name }}` table contains info about TV-show based targeting criteria for Promoted Products.

replication-method: "Full Table"

api-method:
  name: "Get TV show targeting criteria for a TV market"
  doc-link: "https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get-targeting-criteria-tv-shows"

attributes:
  - name: "targeting_value"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "targeting-tv-show-id"

  - name: "genre"
    type: "string"
    description: ""

  - name: "locales"
    type: "array"
    description: |
      The TV market locales the TV show is associated with. Use these values to join records from this table to the [`targeting_tv_markets`](#targeting_tv_markets) table.

      In the format `language-country`, these values will match the `targeting_tv_markets.locale` column. For example: If `language: en` and `country: US`, construct a the values as `language-country`, or `en-US` in this case, to join to the `targeting_tv_markets` table where `locale: en-US`.
    subattributes:
      - name: "country"
        type: "string"
        description: ""

      - name: "language"
        type: "string"
        description: ""

  - name: "name"
    type: "string"
    description: ""
---