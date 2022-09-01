---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "github"
version: "2"
key: "assignee"

name: "assignees"
doc-link: https://developer.github.com/v3/issues/assignees/
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/assignees.json
description: |
  The `{{ table.name }}` table contains info about the available assignees for issues in the repositories specified for the integration.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "List assignees"
  doc-link: "https://docs.github.com/en/rest/reference/issues#list-assignees"

replication-method: "Full Table"


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The assignee ID."
    # foreign-key-id: "assignee-id"

  - name: "login"
    type: "string"
    description: "The user's username."

  - name: "_sdc_repository"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: "The user's type."

  - name: "url"
    type: "string"
    description: "The profile URL associated with the user."

  - name: "name"
    type: "string"
    description: "The user's name."

  - name: "email"
    type: "string"
    description: "The user's email address."

  - name: "node_id"
    type: "string"
    description: ""

  - name: "avatar_url"
    type: "string"
    description: ""

  - name: "gravatar_id"
    type: "string"
    description: ""

  - name: "html_url"
    type: "string"
    description: ""

  - name: "followers_url"
    type: "string"
    description: ""

  - name: "following_url"
    type: "string"
    description: ""

  - name: "gists_url"
    type: "string"
    description: ""

  - name: "starred_url"
    type: "string"
    description: ""

  - name: "subscriptions_url"
    type: "string"
    description: ""

  - name: "organizations_url"
    type: "string"
    description: ""

  - name: "repos_url"
    type: "string"
    description: ""

  - name: "events_url"
    type: "string"
    description: ""

  - name: "received_events_url"
    type: "string"
    description: ""

  - name: "site_admin"
    type: "boolean"
    description: ""

  - name: "starred_at"
    type: "string"
    description: ""

---