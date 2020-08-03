---
tap: "pipedrive"
version: "1"
key: "pipeline"

name: "pipelines"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-pipedrive/blob/master/tap_pipedrive/schemas/pipelines.json"
description: |
  The `{{ table.name }}` table contains info about the pipelines in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get all pipelines"
  doc-link: "https://developers.pipedrive.com/docs/api/v1/#!/Pipelines"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The pipeline ID."
    foreign-key-id: "pipeline-id"

  - name: "update_time"
    type: "date-time"
    replication-key: true
    description: "The time the pipeline was last updated."

  - name: "active"
    type: "boolean"
    description: ""

  - name: "add_time"
    type: "date-time"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "order_nr"
    type: "integer"
    description: ""

  - name: "selected"
    type: "boolean"
    description: ""

  - name: "url_title"
    type: "string"
    description: ""
---