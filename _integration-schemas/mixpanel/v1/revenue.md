---
tap: "mixpanel"
version: "1"
key: "revenue"

name: "revenue"
doc-link: "https://developer.mixpanel.com/docs/data-export-api#hrspan-stylefont-family-courierrevenuespan"
singer-schema: "https://github.com/singer-io/tap-mixpanel/blob/master/tap_mixpanel/schemas/revenue.json"
description: |
  The `{{ table.name }}` table contains info about revenue, segmented by day.

  **Note**: This table is replicated using the **Attribution Window** value defined in the integration's settings page. Refer to the [Replication section](#attribution-windows-extraction) for more info.

replication-method: "Key-based Incremental"
attribution-window: true

api-method:
  name: "Export formatted data (Revenue)"
  doc-link: "https://developer.mixpanel.com/docs/data-export-api#hrspan-stylefont-family-courierrevenuespan"

attributes:
  - name: "date"
    type: "date"
    primary-key: true
    replication-key: true
    description: "The day the revenue data is for."

  - name: "amount"
    type: "number"
    description: ""

  - name: "count"
    type: "integer"
    description: ""

  - name: "datetime"
    type: "date-time"
    description: ""

  - name: "paid_count"
    type: "integer"
    description: ""
---