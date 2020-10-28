---
tap: "looker"
version: "1"
key: "query-history"

name: "query_history"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/query_history.json"
description: |
  The `{{ table.name }}` table contains query history data pulled from {{ integration.display_name }}'s [History Explore](https://docs.looker.com/admin-options/tutorials/i__looker){:target="new"}, or `i__looker` database, for queries run in the past seven days.

  To extract this data, Sttich will submit a query with [the properties in this file](https://github.com/singer-io/tap-looker/blob/master/tap_looker/streams.py#L363){:target="new"} to the {{ integration.display_name }} API. The results of Stitch's query are then extracted and replicated to your destination.

  **Note**: Stitch's {{ integration.display_name }} integration only replicates the **past seven days** of query history at any given time.

replication-method: "Full Table"

api-method:
  name: "Run inline query"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/query#run_inline_query"

attributes:
  - name: "dims_hash_key"
    type: "string"
    primary-key: true
    description: ""

  - name: "history_created_date"
    type: "string"
    primary-key: true
    description: ""

  - name: "query_id"
    type: "string"
    description: ""
    primary-key: true
    foreign-key-id: "query-id"

  - name: "dashboard_id"
    type: "string"
    description: ""
    foreign-key-id: "dashboard-id"

  - name: "history_query_run_count"
    type: "integer"
    description: ""

  - name: "history_total_runtime"
    type: "number"
    description: ""

  - name: "look_id"
    type: "string"
    description: ""
    foreign-key-id: "look-id"

  - name: "query_model"
    type: "string"
    description: ""
    foreign-key-id: "model-id"

  - name: "query_view"
    type: "string"
    description: ""

  - name: "space_id"
    type: "string"
    description: ""
    foreign-key-id: "space-id"

  - name: "user_id"
    type: "string"
    description: ""
    foreign-key-id: "user-id"
---