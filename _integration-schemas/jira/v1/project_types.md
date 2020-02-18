---
tap: "jira"
version: "1"
key: "project-type"

name: "project_types"
doc-link: "https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-api-2-project-type-get"
singer-schema: "https://github.com/singer-io/tap-jira/tree/77206190933146b7cf51f14bfc7aaf670539ca5f/tap_jira/schemas/project_types.json"
description: |
  The `{{ table.name }}` table contains info about project types.

replication-method: "Full Table"

api-method:
    name: "Get all project types"
    doc-link: "https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-api-2-project-type-get"
    
attributes:
  - name: "key"
    type: "string"
    primary-key: true
    description: "The project type key."
    # foreign-key-id: "project-type-key"

  - name: "color"
    type: "string"
    description: "The color of the project type."

  - name: "descriptionI18nKey"
    type: "string"
    description: "The key of the project type's description."

  - name: "formattedKey"
    type: "string"
    description: "The formatted key of the project type."

  - name: "icon"
    type: "string"
    description: "The icon associated with the project type."
---