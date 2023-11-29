---
tap: "frontapp"
version: "1"
key: ""

name: "tags_table"
doc-link: "https://dev.frontapp.com/#analytics"
singer-schema: "https://github.com/singer-io/tap-frontapp/blob/master/tap_frontapp/schemas/tags_table.json"
description: |
  The `{{ table.name }}` table contains a list of tag statistics since the last completed replication job through the most recent iteration of the defined [**Incremental Range**](#add-stitch-data-source) (day or hour).

  This table will include tags in your {{ integration.display_name }} account.

  **Note**: During the historical replication job, all increments (defined using the **Incremental Range** setting) since the **Start Date** will be replicated. This will result in the first record for this table being an aggregated record across all tags.

replication-method: "Key-based Incremental"

api-method:
    name: "getAnalytics"
    doc-link: "https://dev.frontapp.com/#analytics"

attributes:
  - name: "analytics_date"
    type: "string"
    description: ""
    replication-key: true

  - name: "analytics_range"
    type: "string"
    description: ""
    replication-key: true

  - name: "avg_first_response_time"
    type: "number"
    description: ""

  - name: "avg_handle_time"
    type: "number"
    description: ""

  - name: "avg_response_time"
    type: "number"
    description: ""

  - name: "avg_sla_breach_time"
    type: "number"
    description: ""

  - name: "avg_total_reply_time"
    type: "number"
    description: ""

  - name: "metric_description"
    type: "string"
    description: ""

  - name: "metric_id"
    type: "string"
    description: ""

  - name: "new_segments_count"
    type: "number"
    description: ""

  - name: "num_active_segments_full"
    type: "number"
    description: ""

  - name: "num_archived_segments"
    type: "number"
    description: ""

  - name: "num_archived_segments_with_reply"
    type: "number"
    description: ""

  - name: "num_closed_segments"
    type: "number"
    description: ""

  - name: "num_csat_survey_response"
    type: "number"
    description: ""

  - name: "num_messages_received"
    type: "number"
    description: ""

  - name: "num_messages_sent"
    type: "number"
    description: ""

  - name: "num_open_segments_end"
    type: "number"
    description: ""

  - name: "num_open_segments_start"
    type: "number"
    description: ""

  - name: "num_sla_breach"
    type: "number"
    description: ""

  - name: "num_workload_segments"
    type: "number"
    description: ""

  - name: "pct_csat_survey_satisfaction"
    type: "number"
    description: ""

  - name: "pct_tagged_conversations"
    type: "number"
    description: ""

  - name: "report_id"
    type: "string"
    description: ""
    primary-key: true
---
