---
tap: "google-ads"
version: "1.0"

name: "video_performance_report"
doc-link: https://developers.google.com/adwords/api/docs/appendix/reports/video-performance-report
description: |
  The `video_performance_report` table contains statistics for your account's upgraded [AdWords for Video campaigns](https://adwords.googleblog.com/2015/09/trueview-campaigns-now-in-adwords.html){:target="new"}.

  [This is a **Report** table](#replication). See the **Replication** section for information on how data is replicated and loaded for this table.

replication-method: "Key-based Incremental"
append-only-loading: true

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

  - name: "{{ system-column.report-date-time }}"
    type: "date-time"
    description: "The start time of the Stitch replication job that replicated this record."

  - name: "Custom Fields"
    description: |
      Columns (attributes/segments/metrics) selected by you. For descriptions of available columns, see [Google's documentation](https://developers.google.com/adwords/api/docs/appendix/reports/ad-performance-report){:target="_blank"}.
---