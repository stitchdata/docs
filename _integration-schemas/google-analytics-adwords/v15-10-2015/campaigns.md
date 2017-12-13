---
tap: "google-analytics-adwords"
version: "15-10-2015"

name: "campaigns123456789_v2"
doc-link:  
description: |
  The `campaigns` table contains daily info about your AdWords campaigns.

  **Note**: Google AdWords data is paginated on a daily basis. This means that a single row in each of the tables pertains to a single day.

replication-method: "Incremental"
attribution-window: true

attributes:
## Primary Key
  - name: "campaign"
    type: "dimension"
    primary-key: true
    description: |
      The name of the campaign ([utm_campaign](https://support.google.com/analytics/answer/1033867?hl=en){:target="new"}).
    doc-link: https://developers.google.com/analytics/devguides/reporting/core/dimsmets#view=detail&group=traffic_sources&jump=ga_campaign

## Primary Key
  - name: "adwordsCampaignId"
    type: "dimension"
    primary-key: true
    description: "The campaign ID."

## Primary Key
  - name: "date"
    type: "dimension"
    primary-key: true
    replication-key: true
    description: "The timestamp for the date the campaign ran."

  - name: "accountId"
    type: "dimension"
    description: "Your Google Analytics account ID."

  - name: "adClicks"
    type: "metric"
    description: "The number of clicks for the campaign for the day."

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