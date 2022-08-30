---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "github"
version: "2"
key: "pull-request"

name: "pull_requests"
doc-link: https://developer.github.com/v3/pulls/
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/pull_requests.json
description: |
  The `{{ table.name }}` table contains info about pull requests made against the repositories specified for the integration.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "List pull requests"
  doc-link: "https://docs.github.com/en/rest/reference/pulls#list-pull-requests"

replication-method: "Key-based Incremental"
replication-key:
  name: "since"
  based-on: "updated_at"
  tooltip: "This is a query parameter used to extract new/updated data from GitHub. It will not be included in the table's fields."

# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The pull request ID."
    foreign-key-id: "pull-request-id"

  - name: "_sdc_repository"
    type: "string"
    description: ""

  - name: "base"
    type: "object"
    description: "Details about the base branch."
    subattributes:
      - name: "ref"
        type: "string"
        description: ""

      - name: "label"
        type: "string"
        description: ""

      - name: "repo"
        type: "object"
        description: ""
        subattributes:
          - name: "id"
            type: "integer"
            description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "url"
            type: "string"
            description: ""

      - name: "sha"
        type: "string"
        description: ""

  - name: "body"
    type: "string"
    description: "The description of the pull request."

  - name: "closed_at"
    type: "string"
    description: "The time the pull request was closed."

  - name: "created_at"
    type: "string"
    description: "The time the pull request was created."

  - name: "labels"
    type: "array"
    description: ""
    subattributes:
      - name: "color"
        type: "string"
        description: ""
        
      - name: "default"
        type: "boolean"
        description: ""

      - name: "description"
        type: "string"
        description: ""

      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "issue-label-id"

      - name: "name"
        type: "string"
        description: ""

      - name: "node_id"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

  - name: "merged_at"
    type: "string"
    description: "The time the pull request was merged."

  - name: "number"
    type: "integer"
    description: "The number of the pull request in the repository."

  - name: "state"
    type: "string"
    description: "The current status of the pull request. For example: `open`"

  - name: "title"
    type: "string"
    description: "The title of the pull request."

  - name: "updated_at"
    type: "date-time"
    description: "The last time the pull request was updated."

  - name: "url"
    type: "string"
    description: "The URL to the pull request."

  - name: "user"
    type: "object"
    description: "Details about the user who created the pull request."
    subattributes:
      - name: "id"
        type: "integer"
        description: "The user ID."
        foreign-key-id: "collaborator-id"

      - name: "login"
        type: "string"
        description: "The user's GitHub username."
---