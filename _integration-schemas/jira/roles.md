---
tap: "jira"
version: "1.0"

name: "roles"
doc-link: "https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-api-2-role-get"
singer-schema: "https://github.com/singer-io/tap-jira/blob/master/tap_jira/schemas/roles.json"
description: |
  The `{{ table.name }}` table contains info about the project roles in your {{ integration.display_name }} account.

  **Note**: To replicate this data, the `Administer {{ integration.display_name }}` [global {{ integration.display_name }} permission]({{ integration.global-permissions-doc }}){:target="new"} is required. Refer to [{{ integration.display_name }}'s API documentation]({{ table.doc-link }}){:target="new"} for more info.

replication-method: "Full Table"

api-method:
    name: "Get project roles"
    doc-link: "https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-api-2-role-get"
    
attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The project role ID."
    # foreign-key-id: "role-id"

  - name: "actors"
    type: "array"
    description: "Details about the user assigned this project role."
    array-attributes:
      - name: "avatarUrl"
        type: "string"
        description: "The URL of the user's avatar."

      - name: "displayName"
        type: "string"
        description: "The display name of the user. Depending on the user's privacy setting, this may be returned as null."

      - name: "id"
        type: "integer"
        description: "The user's ID."

      - name: "name"
        type: "string"
        description: "The name of the user."

      - name: "type"
        type: "string"
        description: "The type of the user."

  - name: "description"
    type: "string"
    description: "The description of the project role."

  - name: "name"
    type: "string"
    description: "The name of the project role."

  - name: "self"
    type: "uri"
    description: "The URL of the project role."
---