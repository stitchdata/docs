---
tap: "jira"
version: "1.0"

name: "roles"
doc-link: https://developer.atlassian.com/cloud/jira/platform/rest/#api/2/role-getProjectRoles
singer-schema: https://github.com/singer-io/tap-jira/blob/master/tap_jira/schemas/roles.json
description: |
  The `roles` table contains info about the roles that can be assigned to projects in your JIRA account.

replication-method: "Full Table"
api-method:
  name: getProjectRoles
  doc-link: https://developer.atlassian.com/cloud/jira/platform/rest/#api/2/role-getProjectRoles

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The role ID."

  - name: "self"
    type: "string"
    description: "The URL associated with the role."

  - name: "name"
    type: "string"
    description: "The name of the role."

  - name: "description"
    type: "string"
    description: "The description of the role."

  - name: "actors"
    type: "array"
    description: "Details about the actors associated with the role."
    array-attributes:
      - name: "id"
        type: "integer"
        description: "The role actor ID."

      - name: "displayName"
        type: "string"
        description: "The role actor display name."

      - name: "type"
        type: "string"
        description: "The role actor type."

      - name: "name"
        type: "string"
        description: "The name of the role actor."

      - name: "avatarUrl"
        type: "string"
        description: "The URL for the avatar associated with the role actor."

---