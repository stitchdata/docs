---
tap: "snapchat-ads"
version: "1"
key: ""

name: "campaigns"
doc-link: https://developers.snapchat.com/api/docs/#get-all-campaigns
singer-schema: https://github.com/singer-io/tap-snapchat-ads/tree/master/tap_snapchat_ads/schemas/campaigns.json
description: "This stream retrieves all campaigns within a specified ad account"

replication-method: "Key-based Incremental"

table-key-properties: "id"
valid-replication-keys: "updated_at"

attributes:
  - name: "ad_account_id"
    type: "string"
    description: "Ad Account ID"

  - name: "buy_model"
    type: "string"
    description: "Buy Model. Example: AUCTION(default), RESERVED"

  - name: "created_at"
    type: "date-time"
    description: "Date of creation"

  - name: "daily_budget_micro"
    type: "integer"
    description: "Daily Spend Cap (micro-currency)"

  - name: "end_time"
    type: "date-time"
    description: "End time of the Campaign"

  - name: "id"
    primary-key: true
    type: "string"
    description: "Campaign ID"

  - name: "lifetime_spend_cap_micro"
    type: "integer"
    description: "Lifetime spend cap for the campaign (microcurrency)"

  - name: "measurement_spec"
    type: "object"
    description: "The apps to be tracked for this campaign"
    subattributes:

  - name: "name"
    type: "string"
    description: "Campaign name"

  - name: "objective"
    type: "string"
    description: "Objective of the Campaign. Default: BRAND_AWARENESS"

  - name: "regulations"
    type: "object"
    description: "Required for Campaigns that run Ads for Credit, Housing, Employment (CHE)"
    subattributes:

  - name: "start_time"
    type: "date-time"
    description: "Start Time of Campaign"

  - name: "status"
    type: "string"
    description: "Campaign status"

  - name: "updated_at"
    type: "date-time"
    description: "Date of last updated"
    replication-key: true
---