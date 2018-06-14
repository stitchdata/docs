---
tap: "google-analytics-adwords"
version: "15-10-2015"

name: "adwords123456789_v2"
doc-link: 
description: |
  The `adwords` table contains daily info about each of your active campaigns and the ads contained within those campaigns.

  **Note**: Google AdWords data is paginated on a daily basis. This means that a single row in each of the tables pertains to a single day.

replication-method: "Key-based Incremental"
attribution-window: true

attributes:
## Primary Key
  - name: "campaign"
    type: "dimension"
    primary-key: true
    description: |
      The campaign name ([utm_campaign](https://support.google.com/analytics/answer/1033867?hl=en))
    doc-link: "https://developers.google.com/analytics/devguides/reporting/core/dimsmets#view=detail&group=traffic_sources&jump=ga_campaign"

## Primary Key
  - name: "adwordsCampaignId"
    type: "dimension"
    primary-key: true
    description: "The campaign ID."

## Primary Key
  - name: "adGroup"
    type: "dimension"
    primary-key: true
    description: "The campaign's ad group name."
    doc-link: "https://support.google.com/adwords/answer/6298?hl=en"

## Primary Key
  - name: "adDestinationUrl"
    type: "dimension"
    primary-key: true
    description: "The URL to which AdWords referred traffic."
    doc-link: "https://developers.google.com/analytics/devguides/reporting/core/dimsmets#view=detail&group=adwords&jump=ga_addestinationurl"

## Primary Key
  - name: "adContent"
    type: "dimension"
    primary-key: true
    description: |
      The content description ([utm_content](https://support.google.com/analytics/answer/1033867?hl=en){:target="new"})

## Primary Key
  - name: "date"
    type: "dimension"
    primary-key: true
    replication-key: true
    description: "The timestamp for the date the campaign ran."

## Primary Key
  - name: "keyword"
    type: "dimension"
    primary-key: true
    description: |
      This column contains the keyword description ([utm_term](https://support.google.com/analytics/answer/1033867?hl=en){:target="new"})
    doc-link: "https://developers.google.com/analytics/devguides/reporting/core/dimsmets#view=detail&group=traffic_sources&jump=ga_keyword"

  - name: "accountId"
    type: "dimension"
    description: "Your Google Analytics account ID."

  - name: "adClicks"
    type: "metric"
    description: "The number of clicks for the day."

  - name: "adCost"
    type: "metric"
    description: "The total cost for the campaign for the day."

  - name: "impressions"
    type: "metric"
    description: "The number of impressions for the day."

  - name: "profileId"
    type: "dimension"
    description: "Your Google Analytics profile ID."

  - name: "profileName"
    type: "dimension"
    description: "Your Google Analytics profile name."
---