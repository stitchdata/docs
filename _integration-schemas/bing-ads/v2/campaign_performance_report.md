---
tap: "bing-ads"
version: "2.0"

name: "campaign_performance_report"
doc-link: https://docs.microsoft.com/en-us/bingads/reporting-service/campaignperformancereportcolumn#values
singer-schema: 
description: |
  The `{{ table.name }}` table contains performance data for campaigns, aggregated by day..

  [This is a **Report** table](#replication). See the **Replication** section for information on how data is replicated and loaded for this table.

  #### Column compatibility

  As per Microsoft's attribute selection rules, some columns may be incompatible. This means that you won't be able to select certain combinations of columns in Stitch. Refer to [Microsoft's documentation](https://docs.microsoft.com/en-us/bingads/guides/reports?view=bingads-12#columnrestrictions){:target="new"} for more info, and the specific column combinations for this table.

  #### Columns renamed from Bing Ads v1 {#renamed-v1-columns}

  In this version of Stitch's {{ integration.display_name }} integration, some columns have been re-named. This was done to ensure consistency between the fields in our integration and [the changes made by Microsoft to the Bing Ads API](https://docs.microsoft.com/en-us/bingads/guides/migration-guide?view=bingads-12#reporting-downloadedcolumns){:target="new}.

  - `HistoricQualityScore` is now `HistoricalQualityScore`
  - `HistoricExpectedCtr` is now `HistoricalExpectedCtr`
  - `HistoricAdRelevance` is now `HistoricalAdRelevance`
  - `HistoricLandingPageExperience` is now `HistoricalLandingPageExperience`
  - `Status` is now `CampaignStatus`

replication-method: "Key-based Incremental"
append-only-loading: true

attribution-window: true

attributes:
  - name: "AccountId"
    type: "integer"
    primary-key: true
    description: "The Bing Ads-assigned ID of the account."
    foreign-key: true

  - name: "{{ system-column.report-date-time }}"
    type: "date-time"
    primary-key: true
    description: "The start time of the Stitch replication job that replicated this record."

  - name: "TimePeriod"
    type: "date"
    primary-key: true
    replication-key: true
    description: "The day the record pertains to."

  - name: "CampaignId"
    type: "integer"
    description: "The ID of the campaign."
    foreign-key-id: "campaign-id"

  - name: "Custom Fields"
    description: |
      Columns selected by you. For descriptions of available columns, refer to [Microsoft's documentation]({{ table.doc-link }}).
---