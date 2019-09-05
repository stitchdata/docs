---
tap: "helpscout"
version: "1.0"

key: "workflow"
name: "workflows"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-helpscout/blob/master/tap_helpscout/schemas/workflows.json"
description: |
  The `{{ table.name }}` table contains info about the workflows in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List workflows"
    doc-link: "https://developer.helpscout.com/mailbox-api/endpoints/workflows/list/"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The workflow ID."
    #foreign-key-id: "workflow-id"

  - name: "modified_at"
    type: "date-time"
    replication-key: true
    description: "The UTC time the workflow was last modified."

  - name: "created_at"
    type: "date-time"
    description: "The UTC time the workflow was created."

  - name: "mailbox_id"
    type: "integer"
    description: "The ID of the mailbox the workflow is associated with."
    foreign-key-id: "mailbox-id"

  - name: "name"
    type: "string"
    description: "The name of the workflow."

  - name: "order"
    type: "integer"
    description: "The order of the workflow."

  - name: "status"
    type: "string"
    description: |
      The current status of the workflow. Possible values are:

      - `active`
      - `inactive`
      - `invalid`

  - name: "type"
    type: "string"
    description: "The type of the workflow."
---