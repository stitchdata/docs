---
tap: "google-adwords"
version: "1.0"

name: "final_url_report"
doc-link: https://developers.google.com/adwords/api/docs/appendix/reports/gender-performance-report
description: |
  The `final_url_report` table contains all statistics aggregated at the final URL level.

  [This is a **Report** table](#replication). See the **Replication** section for information on how data is replicated and loaded for this table.

replication-method: "Append-Only (Incremental)"
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

  - name: "{{ system-column.report-date-time }}"
    type: "date-time"
    description: "The start time of the Stitch replication job that replicated this record."

  - name: "Custom Fields"
    description: |
      Columns (attributes/segments/metrics) selected by you. For descriptions of available columns, see [Google's documentation](https://developers.google.com/adwords/api/docs/appendix/reports/campaign-performance-report){:target="_blank"}.
---