---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "github"
version: "2"
key: "commit-comment"

name: "commit_comments"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/commit_comments.json"
description: |
  The `{{ table.name }}` table contains info about the commit comments in the repositories specified for the integration.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "List commit comments for a repository"
  doc-link: "https://docs.github.com/en/rest/reference/repos#list-commit-comments-for-a-repository"

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
    type: "number"
    primary-key: true
    description: "The commit comment ID."
    foreign-key-id: "commit-comment-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "body"
    type: "string"
    description: ""

  - name: "commit_id"
    type: "string"
    description: ""
    foreign-key-id: "commit-id"

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "html_url"
    type: "string"
    description: ""

  - name: "line"
    type: "number"
    description: ""

  - name: "node_id"
    type: "string"
    description: ""

  - name: "path"
    type: "string"
    description: ""

  - name: "position"
    type: "number"
    description: ""

  - name: "url"
    type: "string"
    description: ""

  - name: "user"
    type: "object"
    description: "Details about the user who created the comment."
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

  - name: "author_association"
    type: "string"
    description: ""

  - name: "reactions"
    type: "object, string"
    description: ""
    subattributes:
      - name: "url"
        type: "string"
        description: ""
        
      - name: "total_count"
        type: "integer"
        description: ""
        
      - name: "+1"
        type: "integer"
        description: ""
        
      - name: "-1"
        type: "integer"
        description: ""
        
      - name: "laugh"
        type: "integer"
        description: ""
        
      - name: "confused"
        type: "integer"
        description: ""
        
      - name: "heart"
        type: "integer"
        description: ""
        
      - name: "hooray"
        type: "integer"
        description: ""
        
      - name: "eyes"
        type: "integer"
        description: ""
        
      - name: "rocket"
        type: "integer"
        description: ""
---