---
tap: "jira"
version: "1.0"

name: "project_categories"
doc-link: https://docs.atlassian.com/jira/REST/cloud/#api/2/projectCategory-getAllProjectCategories
singer-schema: https://github.com/singer-io/tap-jira/blob/master/tap_jira/schemas/project_categories.json
description: |
  The `project_categories` table contains info about the categories assigned to the projects in your JIRA account.

replication-method: "Full Table"

api-method:
  name: getAllProjectCategories
  doc-link: https://docs.atlassian.com/jira/REST/cloud/#api/2/projectCategory-getAllProjectCategories

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The project category ID."

  - name: "self"
    type: "string"
    description: "The URL associated with the project category."

  - name: "name"
    type: "string"
    description: "The name of the project category."

  - name: "description"
    type: "string"
    description: "The description of the project category."
---