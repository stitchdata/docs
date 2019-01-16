---
tap: "bing-ads"
version: "2.0"

name: "geographic_performance_report"
doc-link: https://docs.microsoft.com/en-us/bingads/reporting-service/geographicperformancereportcolumn#values
singer-schema: 
description: |
  The `{{ table.name }}` table contains info about the physical locations of people searching for an ad or the locations people are searching for. This data can be used to validate or improve location targeting strategies.

  [This is a **Report** table](#replication). See the **Replication** section for information on how data is replicated and loaded for this table.

replication-method: "Append-Only (Incremental)"
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