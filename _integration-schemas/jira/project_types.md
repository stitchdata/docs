---
tap: "jira"
version: "1.0"

name: "project_types"
doc-link: https://docs.atlassian.com/jira/REST/ondemand/#api/2/project/type-getAllProjectTypes
singer-schema: https://github.com/singer-io/tap-jira/blob/master/tap_jira/schemas/project_types.json
description: |
  The `project_types` table contains info about the project types defined in your JIRA account.

replication-method: "Full Table"

api-method:
  name: getAllProjectTypes
  doc-link: https://docs.atlassian.com/jira/REST/ondemand/#api/2/project/type-getAllProjectTypes

attributes:
  - name: "key"
    type: "string"
    primary-key: true
    description: "The project type key."

  - name: "formattedKey"
    type: "string"
    description: "The formatted project type key."

  - name: "descriptionI18Key"
    type: "string"
    description: "The description of the project type."

  - name: "icon"
    type: "string"
    description: "The name of the icon associated with the project type."

  - name: "color"
    type: "string"
    description: "The color associated with the project type."
---