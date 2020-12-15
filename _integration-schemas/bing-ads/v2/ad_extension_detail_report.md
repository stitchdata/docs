---
# Commenting out as this table isn't currently functional in the tap (12/15/2020)
# tap: "bing-ads"
# version: "2"

name: "ad_extension_detail_report"
doc-link: https://docs.microsoft.com/en-us/advertising/reporting-service/adextensiondetailreportfilter?view=bingads-13
singer-schema: 
description: |
  The `{{ table.name }}` table contains info about ad extension items.

  [This is a **Report** table](#replication). See the **Replication** section for information on how data is replicated and loaded for this table.

replication-method: "Key-based Incremental"
loading-behavior: "Append-Only"

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

  - name: "AdExtensionId"
    type: ""
    description: "The ID of the ad extension."
    foreign-key-id: "ad-extension-id"

  - name: "AdExtensionTypeId"
    type: "string"
    description: "The ID of the ad extension type."
    foreign-key-id: "ad-extension-type-id"

  - name: "AdExtensionPropertyValue"
    type: "string"
    description: ""

  - name: "AdExtensionType"
    type: "string"
    description: ""

  - name: "Custom Fields"
    description: |
      Columns selected by you. For descriptions of available columns, refer to [Microsoft's documentation]({{ table.doc-link }}).
---