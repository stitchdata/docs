---
tap: "bing-ads"
version: "2"

name: "keyword_performance_report"
doc-link: https://docs.microsoft.com/en-us/advertising/reporting-service/keywordperformancereportfilter?view=bingads-13
singer-schema: 
description: |
  The `{{ table.name }}` table contains performance data about keywords.

  [This is a **Report** table](#replication). See the **Replication** section for information on how data is replicated and loaded for this table.

  #### Columns renamed from Bing Ads v1 {#renamed-v1-columns}

  In this version of Stitch's {{ integration.display_name }} integration, some columns have been re-named. This was done to ensure consistency between the fields in our integration and [the changes made by Microsoft to the Bing Ads API](https://docs.microsoft.com/en-us/bingads/guides/migration-guide?view=bingads-12#reporting-downloadedcolumns){:target="new}.

  - `FinalAppURL` is now `FinalAppUrl`
  - `FinalURL` is now `FinalUrl`
  - `FinalMobileURL` is now `FinalMobileUrl`
  - `HistoricQualityScore` is now `HistoricalQualityScore`
  - `HistoricExpectedCtr` is now `HistoricalExpectedCtr`
  - `HistoricAdRelevance` is now `HistoricalAdRelevance`
  - `HistoricLandingPageExperience` is now `HistoricalLandingPageExperience`
  - `Status` is now `CampaignStatus`
  - `SidebarBid` is now `FirstPageBid`

replication-method: "Key-based Incremental"
append-only-loading: true

attribution-window: true

attributes:
  - name: "AccountId"
    type: "integer"
    primary-key: true
    description: "The Bing Ads-assigned ID of the account."
    foreign-key-id: "account-id"

  - name: "{{ system-column.report-date-time }}"
    type: "date-time"
    primary-key: true
    description: "The start time of the Stitch replication job that replicated this record."

  - name: "TimePeriod"
    type: "date"
    primary-key: true
    replication-key: true
    description: "The day the record pertains to."

  - name: "AdGroupId"
    type: "integer"
    description: "The ID of the ad group."
    foreign-key-id: "ad-group-id"

  - name: "CampaignId"
    type: "integer"
    description: "The ID of the campaign."
    foreign-key-id: "campaign-id"

  - name: "Custom Fields"
    description: |
      Columns selected by you. For descriptions of available columns, refer to [Microsoft's documentation]({{ table.doc-link }}).
---