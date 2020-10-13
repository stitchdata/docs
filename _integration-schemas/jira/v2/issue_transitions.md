---
tap: "jira"
version: "2"
key: "issue-transition"

name: "issue_transitions"
doc-link: "https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-api-2-issue-issueIdOrKey-transitions-get"
singer-schema: "https://github.com/singer-io/tap-jira/blob/master/tap_jira/schemas/issue_transitions.json"
description: |
  The `{{ table.name }}` table contains info about issue transitions.

  #### Replication requirements {#replication-requirements-issue-transitions}

  To replicate this data:

  1. The [`issues`](#issues) table must also be set to replicate. **Note**: When an issue is updated, all the transitions for that issue will also be replicated.
   2. The `Browse Projects` [project {{ integration.display_name }} permission]({{ integration.project-permissions-doc }}){:target="new"} is required. Refer to [{{ integration.display_name }}'s API documentation]({{ table.doc-link }}){:target="new"} for more info.

replication-method: "Key-based Incremental"

loading-behavior: "Append-Only"

replication-key:
  name: "issues.updated"

api-method:
    name: "Get issue transitions"
    doc-link: "https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-api-2-issue-issueIdOrKey-transitions-get"
    
attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The issue transition ID."
    # foreign-key-id: "issue-transition-id"

  - name: "expand"
    type: "string"
    description: "Details of expands available for the transition."

  - name: "fields"
    type: "object"
    description: "Details of the fields associated with the issue transition screen."
    subattributes:
      - name: "anyFieldAtAll"
        type: "object"
        description: ""
        subattributes:
          - name: "allowedValues"
            type: "array"
            description: "The list of values allowed in the field."
            subattributes:
              - name: "value"
                type: "varies"
                description: "The value allowed in the field."

          - name: "autoCompleteUrl"
            type: "string"
            description: "The URL that can be used to automatically complete the field."

          - name: "defaultValue"
            type: "anything"
            description: "The default value of the field."

          - name: "hasDefaultValue"
            type: "boolean"
            description: "Indicates whether the field has a default value."

          - name: "key"
            type: "string"
            description: "The key of the field."

          - name: "name"
            type: "string"
            description: "The name of the field."

          - name: "operations"
            type: "array"
            description: "A list of operations that can be performed on the field."
            subattributes:
              - name: "value"
                type: "string"
                description: "The operation that can be performed on the field."

          - name: "required"
            type: "boolean"
            description: "Indicates whether the field is required."

          - name: "schema"
            type: "object"
            description: "The data type of the field."
            subattributes:
              - name: "custom"
                type: "string"
                description: "If the field is a custom field, the URI of the field."

              - name: "customId"
                type: "integer"
                description: "If the field is a custom field, the ID of the custom field."

              - name: "items"
                type: "string"
                description: "When the data type is `array`, the name of the field items within the array."

              - name: "system"
                type: "string"
                description: "If the field is a system field, the name of the field."

              - name: "type"
                type: "string"
                description: "The data type of the field."

  - name: "hasScreen"
    type: "boolean"
    description: "Indicates whether there is a screen associated with the issue transition."

  - name: "isConditional"
    type: "boolean"
    description: "Indicates whether the issue has to meet certain criteria before the issue transition can be applied."

  - name: "isGlobal"
    type: "boolean"
    description: "Indicates whether the issue transition is global, meaning the transition can be applied to issues regardless of status."

  - name: "isInitial"
    type: "boolean"
    description: "Indicates whether this is the initial issue transition for the workflow."

  - name: "issueId"
    type: "string"
    description: "The ID of the issue associated with the transition."
    foreign-key-id: "issue-id"

  - name: "name"
    type: "string"
    description: "The name of the issue transition."

  - name: "to"
    type: "object"
    description: "Details of the issue status after the transition."
    subattributes:
      - name: "description"
        type: "string"
        description: "The description of the transition status."

      - name: "iconUrl"
        type: "string"
        description: "The URL of the transition status icon."

      - name: "id"
        type: "string"
        description: "The ID of the transition status."

      - name: "name"
        type: "string"
        description: "The name of the transition status."

      - name: "self"
        type: "string"
        description: "The URL of the transition status."

      - name: "statusCategory"
        type: "object"
        description: "The category assigned to the transition status."
        subattributes:
          - name: "colorName"
            type: "string"
            description: "The name of the color used to represent the status category."

          - name: "id"
            type: "integer"
            description: "The ID of the status category."

          - name: "key"
            type: "string"
            description: "The key of the status category."

          - name: "name"
            type: "string"
            description: "The name of the status category."

          - name: "self"
            type: "string"
            description: "The URL of the status category."

      - name: "statusColor"
        type: "string"
        description: "The name of the color of the transition status."
---
