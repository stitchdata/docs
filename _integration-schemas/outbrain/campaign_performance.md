---
tap: "outbrain"
version: "1.0"

name: "campaign_performance"
doc-link: http://docs.amplifyv01.apiary.io/#reference/performance-reporting/campaigns
singer-schema: https://github.com/singer-io/tap-outbrain/blob/master/tap_outbrain/schemas.py#L218
description: |
  The `{{ table.name }}` table contains performance metrics for your {{ integration.display_name }} campaigns.

replication-method: "Key-based Incremental"
api-method:
  name: retrieveCampaignsWithPerformanceStatisticsForAMarketer
  doc-link: http://docs.amplifyv01.apiary.io/#reference/performance-reporting/campaigns/retrieve-campaigns-with-performance-statistics-for-a-marketer

attributes:
  - name: "campaignId"
    type: "string"
    primary-key: true
    description: "The campaign ID plus the start date (day)."

  - name: "fromDate"
    type: "date"
    primary-key: true
    replication-key: true
    description: "The start date."

  - name: "impressions"
    type: "number"
    description: "The total number of PromotedLinks impressions for the campaign."

  - name: "clicks"
    type: "number"
    description: "The total number of PromotedLinks clicks for the campaign."

  - name: "ctr"
    type: "number"
    description: "The average click through rate percentage for the campaign. Calculated as `(clicks / impressions)/100`"

  - name: "spend"
    type: "number"
    description: "The total amount of money spent for the campaign."

  - name: "ecpc"
    type: "number"
    description: "The effective (calculated) average CPC (Cost Per Click) for the campaign. Calculated as `(spend / clicks)`"

  - name: "conversions"
    type: "number"
    description: "The total number of conversions for the campaign."

  - name: "conversionRate"
    type: "number"
    description: "The average rate of conversions per click percentage for the campaign. Calculated as `(conversions / clicks)/100`"

  - name: "cpa"
    type: "number"
    description: "The average CPA (Cost Per Acquisition) for the campaign. Calculated as `(spend / conversions)`"
---