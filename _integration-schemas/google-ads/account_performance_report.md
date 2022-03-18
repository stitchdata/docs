---
tap: "google-ads"
version: "1"

name: "account_performance_report"
doc-link: https://developers.google.com/adwords/api/docs/appendix/reports/account-performance-report
description: |
  The `{{ table.name }}` table contains all statistics aggregated by default at the account level.

  [This is a **Report** table](#replication). See the **Replication** section for information on how data is replicated and loaded for this table.

replication-method: "Key-based Incremental"
loading-behavior: "Append-Only"

attribution-window: true

attributes:
  - name: "{{ system-column.primary-key }}"
    type: "string"
    primary-key: true
    description: "{{ system-column.primary-key-description }}"

  - name: "day"
    type: "date-time"
    replication-key: true
    description: "The day the record pertains to."

  - name: "{{ system-column.customer-id }}"
    type: "integer"
    description: "The ID of the AdWords account that the record belongs to."
    foreign-key-id: "customer-id"
    foreign-key-id: "customer-id"

  - name: "{{ system-column.report-date-time }}"
    type: "date-time"
    description: "The start time of the Stitch replication job that replicated this record."

  - name: "customerCurrencyCode"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "customerDescriptiveName"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "customerTimeZone"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsActiveViewCpm"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsActiveViewCtr"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsActiveViewImpressions"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsActiveViewMeasurability"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsActiveViewMeasurableCostMicros"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsActiveViewMeasurableImpressions"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsActiveViewViewability"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "segmentsAdNetworkType"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsAllConversionsFromInteractionsRate"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsAllConversionsValue"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsAllConversions"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsAverageCost"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsAverageCpc"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsAverageCpe"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsAverageCpm"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsAverageCpv"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "customerManager"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "segmentsClickType"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsClicks"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsContentBudgetLostImpressionShare"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsContentImpressionShare"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsContentRankLostImpressionShare"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "segmentsConversionAdjustment"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "segmentsConversionOrAdjustmentLagBucket"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "segmentsConversionActionCategory"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "segmentsConversionLagBucket"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsConversionsFromInteractionsRate"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "segmentsConversionAction"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "segmentsConversionActionName"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsConversionsValue"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsConversions"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsCostMicros"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsCostPerAllConversions"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsCostPerConversion"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsCrossDeviceConversions"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsCtr"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "customerDescriptiveName"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "segmentsDate"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "segmentsDayOfWeek"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "segmentsDevice"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsEngagementRate"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsEngagements"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "segmentsExternalConversionSource"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "customerId"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "segmentsHour"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsImpressions"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsInteractionRate"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsInteractionEventTypes"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsInteractions"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsInvalidClickRate"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsInvalidClicks"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "customerAutoTaggingEnabled"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "customerTestAccount"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "segmentsMonth"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "segmentsMonthOfYear"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "segmentsQuarter"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsSearchBudgetLostImpressionShare"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsSearchExactMatchImpressionShare"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsSearchImpressionShare"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsSearchRankLostImpressionShare"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "segmentsSlot"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsValuePerAllConversions"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsValuePerConversion"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsVideoViewRate"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsVideoViews"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "metricsViewThroughConversions"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "segmentsWeek"
    type: ""
    description: "{{ system-column.optional-column-description }}"

  - name: "segmentsYear"
    type: ""
    description: "{{ system-column.optional-column-description }}"
---