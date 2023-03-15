---
tap: "circle-ci"
version: "1"
key: ""

name: "jobs"
doc-link: https://circleci.com/docs/api/v2/index.html#operation/listWorkflowJobs
singer-schema: https://github.com/singer-io/tap-circle-ci/tree/master/tap_circle_ci/schemas/jobs.json
description: |
  The **{{ table.name }}** table contains information about jobs from your {{ integration.display_name }} workflows.

replication-method: "Full Table"

api-method:
  name: "Get a workflow's jobs"
  doc-link: "https://circleci.com/docs/api/v2/index.html#operation/listWorkflowJobs"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The job ID."
    #foreign-key-id: "job-id"

  - name: "_sdc_record_hash"
    type: "string"
    primary-key: true
    description: "The record hash."
    #foreign-key-id: "record-id"  

  - name: "_pipeline_id"
    type: "string"
    description: "The pipeline ID."
    foreign-key-id: "pipeline-id"

  - name: "_workflow_id"
    type: "string"
    description: "The workflow ID."
    foreign-key-id: "workflow-id"

  - name: "approval_request_id"
    type: "string"
    description: ""

  - name: "approved_by"
    type: "string"
    description: ""

  - name: "canceled_by"
    type: "string"
    description: ""

  - name: "dependencies"
    type: "array"
    description: ""
    subattributes:
      - name: "items"
        type: "string"
        description: ""

  - name: "job_number"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "project_slug"
    type: "string"
    description: ""

  - name: "started_at"
    type: "date-time"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "stopped_at"
    type: "date-time"
    description: ""

  - name: "type"
    type: "string"
    description: ""
---