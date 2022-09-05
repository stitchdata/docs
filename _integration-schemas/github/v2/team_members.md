---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "github"
version: "2"
key: "team-member"

name: "team_members"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/team_members.json"
description: |
  The `{{ table.name }}` table contains info about members of organization teams that are visible to the user who authorized the integration.
  

# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "List teams"
  doc-link: "https://docs.github.com/en/rest/reference/teams#list-team-members"

replication-method: "Full Table"
replication-key:
  name: "since"
  tooltip: "This is a query parameter used to extract new/updated data from GitHub. It will not be included in the table's fields."


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "id"
    type: "number"
    primary-key: true
    description: "The team member's ID."
    foreign-key-id: "team-member-id"

  - name: "_sdc_repository"
    type: "string"
    description: ""

  - name: "avatar_url"
    type: "string"
    description: ""

  - name: "events_url"
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

  - name: "gravatar_id"
    type: "string"
    description: ""

  - name: "html_url"
    type: "string"
    description: ""

  - name: "login"
    type: "string"
    description: ""

  - name: "node_id"
    type: "string"
    description: ""

  - name: "organizations_url"
    type: "string"
    description: ""

  - name: "received_events_url"
    type: "string"
    description: ""

  - name: "repos_url"
    type: "string"
    description: ""

  - name: "site_admin"
    type: "boolean"
    description: ""

  - name: "starred_url"
    type: "string"
    description: ""

  - name: "subscriptions_url"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "url"
    type: "string"
    description: ""
         
  - name: "name"
    type: "string"
    description: ""
         
  - name: "email"
    type: "string"
    description: ""
         
  - name: "starred_at"
    type: "string"
    description: ""
---