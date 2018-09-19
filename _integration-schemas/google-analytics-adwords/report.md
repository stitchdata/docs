---
tap: "google-analytics-adwords"
version: "05-12-2017"

name: "report"
doc-link: 
description: |
  The `report` table contains info about your active campaigns and the ads contained within those campaigns.

  **Note**: The attributes in this table are dependent upon the [Metrics and Dimensions selected during setup](#choose-your-data). The schema shown below uses the Metrics and Dimensions from an older version of Stitch's Google AdWords integration.

  #### Table Rows and Data Pagination

  Google AdWords data is paginated on a daily basis. This means a single row in the table pertains to a specific day. The `start_date` and `end_date` columns, which will contain identical values, indicate the day the row is for.

  For example: If `start_date` and `end_date` contain the value `2017-12-12 00:00:00`, the row contains data for December 12, 2017.

replication-method: "Key-based Incremental"
attribution-window: true

attributes:
## Primary Key
  - name: "adContent"
    type: "dimension"
    primary-key: true
    description: |
      The content description ([utm_content](https://support.google.com/analytics/answer/1033867?hl=en){:target="new"}).

## Primary Key
  - name: "adDestinationUrl"
    type: "dimension"
    primary-key: true
    description: "The URL to which AdWords referred traffic."
    doc-link: "https://developers.google.com/analytics/devguides/reporting/core/dimsmets#view=detail&group=adwords&jump=ga_addestinationurl"

## Primary Key
  - name: "adGroup"
    type: "dimension"
    primary-key: true
    description: "The campaign's ad group name."
    doc-link: "https://support.google.com/adwords/answer/6298?hl=en"

## Primary Key
  - name: "adwordsCampaignId"
    type: "dimension"
    primary-key: true
    description: "The campaign ID."

## Primary Key
  - name: "campaign"
    type: "dimension"
    primary-key: true
    description: |
      The campaign name ([utm_campaign](https://support.google.com/analytics/answer/1033867?hl=en)).
    doc-link: "https://developers.google.com/analytics/devguides/reporting/core/dimsmets#view=detail&group=traffic_sources&jump=ga_campaign"

## Primary Key
  - name: "date"
    type: "dimension"
    primary-key: true
    description: "The date the campaign ran."

## Primary Key
  - name: "start_date"
    type: "datetime"
    primary-key: true
    description: "The date the data in the row pertains to."

## Primary Key and Replication Key
  - name: "end_date"
    type: "datetime"
    primary-key: true
    replication-key: true
    description: "The date the data in the row pertains to."

## Primary Key
  - name: "keyword"
    type: "dimension"
    primary-key: true
    description: |
      The keyword description ([utm_term](https://support.google.com/analytics/answer/1033867?hl=en){:target="new"}).
    doc-link: "https://developers.google.com/analytics/devguides/reporting/core/dimsmets#view=detail&group=traffic_sources&jump=ga_keyword"

  - name: "adClicks"
    type: "metric"
    description: "The number of clicks for the campaign for the day."

  - name: "adCost"
    type: "metric"
    description: "The total cost for the campaign for the day."

  - name: "impressions"
    type: "metric"
    description: "The number of impressions for the day."
---