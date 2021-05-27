---
tap: "github"
version: "1"
key: "issue-label"

name: "issue_labels"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/issue_labels.json"
description: |
  The `{{ table.name }}` table contains info about issue labels in the repositories specified for the integration.

replication-method: "Key-based Incremental"
replication-key:
  name: "since"
  tooltip: "This is a query parameter used to extract new/updated data from GitHub. It will not be included in the table's fields."

api-method:
  name: "List labels for a repository"
  doc-link: "https://docs.github.com/en/rest/reference/issues#list-labels-for-a-repository"

attributes:
  - name: "id"
    type: "number"
    primary-key: true
    description: "The issue label ID."
    foreign-key-id: "label-id"

  - name: "_sdc_repository"
    type: "string"
    description: ""

  - name: "color"
    type: "string"
    description: ""

  - name: "default"
    type: "boolean"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "node_id"
    type: "string"
    description: ""

  - name: "url"
    type: "string"
    description: ""
---