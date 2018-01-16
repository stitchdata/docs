---
tap: "bing-ads"
# version: "1.0"

name: "search_query_performance_report"
doc-link: ## link to source's API docs
singer-schema: ## link to the JSON schema file in the integration's Singer repo
description: |
  The `search_query_performance_report` contains performance data for search terms that resulted in a significant number of clicks in the last 30 days. As this data may change over time, use the `keyword_performance_report` table to analyze the overall performance of keywords.

  **Note**: This data in this table is not applicable to Bing Shopping campaigns.

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

  - name: "{{ system-column.report-date-time }}"
    type: "date-time"
    primary-key: true
    description: "The start time of the Stitch replication job that replicated this record."

  - name: "gregorianDate"
    type: "date"
    primary-key: true
    replication-key: true
    description: "The day the record pertains to."

  - name: "Custom Fields"
    description: |
      Columns selected by you. For descriptions of available columns, refer to [Microsoft's documentation](){:target="_blank"}.
---