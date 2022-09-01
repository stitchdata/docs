---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "github"
version: "2"
key: "issue-milestone"

name: "issue_milestones"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/issue_milestones.json"
description: |
  The `{{ table.name }}` table contains info about issue milestones in the repositories specified for the integration.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "List milestones"
  doc-link: "https://docs.github.com/en/rest/reference/issues#list-milestones"

replication-method: "Key-based Incremental"
replication-key:
  name: "since"
  based-on: "due_on"
  tooltip: "This is a query parameter used to extract new/updated data from GitHub. It will not be included in the table's fields."


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "id"
    type: "number"
    primary-key: true
    description: "The issue milestone ID."
    foreign-key-id: "issue-milestone-id"

  - name: "_sdc_repository"
    type: "string"
    description: ""

  - name: "closed_at"
    type: "date-time"
    description: ""

  - name: "closed_issues"
    type: "number"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "creator"
    type: "object"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: "The name of the user."
        
      - name: "email"
        type: "string"
        description: "The email address of the user."

      - name: "login"
        type: "string"
        description: "The login name of the user."

      - name: "id"
        type: "string"
        description: "The ID of the user."

      - name: "node_id"
        type: "string"
        description: "The node ID of the user."

      - name: "avatar_url"
        type: "string"
        description: "The URL of the avatar of the user."

      - name: "gravatar_id"
        type: "string"
        description: "The URL of the Gravatar of the user."

      - name: "url"
        type: "string"
        description: "The API URL of the user."

      - name: "html_url"
        type: "string"
        description: "The GitHub URL of the user."

      - name: "followers_url"
        type: "string"
        description: "The URL to the user's followers page."

      - name: "following_url"
        type: "string"
        description: "The URL to the user's following page."

      - name: "gists_url"
        type: "string"
        description: "The URL to the user's gists page."

      - name: "starred_url"
        type: "string"
        description: "The URL to the user's starred page."

      - name: "subscriptions_url"
        type: "string"
        description: "The URL to the user's subscriptions page."

      - name: "organizations_url"
        type: "string"
        description: "The URL to the user's organizations page."

      - name: "repos_url"
        type: "string"
        description: "The URL to the user's repositories page."

      - name: "events_url"
        type: "string"
        description: "The URL to the user's events page."

      - name: "received_events_url"
        type: "string"
        description: "The URL to the user's received events page."

      - name: "type"
        type: "string"
        description: "The type of the user."

      - name: "site_admin"
        type: "string"
        description: "Indicates if the user is a site administrator."
        
      - name: "starred_at"
        type: "string"
        description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "due_on"
    type: "date-time"
    description: ""

  - name: "html_url"
    type: "string"
    description: ""

  - name: "labels_url"
    type: "string"
    description: ""

  - name: "node_id"
    type: "string"
    description: ""

  - name: "number"
    type: "number"
    description: ""

  - name: "open_issues"
    type: "number"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "updated_at"
    type: "date-time"
    description: ""

  - name: "url"
    type: "string"
    description: ""
---