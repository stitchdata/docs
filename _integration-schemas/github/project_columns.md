---
tap: "github"
version: "1"
key: "project-column"

name: "project_columns"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/project_columns.json"
description: |
  The `{{ table.name }}` table contains info about the columns of projects in the repositories specified for the integration.

  **Note**: In order to replicate this table, you must also set the [`projects`](#projects) table to replicate.

replication-method: "Key-based Incremental"
replication-key:
  name: "since"
  based-on: "updated_at"
  tooltip: "This is a query parameter used to extract new/updated data from GitHub. It will not be included in the table's fields."

dependent-on: "projects"

api-method:
  name: "List project columns"
  doc-link: "https://docs.github.com/en/rest/reference/projects#list-project-columns"

attributes:
  - name: "id"
    type: "number"
    primary-key: true
    description: "The project column ID."
    foreign-key-id: "project-column-id"

  - name: "_sdc_repository"
    type: "string"
    description: ""

  - name: "cards_url"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "node_id"
    type: "string"
    description: ""

  - name: "project_url"
    type: "string"
    description: ""

  - name: "updated_at"
    type: "date-time"
    description: ""

  - name: "url"
    type: "string"
    description: ""
---