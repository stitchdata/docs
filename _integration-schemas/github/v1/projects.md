---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "github"
version: "1"
key: "project"

name: "projects"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/projects.json"
description: |
  The `{{ table.name }}` table contains info about projects in the repositories specified for the integration. 


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "List repository projects"
  doc-link: "https://docs.github.com/en/rest/reference/projects#list-repository-projects"

replication-method: "Key-based Incremental"
replication-key:
  name: "since"
  based-on: "updated_at"
  tooltip: "This is a query parameter used to extract new/updated data from GitHub. It will not be included in the table's fields."

is-parent-table: true


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

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