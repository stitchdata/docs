---
tap: "frontapp"
version: "1"
key: ""

name: "inboxes_table"
doc-link: "https://dev.frontapp.com/reference/analytics"
singer-schema: https://github.com/singer-io/tap-frontapp/blob/master/tap_frontapp/schemas/inboxes_table.json
description: "The `{{ table.name }}` table contains data about inboxes in your {{ integration.display_name }} account."

replication-method: "Key-based Incremental"



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