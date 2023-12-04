---
tap: "impact"
version: "1"
key: "click"

name: "clicks"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/clicks.json"
description: |
  The `{{ table.name }}` table contains info about a campaign's clicks.

replication-method: "Key-based Incremental"

api-method:
  name: "Get clicks"
  doc-link: "https://developer.impact.com/default#operations-Clicks-GetClicks"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "click-id"

  - name: "event_date"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "ad_campaign"
    type: "string"
    description: ""

  - name: "ad_group"
    type: "string"
    description: ""

  - name: "ad_id"
    type: "integer"
    description: ""
    foreign-key-id: "ad-id"

  - name: "ad_name"
    type: "string"
    description: ""

  - name: "ad_type"
    type: "string"
    description: ""

  - name: "bid_keyword"
    type: "string"
    description: ""

  - name: "browser"
    type: "string"
    description: ""

  - name: "campaign_id"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-id"

  - name: "campaign_name"
    type: "string"
    description: ""

  - name: "channel"
    type: "string"
    description: ""

  - name: "cpc_bid"
    type: "number"
    description: ""

  - name: "customer_area"
    type: "string"
    description: ""

  - name: "customer_city"
    type: "string"
    description: ""

  - name: "customer_country"
    type: "string"
    description: ""

  - name: "customer_region"
    type: "string"
    description: ""

  - name: "deal_name"
    type: "string"
    description: ""

  - name: "deal_scope"
    type: "string"
    description: ""

  - name: "deal_type"
    type: "string"
    description: ""

  - name: "device_family"
    type: "string"
    description: ""

  - name: "device_type"
    type: "string"
    description: ""

  - name: "ip_address"
    type: "string"
    description: ""

  - name: "keyword"
    type: "string"
    description: ""

  - name: "landing_page_url"
    type: "string"
    description: ""

  - name: "match_type"
    type: "string"
    description: ""

  - name: "media_id"
    type: "integer"
    description: ""
    foreign-key-id: "media-id"

  - name: "media_name"
    type: "string"
    description: ""

  - name: "os"
    type: "string"
    description: ""

  - name: "payout"
    type: "number"
    description: ""

  - name: "product_sku"
    type: "string"
    description: ""

  - name: "profile_id"
    type: "string"
    description: ""

  - name: "referring_domain"
    type: "string"
    description: ""

  - name: "referring_url"
    type: "string"
    description: ""

  - name: "search_text"
    type: "string"
    description: ""

  - name: "shared_id"
    type: "string"
    description: ""

  - name: "traffic_category"
    type: "string"
    description: ""

  - name: "traffic_source"
    type: "string"
    description: ""

  - name: "unique_click"
    type: "boolean"
    description: ""
---