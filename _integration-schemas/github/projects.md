---
tap: "github"
version: "1"
key: "project"

name: "projects"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/projects.json"
description: |
  The `{{ table.name }}` table contains info about projects in the repositories specified for the integration. 

replication-method: "Key-based Incremental"

api-method:
  name: "List repository projects"
  doc-link: "https://docs.github.com/en/rest/reference/projects#list-repository-projects"

attributes:
  - name: "id"
    type: "number"
    primary-key: true
    description: "The project ID."
    foreign-key-id: "project-id"

  - name: "body"
    type: "string"
    description: ""

  - name: "columns_url"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "creator"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "number"
        description: ""

      - name: "login"
        type: "string"
        description: ""

  - name: "html_url"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "node_id"
    type: "string"
    description: ""

  - name: "number"
    type: "number"
    description: ""

  - name: "owner_url"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "updated_at"
    type: "date-time"
    description: ""

  - name: "url"
    type: "string"
    description: ""
---