---
tap: "github"
version: "1"
key: "team"

name: "teams"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/teams.json"
description: |
  The `{{ table.name }}` table contains info about the teams in an organization.

  **Note**: Only teams that are visible to the user who authorized the integration in Stitch will be replicated.

replication-method: "Key-based Incremental"

api-method:
  name: "List teams"
  doc-link: "https://docs.github.com/en/rest/reference/teams#list-teams"

attributes:
  - name: "id"
    type: "number"
    primary-key: true
    description: "The team ID."
    foreign-key-id: "team-id"

  - name: "_sdc_repository"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "html_url"
    type: "string"
    description: ""

  - name: "members_url"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "node_id"
    type: "string"
    description: ""

  - name: "parent"
    type: "string"
    description: ""

  - name: "permission"
    type: "string"
    description: ""

  - name: "privacy"
    type: "string"
    description: ""

  - name: "repositories_url"
    type: "string"
    description: ""

  - name: "slug"
    type: "string"
    description: ""

  - name: "url"
    type: "string"
    description: ""
---