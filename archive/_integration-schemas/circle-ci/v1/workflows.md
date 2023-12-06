---
tap: "circle-ci"
version: "1"
key: ""

name: "workflows"
doc-link: https://circleci.com/docs/api/v2/index.html#operation/listWorkflowsByPipelineId
singer-schema: https://github.com/singer-io/tap-circle-ci/tree/master/tap_circle_ci/schemas/workflows.json
description: |
  The **{{ table.name }}** table contains a list of workflows from your {{ integration.display_name }} projects, sorted by pipeline ID.

replication-method: "Key-based Incremental"

api-method:
  name: "Get a pipeline's workflows."
  doc-link: "https://circleci.com/docs/api/v2/index.html#operation/listWorkflowsByPipelineId"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The workflow ID."
    foreign-key-id: "workflow-id"

  - name: "created_at"
    type: "date-time"
    replication-key: true
    description: "The time the workflow was created."  

  - name: "canceled_by"
    type: "string"
    description: ""

  - name: "errored_by"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "pipeline_id"
    type: "string"
    description: "The pipeline ID."
    foreign-key-id: "pipeline-id"

  - name: "pipeline_number"
    type: "integer"
    description: ""

  - name: "project_slug"
    type: "string"
    description: ""

  - name: "started_by"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "stopped_at"
    type: "string"
    format: "date-time"
    description: ""

  - name: "tag"
    type: "string"
    description: ""
---