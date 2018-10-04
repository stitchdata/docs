---
tap: "bing-ads"
# version: "2.0"

name: "search_query_performance_report"
doc-link: https://docs.microsoft.com/en-us/bingads/reporting-service/searchqueryperformancereportcolumn#values
singer-schema: 
description: |
  The `{{ table.name }} ` table contains performance data for search terms that resulted in a significant number of clicks in the last 30 days. As this data may change over time, use the `keyword_performance_report` table to analyze the overall performance of keywords.

  **Note**: This data in this table is not applicable to Bing Shopping campaigns.

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

  - name: "adGroupId"
    type: "integer"
    description: "The ID of the ad group."
    foreign-key-id: "ad-group-id"

  - name: "campaignId"
    type: "integer"
    description: "The ID of the campaign."
    foreign-key-id: "campaign-id"

  - name: "Custom Fields"
    description: |
      Columns selected by you. For descriptions of available columns, refer to [Microsoft's documentation]({{ table.doc-link }}).
---