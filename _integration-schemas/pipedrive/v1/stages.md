---
tap: "pipedrive"
version: "1.0"
key: "stage"

name: "stages"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-pipedrive/blob/master/tap_pipedrive/schemas/stages.json"
description: |
  The `{{ table.name }}` table contains info about the pipeline stages in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get all stages"
  doc-link: "https://developers.pipedrive.com/docs/api/v1/#!/Stages/get_stages"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The stage ID."
    foreign-key-id: "stage-id"

  - name: "update_time"
    type: "date-time"
    replication-key: true
    description: "The time the stage was last updated."

  - name: "active_flag"
    type: "boolean"
    description: ""

  - name: "add_time"
    type: "date-time"
    description: ""

  - name: "deal_probability"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "order_nr"
    type: "integer"
    description: ""

  - name: "pipeline_id"
    type: "integer"
    description: ""
    foreign-key-id: "pipeline-id"

  - name: "pipeline_name"
    type: "string"
    description: ""

  - name: "rotten_days"
    type: "integer"
    description: ""

  - name: "rotten_flag"
    type: "boolean"
    description: ""
---