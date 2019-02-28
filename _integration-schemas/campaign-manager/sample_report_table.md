---
tap: "campaign-manager"
# version: "1.0"

name: "[sample_report_table]"

description: |
  For each report you set to replicate, Stitch will create a table in your destination. The name of the report will be the name of the destination table, with some light transformations to ensure the table name adheres to your destination's naming rules.

  For example: A report named `Ad Performance Report` in {{ integration.display_name }} may result in a table named `ad_performance_report` or `AD_PERFORMANCE_REPORT`, depending on your destination.

replication-method: "Append-Only (Incremental)"

attributes:
  - name: "{{ system-column.primary-key }}"
    type: "string"
    primary-key: true
    description: "{{ system-column.primary-key-description }}"

  - name: "{{ system-column.report-date-time }}"
    type: "date-time"
    description: "The start time of the Stitch replication job that replicated this record."

  - name: "Dimensions"
    type: ""
    description: |
      The Dimensions you include in your {{ integration.display_name }} report will display in the table, one column for each Dimension.

  - name: "Metrics"
    type: ""
    description: |
      The Metrics you include in your {{ integration.display_name }} report will display in the table, one column for each Metric.
---