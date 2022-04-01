---
tap: "google-ads"
version: "1"
name: "accessible_bidding_strategies"
doc-link: https://developers.google.com/google-ads/api/reference/rpc/v10/AccessibleBiddingStrategy
description: |
  The `{{ table.name }}` table contains info about accessible bidding strategies in your Google Ads account.

  [This is a **Core Object** table](#replication).

replication-method: "Full Table"
attribution-window: true

attributes:
  - name: "customer_id"
    type: "integer"
    description: ""
  - name: "id"
    type: "integer"
    description: ""
    primary-key: true
  - name: "maximize_conversion_value"
    type: "object"
    description: ""
    subattributes:
      - name: "target_roas"
        type: "singer.decimal"
        description: ""
  - name: "maximize_conversions"
    type: "object"
    description: ""
    subattributes:
      - name: "target_cpa"
        type: "integer"
        description: ""
  - name: "name"
    type: "string"
    description: ""
  - name: "owner_customer_id"
    type: "integer"
    description: ""
  - name: "owner_descriptive_name"
    type: "string"
    description: ""
  - name: "resource_name"
    type: "object, string"
    description: ""
  - name: "target_cpa"
    type: "object"
    description: ""
    subattributes:
      - name: "target_cpa_micros"
        type: "integer"
        description: ""
  - name: "target_impression_share"
    type: "object"
    description: ""
    subattributes:
      - name: "cpc_bid_ceiling_micros"
        type: "integer"
        description: ""
      - name: "location"
        type: "string"
        description: ""
      - name: "location_fraction_micros"
        type: "integer"
        description: ""
  - name: "target_roas"
    type: "object"
    description: ""
    subattributes:
      - name: "target_roas"
        type: "singer.decimal"
        description: ""
  - name: "target_spend"
    type: "object"
    description: ""
    subattributes:
      - name: "cpc_bid_ceiling_micros"
        type: "integer"
        description: ""
      - name: "target_spend_micros"
        type: "integer"
        description: ""
  - name: "type"
    type: "string"
    description: ""
---
