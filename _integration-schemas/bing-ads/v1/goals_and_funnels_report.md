---
tap: "bing-ads"
version: "1.0"

name: "goals_and_funnels_report"
doc-link: https://docs.microsoft.com/en-us/bingads/reporting-service/goalsandfunnelsreportcolumn
singer-schema: 
description: |
  The `goals_and_funnels_report` table contains information about your audience's progression through your conversion funnel. Use this report to determine the point at which users leave the funnel, thereby allowing you to improve and increase conversion.

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
    foreign-key-id: "account-id"

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