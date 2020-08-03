---
tap: "mixpanel"
version: "1"
key: "export"

name: "export"
doc-link: "https://developer.mixpanel.com/docs/exporting-raw-data#section-export-api-reference"
singer-schema: "https://github.com/singer-io/tap-mixpanel/blob/master/tap_mixpanel/schemas/export.json"
description: |
  The `{{ table.name }}` table contains "raw data dumps" of tracked events.

  The schema for this table is dynamic, meaning that the columns Stitch detects are dependent upon the properties provided upon upload in {{ integration.display_name }}. For every property available in {{ integration.display_name }} for `{{ table.name }}` records, Stitch will display a column in the integration's **Tables to Replicate** tab.

  **Note**: This table is replicated using the **Attribution Window** value defined in the integration's settings page. Refer to the [Replication section](#attribution-windows-extraction) for more info.

replication-method: "Key-based Incremental"
attribution-window: true

api-method:
  name: "Export raw data"
  doc-link: "https://developer.mixpanel.com/docs/exporting-raw-data#section-export-api-reference"

attributes:
  - name: "distinct_id"
    type: "string"
    primary-key: true
    description: ""

  - name: "event"
    type: "string"
    primary-key: true
    description: "The event. For example: `Viewed report`"

  - name: "time"
    type: "date-time"
    primary-key: true
    replication-key: true
    description: "The time the event occurred."

  - name: "dataset"
    type: "string"
    description: ""

  - name: "labels"
    type: "null"
    description: ""

  - name: "sampling_factor"
    type: "integer"
    description: ""

  - name: "OTHER_ATTRIBUTES"
    type: "varies"
    description: |
      For every property available in {{ integration.display_name }} for `{{ table.name }}` records, Stitch will display a column in the integration's **Tables to Replicate** tab.
---