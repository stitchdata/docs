---
tap: "circle-ci"
version: "1"
key: ""

name: "pipelines"
doc-link: https://circleci.com/docs/api/v2/index.html#operation/listPipelinesForProject
singer-schema: https://github.com/singer-io/tap-circle-ci/tree/master/tap_circle_ci/schemas/pipelines.json
description: |
  The **{{ table.name }}** table contains information about piplines from your {{ integration.display_name }} projects.

replication-method: "Key-based Incremental"

api-method:
  name: "Get all pipelines"
  doc-link: "https://circleci.com/docs/api/v2/index.html#operation/listPipelinesForProject"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The pipeline ID."
    foreign-key-id: "pipeline-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the pipeline was updated."  

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "errors"
    type: "array"
    description: ""
    subattributes:
      - name: "type"
        type: "string"
        description: ""

      - name: "message"
        type: "string"
        description: ""


  - name: "number"
    type: "integer"
    description: ""

  - name: "project_slug"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "trigger"
    type: "object"
    description: ""
    subattributes:
      - name: "received_at"
        type: "date-time"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "actor"
        type: "object"
        description: ""
        subattributes:
          - name: "login"
            type: "string"
            description: ""

          - name: "avatar_url"
            type: "string"
            description: ""



  - name: "trigger_parameters"
    type: "object"
    description: ""


  - name: "vcs"
    type: "object"
    description: ""
    subattributes:
      - name: "origin_repository_url"
        type: "string"
        description: ""
 
      - name: "target_repository_url"
        type: "string"
        description: ""

      - name: "revision"
        type: "string"
        description: ""

      - name: "provider_name"
        type: "string"
        description: ""

      - name: "commit"
        type: "object"
        description: ""
        subattributes:
          - name: "body"
            type: "string"
            description: ""

          - name: "subject"
            type: "string"
            description: ""


      - name: "branch"
        type: "string"
        description: ""

      - name: "tag"
        type: "string"
        description: ""
---