---
tap: "jira"
version: "2"
key: "component"

name: "components"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-jira/blob/master/tap_jira/schemas/components.json"
description: |
  The `{{ table.name }}` table contains info about components in projects in your {{ integration.display_name }} account.

  #### Replication requirements

  **Note**: To replicate this data:

     1. The [`projects`](#projects) table must also be set to replicate, and
     2. The `Browse Projects` [project {{ integration.display_name }} permission]({{ integration.project-permissions-doc }}){:target="new"} is required. Refer to [{{ integration.display_name }}'s API documentation]({{ table.doc-link }}){:target="new"} for more info.

replication-method: "Full Table"

api-method:
  name: "Get project components paginated"
  doc-link: "https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-project-components/#api-rest-api-2-project-projectidorkey-component-get"
avatar-urls: &avatarUrls
  name: "avatarUrls"
  type: "object"
  description: ""
  subattributes:
    - name: "16x16"
      type: "string"
      description: ""

    - name: "24x24"
      type: "string"
      description: ""

    - name: "32x32"
      type: "string"
      description: ""

    - name: "48x48"
      type: "string"
      description: ""

attributes:
  - name: "id"
    type: "string"
    description: "The component ID."
    primary-key: true
    foreign-key-id: "component-id"

  - name: "assignee"
    type: "object"
    description: ""
    subattributes:
      - name: "accountId"
        type: "string"
        description: ""
        foreign-key-id: "user-id"

      - name: "active"
        type: "boolean"
        description: ""

      - <<: *avatarUrls
        
      - name: "displayName"
        type: "string"
        description: ""

      - name: "self"
        type: "string"
        description: ""

  - name: "assigneeType"
    type: "string"
    description: ""

  - name: "componentBean"
    type: "object"
    description: ""
    subattributes:
      - name: "assignee"
        type: "object"
        description: ""
        subattributes:
          - name: "accountId"
            type: "string"
            description: ""
            foreign-key-id: "user-id"

          - name: "active"
            type: "boolean"
            description: ""

          - <<: *avatarUrls

          - name: "displayName"
            type: "string"
            description: ""

          - name: "self"
            type: "string"
            description: ""

      - name: "assigneeType"
        type: "string"
        description: ""

      - name: "description"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "isAssigneeTypeValid"
        type: "boolean"
        description: ""

      - name: "lead"
        type: "object"
        description: ""
        subattributes:
          - name: "accountId"
            type: "string"
            description: ""
            foreign-key-id: "user-id"

          - name: "active"
            type: "boolean"
            description: ""

          - <<: *avatarUrls

          - name: "displayName"
            type: "string"
            description: ""

          - name: "self"
            type: "string"
            description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "project"
        type: "string"
        description: ""

      - name: "projectId"
        type: "integer"
        description: ""
        foreign-key-id: "project-id"

      - name: "realAssignee"
        type: "object"
        description: ""
        subattributes:
          - name: "accountId"
            type: "string"
            description: ""
            foreign-key-id: "user-id"

          - name: "active"
            type: "boolean"
            description: ""

          - <<: *avatarUrls

          - name: "displayName"
            type: "string"
            description: ""

          - name: "self"
            type: "string"
            description: ""

      - name: "realAssigneeType"
        type: "string"
        description: ""

      - name: "self"
        type: "string"
        description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "isAssigneeTypeValid"
    type: "boolean"
    description: ""

  - name: "issueCount"
    type: "integer"
    description: ""

  - name: "lead"
    type: "object"
    description: ""
    subattributes:
      - name: "accountId"
        type: "string"
        description: ""
        foreign-key-id: "user-id"

      - name: "active"
        type: "boolean"
        description: ""

      - <<: *avatarUrls

      - name: "displayName"
        type: "string"
        description: ""

      - name: "self"
        type: "string"
        description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "project"
    type: "string"
    description: ""

  - name: "projectId"
    type: "integer"
    description: ""
    foreign-key-id: "project-id"

  - name: "realAssignee"
    type: "object"
    description: ""
    subattributes:
      - name: "accountId"
        type: "string"
        description: ""
        foreign-key-id: "user-id"

      - name: "active"
        type: "boolean"
        description: ""

      - <<: *avatarUrls

      - name: "displayName"
        type: "string"
        description: ""

      - name: "self"
        type: "string"
        description: ""

  - name: "realAssigneeType"
    type: "string"
    description: ""

  - name: "self"
    type: "string"
    description: ""
---