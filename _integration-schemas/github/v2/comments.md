---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "github"
version: "2"
key: "comment"

name: "comments"
doc-link: https://developer.github.com/v3/comments/
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/comments.json
description: |
  The `{{ table.name }}` table contains info about comments made on issues in the repositories specified for the integration.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "List issue comments for a repository"
  doc-link: "https://docs.github.com/en/rest/reference/issues#list-issue-comments-for-a-repository"

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
    type: "integer"
    primary-key: true
    description: "The comment ID."
    # foreign-key-id: "comment-id"

  - name: "author_association"
    type: "string"
    description: ""

  - name: "body"
    type: "string"
    description: "The body of the comment."

  - name: "created_at"
    type: "date-time"
    description: "The time the comment was created."

  - name: "home_url"
    type: "string"
    description: "The home URL of the comment."

  - name: "html_url"
    type: "string"
    description: "The HTML URL of the comment."

  - name: "issue_url"
    type: "string"
    description: "The URL of the issue associated with the comment."

  - name: "node_id"
    type: "string"
    description: "The node ID."

  - name: "_sdc_repository"
    type: "string"
    description: ""

  - name: "updated_at"
    type: "date-time"
    description: "The time the comment was last updated."

  - name: "url"
    type: "string"
    description: "The GitHub URL of the comment."

  - name: "user"
    type: "object"
    description: "Details about the user who created the comment."
    subattributes:
      - name: "login"
        type: "string"
        description: "The login name of the user who created the comment."

      - name: "id"
        type: "string"
        description: "The ID of the user who created the comment."

      - name: "node_id"
        type: "string"
        description: "The node ID of the user who created the comment."

      - name: "avatar_url"
        type: "string"
        description: "The URL of the avatar of the user who created the comment."

      - name: "gravatar_id"
        type: "string"
        description: "The URL of the Gravatar of the user who created the comment."

      - name: "url"
        type: "string"
        description: "The API URL of the user who created the comment."

      - name: "html_url"
        type: "string"
        description: "The GitHub URL of the user who created the comment."

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
---