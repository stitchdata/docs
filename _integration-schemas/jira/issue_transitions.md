---
tap: "jira"
version: "1.0"

name: "issue_transitions"
doc-link: https://docs.atlassian.com/jira/REST/ondemand/#api/2/project-getAllProjects
singer-schema: ## link to the JSON schema file in the integration's Singer repo
description: |
  The `issue_transitions` table contains info about the transitions an issue undergoes during its lifecycle. For example: When an issue is opened, it may be a `To Do` item. When work begins, it moves to `In Progress`. Each of these is considered a transition.

  **To replicate data for this table**, the `issues` table must be selected. Additionally, JIRA's API will only return transitions that are available for the [user whose credentials authenticated the integration](#add-stitch-data-source).

replication-method: "Incremental"

api-method:
  name: 
  doc-link: 

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The issue transition ID."

  - name: "updated"
    type: "date-time"
    replication-key: true
    description: "The date the issue transition was last updated."

  - name: "isConditional"
    type: "boolean"
    description: "If `true`, "

  - name: "isGlobal"
    type: "boolean"
    description: "If `true`, "

  - name: "isInitial"
    type: "boolean"
    description: "If `true`, "

  - name: "issueId"
    type: "string"
    description: "The ID of the issue the transition is associated with."
    foreign-key: true

  - name: "name"
    type: "string"
    description: "The name of the issue. For example: `Close Issue`"

  - name: "to"
    type: "object"
    description: "Details about the issue transition and status category."
    object-attributes:
      - name: "id"
        type: "string"
        description: "The transition action ID."

      - name: "description"
        type: "string"
        description: "A description of the transition action."

      - name: "iconUrl"
        type: "string"
        description: "The URL of the icon associated with the transition action."

      - name: "name"
        type: "string"
        description: "The name of the transition action. For example: `To Do`"

      - name: "self"
        type: "string"
        description: "The API URL of the transition action in JIRA."

      - name: "statusCategory"
        type: "object"
        description: "Details about the status category."
        object-attributes:
          - name: "id"
            type: "integer"
            description: "The status category ID."

          - name: "colorName"
            type: "string"
            description: "The name of the color associated with the status category. For example: `grey`"

          - name: "key"
            type: "string"
            description: "The status category key."

          - name: "name"
            type: "string"
            description: "The name of the status category."

          - name: "self"
            type: "string"
            description: "The API URL of the status category in JIRA."
---