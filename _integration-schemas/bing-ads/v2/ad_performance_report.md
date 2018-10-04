---
tap: "bing-ads"
# version: "2.0"

name: "ad_performance_report"
doc-link: https://docs.microsoft.com/en-us/bingads/reporting-service/adperformancereportcolumn#values
singer-schema: 
description: |
  The `ad_performance_report` table contains performance info about ads, including clicks and conversions. This data can be used to identify and improve under-performing ads.

  [This is a **Report** table](#replication). See the **Replication** section for information on how data is replicated and loaded for this table.

replication-method: "Append-Only (Incremental)"
api-method:
  name:
  doc-link: 

attributes:
  - name: "accountId"
    type: "integer"
    primary-key: true
    description: "The Bing Ads-assigned ID of the account."
    foreign-key-id: "accounts-id"

  - name: "{{ system-column.report-date-time }}"
    type: "date-time"
    primary-key: true
    description: "The start time of the Stitch replication job that replicated this record."

  - name: "gregorianDate"
    type: "date"
    primary-key: true
    replication-key: true
    description: "The day the record pertains to."

  - name: "adGroupId"
    type: "integer"
    description: "The ID of the ad group the ad is a part of."
    foreign-key-id: "ad-group-id"

  - name: "adId"
    type: "integer"
    description: "The ad ID."
    foreign-key-id: "ad-id"

  - name: "campaignId"
    type: "integer"
    description: "The ID of the campaign the ad is a part of."
    foreign-key-id: "campaign-id"

  - name: "Custom Fields"
    description: |
      Columns selected by you. For descriptions of available columns, refer to [Microsoft's documentation]({{ table.doc-link }}).
---