---
tap: "taboola"
# version: 

name: "campaign_performance"
doc-link: https://github.com/taboola/Backstage-API/blob/master/Backstage%20API%20-%20Reports.pdf
singer-schema: https://github.com/singer-io/tap-taboola/blob/master/tap_taboola/schemas.py#L117
description: |
  The `campaign_performance` table contains performance data for the campaigns in your Taboola account, broken down by day.

replication-method: "Key-based Incremental"
api-method:
  name: 
  doc-link: 

attributes:
  - name: "campaign_id"
    type: "integer"
    primary-key: true
    #  foreign-keys:
    #    - table: "campaigns"
    #    - attribute: "id"
    description: "The campaign ID."

  - name: "date"
    type: "date"
    primary-key: true
    replication-key: true
    description: "The start date of the campaign."

  - name: "impressions"
    type: "integer"
    description: "The total number of impressions for the campaign for this date.."

  - name: "ctr"
    type: "number"
    description: " for this date, calculated as `(clicks/impressions)`"

  - name: "clicks"
    type: "integer"
    description: "The total number of clicks for the campaign for this date."

  - name: "cpc"
    type: "number"
    description: "The cost per click for the campaign for this date, calculated as `(spend/clicks)`"

  - name: "cpm"
    type: "number"
    description: "The cost per 1000 impressions for the campaign for this date, calculated as `(spend/impressions)`"

  - name: "cpa_conversion_rate"
    type: "number"
    description: "The conversion rate for the campaign for this date, calculated as `(actions/clicks)`"

  - name: "cpa_actions_num"
    type: "integer"
    description: "The total actions (conversions) for the campaign for this date."

  - name: "cpa"
    type: "number"
    description: "The for the campaign for this date, calculated as `(spend/actions`"

  - name: "spent"
    type: "number"
    description: "The total amount spent for the campaign for this date."

  - name: "currency"
    type: "string"
    description: "The ISO4217 currency code for columns containing monetary data."
---