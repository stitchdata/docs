---
tap: "twitter-ads"
version: "1"
key: "custom-report-example"

name: "EXAMPLE_CUSTOM_REPORT"
doc-link: "active_entities"
description: |
  {% assign reference = integration.other-sections | where:"anchor","reference" | first %}
  {% assign custom-report-options = reference.custom-report-options %}

  This is an example of a table created from a custom report configured in the integration's settings page.

  Metric columns in report tables depend on the [entity selected for the report](#custom-report-configuration-options--compatibility).

  When data is extracted for reports, Stitch uses the [Attribution Window](#add-stitch-data-source) defined in the integration's settings.

replication-method: "Key-based Incremental"
loading-behavior: "Append-Only"

attributes:
  - name: "{{ system-column.dimension-hash-key }}"
    type: "string"
    primary-key: true
    description: "{{ system-column.dimension-hash-key-description | flatify }}"

  - name: "end_time"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "METRICS_YOU_SELECT"
    type: "varies"
    description: |
      The available metrics depend on the entity you select for the report. Refer to the [Entity and metric group compatibility reference](#custom-report-configuration-options--compatibility) for more info.

  - name: "account_id"
    type: "string"
    description: ""
    foreign-key-id: "account-id"

  - name: "country"
    type: "string"
    description: ""

  - name: "entity"
    type: "string"
    description: |
      The entity selected for the report. Refer to the [Entity and metric group compatibility reference](#custom-report-configuration-options--compatibility) for more info.

      Possible values are:

      {% for entity in custom-report-options.entities %}
      - `{{ entity.name | upcase }}`
      {% endfor %}

  - name: "entity_id"
    type: "string"
    description: "The name of the entity selected for the report."

  - name: "granularity"
    type: "string"
    description: |
      The granularity selected for the report. Possible values are:

      - `HOUR`
      - `DAY`
      - `TOTAL`

  - name: "placement"
    type: "string"
    description: ""

  - name: "platform"
    type: "string"
    description: ""

  - name: "report_name"
    type: "string"
    description: ""

  - name: "segment_name"
    type: "string"
    description: ""

  - name: "segment_value"
    type: "string"
    description: ""

  - name: "segmentation_type"
    type: "string"
    description: ""
---