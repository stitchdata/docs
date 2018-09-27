---
tap: "github"
# version: ""

name: "pull_requests"
doc-link: https://developer.github.com/v3/pulls/
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/pull_requests.json
description: |
  The `pull_requests` table contains info about pull requests made against the repository.

replication-method: "Full Table"

api-method:
  name: "listPullRequests"
  doc-link: https://developer.github.com/v3/pulls/#list-pull-requests

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The pull request ID."
    foreign-key-id: "pull-request-id"

  - name: "updated_at"
    type: "date-time"
    description: "The last time the pull request was updated."

  - name: "body"
    type: "string"
    description: "The description of the pull request."

  - name: "closed_at"
    type: "string"
    description: "The time the pull request was closed."

  - name: "created_at"
    type: "string"
    description: "The time the pull request was created."

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

  - name: "url"
    type: "string"
    description: "The URL to the pull request."

  - name: "user"
    type: "object"
    description: "Details about the user who created the pull request."
    object-attributes:
      - name: "id"
        type: "integer"
        description: "The user ID."
        foreign-key-id: "collaborator-id"

      - name: "login"
        type: "string"
        description: "The user's GitHub username."
---