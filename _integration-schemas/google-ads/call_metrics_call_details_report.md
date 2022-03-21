---
tap: "google-ads"
version: "1"

name: "call_metrics_call_details_report"
doc-link: https://developers.google.com/adwords/api/docs/appendix/reports/call-metrics-call-details-report
description: |
  The `{{ table.name }}` table contains data for call tracking of call-only ads or call extensions.

  [This is a **Report** table](#replication). See the **Replication** section for information on how data is replicated and loaded for this table.

replication-method: "Key-based Incremental"
loading-behavior: "Append-Only"

attribution-window: true

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: "{{ system-column.record-hash-google-ads }}"

  - name: "date"
    type: "date-time"
    replication-key: true
    description: "The day the record pertains to."

  - name: "customer_id"
    type: "integer"
    description: "The ID of the Ads account that the record belongs to."
    foreign-key-id: "customer_id"

  - name: "{{ site.data.taps.extraction.google-ads.custom-fields.name }}"
    description: "{{ site.data.taps.extraction.google-ads.custom-fields.description }}"
---