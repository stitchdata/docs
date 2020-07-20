---
tap: "bing-ads"
version: "2"

name: "ad_performance_report"
doc-link: https://docs.microsoft.com/en-us/advertising/reporting-service/adperformancereportfilter?view=bingads-13
singer-schema: 
description: |
  The `{{ table.name }}` table contains performance info about ads, including clicks and conversions. This data can be used to identify and improve under-performing ads.

  [This is a **Report** table](#replication). See the **Replication** section for information on how data is replicated and loaded for this table.

  #### Columns renamed from Bing Ads v1 {#renamed-v1-columns}

  In this version of Stitch's {{ integration.display_name }} integration, some columns have been re-named. This was done to ensure consistency between the fields in our integration and [the changes made by Microsoft to the Bing Ads API](https://docs.microsoft.com/en-us/bingads/guides/migration-guide?view=bingads-12#reporting-downloadedcolumns){:target="new}.

  - `FinalAppURL` is now `FinalAppUrl`
  - `FinalURL` is now `FinalUrl`
  - `FinalMobileURL` is now `FinalMobileUrl`

replication-method: "Key-based Incremental"
loading-behavior: "Append-Only"

attribution-window: true

attributes:
  - name: "AccountId"
    type: "integer"
    primary-key: true
    description: "The Bing Ads-assigned ID of the account."
    foreign-key-id: "accounts-id"

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
    description: "The ID of the ad group the ad is a part of."
    foreign-key-id: "ad-group-id"

  - name: "AdId"
    type: "integer"
    description: "The ad ID."
    foreign-key-id: "ad-id"

  - name: "CampaignId"
    type: "integer"
    description: "The ID of the campaign the ad is a part of."
    foreign-key-id: "campaign-id"

  - name: "Custom Fields"
    description: |
      Columns selected by you. For descriptions of available columns, refer to [Microsoft's documentation]({{ table.doc-link }}).
---