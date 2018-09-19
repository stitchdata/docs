---
tap: "hubspot"
version: "1.0"

name: "deal_pipelines"
doc-link: https://developers.hubspot.com/docs/methods/deal-pipelines/overview
singer-schema: https://github.com/singer-io/tap-hubspot/blob/master/tap_hubspot/schemas/deal_pipelines.json
description: |
  The `{{ table.name }}` table contains info about the `deal stage` and `pipeline` properties.

replication-method: "Full Table"
api-method:
  name: getAllDealPipelines
  doc-link: https://developers.hubspot.com/docs/methods/deal-pipelines/get-all-deal-pipelines

attributes:
## Primary Key
  - name: "pipelineId"
    type: "string"
    primary-key: true
    description: "The internal ID of the pipeline."
    # foreign-key-id: "deal-pipeline-id"

  - name: "stages"
    type: "array"
    description: "A list of stages for this specific pipeline."
    array-attributes:
      - name: "stageId"
        type: "string"
        description: "The internal ID of the stage."

      - name: "label"
        type: "string"
        description: "The human-readable label for the stage."

      - name: "probability"
        type: "number"
        description: "The probability that the deal will close."

      - name: "active"
        type: "boolean"
        description: "Indicates if the stage is currently in use."

      - name: "displayOrder"
        type: "integer"
        description: "The order in which the stage appears in HubSpot."

      - name: "closedWon"
        type: "boolean"
        description: "Indicates if this stage marks a deal as closed won."        

  - name: "label"
    type: "string"
    description: "The human-readable label for the pipeline."

  - name: "active"
    type: "boolean"
    description: "Indicates if the pipeline is currently in use."

  - name: "displayOrder"
    type: "integer"
    description: "The order in which the pipeline appears in HubSpot."
---