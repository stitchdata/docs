---
tap: "hubspot"
version: "2.0"

name: "workflows"
doc-link: https://developers.hubspot.com/docs/methods/workflows/workflows_overview
singer-schema: https://github.com/singer-io/tap-hubspot/blob/master/tap_hubspot/schemas/workflows.json
description: |
  The `workflows` table contains info about the workflows in your HubSpot portal.

replication-method: "Key-based Incremental"
api-method:
  name: getWorkflows
  doc-link: https://developers.hubspot.com/docs/methods/workflows/v3/get_workflows

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the workflow."
    # foreign-key-id: "workflow-id"

  - name: "updatedAt"
    type: "date-time"
    replication-key: true
    description: "The time that the workflow was last updated."

  - name: "name"
    type: "string"
    description: "The name of the workflow."

  - name: "type"
    type: "string"
    description: "The type of workflow. For example: `DRIP_DELAY`"

  - name: "enabled"
    type: "boolean"
    description: "Indicates if the workflow is enabled in your HubSpot portal."

  - name: "inserted-at"
    type: "date-time"
    description: "The time that the workflow was inserted."

  - name: "personaTagIds"
    type: "array"
    description: "Info about the personas tied to the workflow."
    array-attributes:
      - name: "value"
        type: "integer"
        description: "The ID of the persona tied to the workflow."

  - name: "contactListIds"
    type: "object"
    description: "Summary info for the contact lists associated with the workflow."
    object-attributes:
      - name: "enrolled"
        type: "integer"
        description: "The number of contacts currently enrolled in the workflow."

      - name: "active"
        type: "integer"
        description: "The number of active contacts for the workflow."

      - name: "steps"
        type: "array"
        description: "Details about the steps in the workflow for the contact list."
        array-attributes:
          - name: "type"
            type: "string"
            description: "The type of step in the workflow." 
---