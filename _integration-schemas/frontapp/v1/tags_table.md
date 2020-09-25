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

  **Note**: During the historical replication job, all increments since the **Start Date** will be replicated. This will result in the first record for this table being an aggregated record across all tags.

replication-method: "Key-based Incremental"

api-method:
    name: "getAnalytics"
    doc-link: "https://dev.frontapp.com/#analytics"

attributes:
  - name: "tag_v"
    type: "string"
    primary-key: true
    description: "The tag ID."

  - name: "analytics_range"
    type: "string"
    primary-key: true
    description: "The range the analytics pertain to."

  - name: "analytics_date"
    type: "date"
    primary-key: true
    replication-key: true
    description: "The date the analytics pertain to."  

  - name: "avg_message_conversations_p"
    type: "number"
    description: ""
  - name: "avg_message_conversations_v"
    type: "number"
    description: ""
  - name: "conversations_archived_p"
    type: "integer"
    description: ""
  - name: "conversations_archived_v"
    type: "integer"
    description: ""
  - name: "conversations_open_p"
    type: "integer"
    description: ""
  - name: "conversations_open_v"
    type: "integer"
    description: ""
  - name: "conversations_total_p"
    type: "integer"
    description: ""
  - name: "conversations_total_v"
    type: "integer"
    description: ""
  - name: "num_messages_p"
    type: "integer"
    description: ""
  - name: "num_messages_v"
    type: "integer"
    description: ""
  - name: "tag_id"
    type: "integer"
    description: ""
  - name: "tag_url"
    type: "string"
    description: ""
---
