---
tap: "bing-ads"
# version: "2.0"

name: "adgroup_performance_report"
doc-link: https://docs.microsoft.com/en-us/bingads/reporting-service/adgroupperformancereportcolumn#values
singer-schema: 
description: |
  The `{{ table.name }}` table contains performance data for ad groups, aggregated by day.

  [This is a **Report** table](#replication). See the **Replication** section for information on how data is replicated and loaded for this table.

  #### Column compatibility

  As per Microsoft's attribute selection rules, some columns may be incompatible. This means that you won't be able to select certain combinations of columns in Stitch. Refer to [Microsoft's documentation](https://docs.microsoft.com/en-us/bingads/guides/reports?view=bingads-12#columnrestrictions){:target="new"} for more info, and the specific column combinations for this table.

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
    description: "The ID of the ad group.."
    foreign-key-id: "ad-group-id"

  - name: "campaignId"
    type: "integer"
    description: "The ID of the campaign the ad group is a part of."
    foreign-key-id: "campaign-id"

  - name: "Custom Fields"
    description: |
      Columns selected by you. For descriptions of available columns, refer to [Microsoft's documentation]({{ table.doc-link }}).
---