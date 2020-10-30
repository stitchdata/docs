---
tap: "mixpanel"
version: "1"
key: "export"

name: "export"
doc-link: "https://developer.mixpanel.com/docs/exporting-raw-data#section-export-api-reference"
singer-schema: "https://github.com/singer-io/tap-mixpanel/blob/master/tap_mixpanel/schemas/export.json"
description: |
  The `{{ table.name }}` table contains "raw data dumps" of tracked events.

  #### Table schema {#export-events-table-schema}

  The schema for this table is dynamic, meaning that the columns Stitch detects are dependent upon the properties provided upon upload in {{ integration.display_name }}. For every property available in {{ integration.display_name }} for `{{ table.name }}` records, Stitch will display a column in the integration's **Tables to Replicate** tab.

  #### Replication with attribution window {#export-events-attribution-window}

  This table is replicated using the **Attribution Window** value defined in the integration's settings page. Refer to the [Replication section](#attribution-windows-extraction) for more info.

  #### Distinct events and loading behavior {#export-events-loading-behavior}

  As Stitch doesn't use a Primary Key for this table, data will be loaded using [Append-Only loading]({{ link.destinations.storage.loading-behavior | prepend: site.baseurl }}). This means you may see duplicate records in your destination, which requires a querying strategy that selects the latest version of each record.

  Stitch takes this approach because it's possible to track events without a `distinct_id`. In {{ integration.display_name }}, `distinct_id` [is used to identify a unique user](https://help.mixpanel.com/hc/en-us/articles/115004509406-Distinct-IDs-){:target="new"}:

  > Mixpanel’s client-side tracking libraries automatically assign a distinct_id to a user when they first visit a website or an application that has Mixpanel installed. Distinct_id should not contain any special characters such as forward slashes, as it will break the URL.
  > Distinct_ids can and often should be sent in server-side implementations as well.

  In order for Stitch to replicate records' `distinct_id` attributes, your server-side {{ integration.display_name }} implementation must send them with tracked events. If the server-side implementation doesn't do this, this attribute will be `null`.

  Previous versions of Stitch's {{ integration.display_name }} integration used `distinct_id` as part of a composite Primary Key for this table. However, due to the possibility of this attribute being `null`, Stitch no longer uses a Primary Key for this table, as `null` values in Primary Key columns will prevent successful Extraction. 

  When working with `exports` data in your destination, you'll need to use a querying strategy that accounts for the Append-Only loading used by this table. We recommend using the following columns to de-duplicate records, along with the approach outlined in the [Querying Append-Only tables guide]({{ link.replication.append-only-querying | prepend: site.baseurl }}):

  - `distinct_id`
  - `event`
  - `time`

replication-method: "Key-based Incremental"
attribution-window: true

loading-behavior: "Append-Only"

api-method:
  name: "Export raw data"
  doc-link: "https://developer.mixpanel.com/docs/exporting-raw-data#section-export-api-reference"

attributes:
  - name: "time"
    type: "date-time"
    replication-key: true
    description: |
      The time the event occurred.

      When analzying this table's data, we recommend using this column, `distinct_id`, and `event`, along with a [querying strategy for Append-Only tables]({{ link.replication.append-only-querying | prepend: site.baseurl }}) to de-duplicate records. Refer to the [table description](#export-events-loading-behavior) for more info.

  - name: "distinct_id"
    type: "string"
    description: |
      The user associated with the event.

      When analzying this table's data, we recommend using this column, `event`, and `time`, along with a [querying strategy for Append-Only tables]({{ link.replication.append-only-querying | prepend: site.baseurl }}) to de-duplicate records. Refer to the [table description](#export-events-loading-behavior) for more info.

  - name: "dataset"
    type: "string"
    description: ""

  - name: "event"
    type: "string"
    description: |
      The event. For example: `Viewed report`

      When analzying this table's data, we recommend using this column, `distinct_id`, and `time`, along with a [querying strategy for Append-Only tables]({{ link.replication.append-only-querying | prepend: site.baseurl }}) to de-duplicate records. Refer to the [table description](#export-events-loading-behavior) for more info.

  - name: "labels"
    type: "array"
    description: ""
    subattributes:
      - title: "value"
        type: "string"
        description: ""

  - name: "sampling_factor"
    type: "integer"
    description: ""

  - name: "OTHER_ATTRIBUTES"
    type: "varies"
    description: |
      For every property available in {{ integration.display_name }} for `{{ table.name }}` records, Stitch will display a column in the integration's **Tables to Replicate** tab.
---