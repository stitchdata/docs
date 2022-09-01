---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "github"
version: "2"
key: "issue"

name: "issues"
doc-link: https://developer.github.com/v3/issues/
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/issues.json
description: |
  The `{{ table.name }}` table contains info about issues in the repositories specified for the integration.

  #### Issues and pull requests

  GitHub's API considers every pull request an issue, but not every issue may be a pull request. Therefore, this table may contain both issues and pull requests.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "List issues for repository"
  doc-link: "https://docs.github.com/en/rest/reference/issues#list-repository-issues"

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
    description: "The issue ID."
    foreign-key-id: "issue-id"

  - name: "_sdc_repository"
    type: "string"
    description: ""

  - name: "assignee"
    type: "object"
    description: ""
    subattributes: &user-attributes
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

  - name: "body"
    type: "string"
    description: ""

  - name: "closed_at"
    type: "date-time"
    description: ""

  - name: "comments"
    type: "integer"
    description: ""

  - name: "comments_url"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "events_url"
    type: "string"
    description: ""

  - name: "html_url"
    type: "string"
    description: ""

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

  - name: "labels_url"
    type: "string"
    description: ""

  - name: "locked"
    type: "boolean"
    description: ""

  - name: "node_id"
    type: "string"
    description: ""

  - name: "number"
    type: "integer"
    description: ""

  - name: "pull_request"
    type: "object"
    description: ""
    subattributes:
      - name: "diff_url"
        type: "string"
        description: ""

      - name: "html_url"
        type: "string"
        description: ""

      - name: "patch_url"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

  - name: "repository_url"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""
    
  - name: "state_reason"
    type: "string"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "updated_at"
    type: "date-time"
    description: "The last time the issue was updated."

  - name: "url"
    type: "string"
    description: ""

  - name: "user"
    type: "object"
    description: ""
    subattributes: *user-attributes  
    
  - name: "assignees"
    type: "array"
    description: ""
    subattributes:
      - name: "items"
        type: "object"
        description: ""
        subattributes: *user-attributes  
      
    
  - name: "milestone"
    type: "object"
    description: ""
    subattributes:
        - name: "url"
          type: "string"
          description: ""
          
        - name: "html_url"
          type: "string"
          description: ""
          
        - name: "labels_url"
          type: "string"
          description: ""
          
        - name: "id"
          type: "integer"
          description: ""
          
        - name: "node_id"
          type: "string"
          description: ""
          
        - name: "number"
          type: "integer"
          description: ""
          
        - name: "state"
          type: "string"
          description: ""
          
        - name: "title"
          type: "string"
          description: ""
          
        - name: "description"
          type: "string"
          description: ""
          
        - name: "creator"
          type: "object"
          description: ""
          subattributes: *user-attributes  
          
        - name: "open_issues"
          type: "integer"
          description: ""
          
        - name: "closed_issues"
          type: "integer"
          description: ""
          
        - name: "created_at"
          type: "string"
          description: ""
          
        - name: "updated_at"
          type: "string"
          description: ""
          
        - name: "closed_at"
          type: "string"
          description: ""
          
        - name: "due_on"
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
    
  - name: "active_lock_reason"
    type: "string"
    description: ""
    
  - name: "body_html"
    type: "string"
    description: ""
    
  - name: "performed_via_github_app"
    type: "object, string"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
        
      - name: "slug"
        type: "string"
        description: ""
        
      - name: "node_id"
        type: "string"
        description: ""
        
      - name: "owner"
        type: "object"
        description: ""
        subattributes: *user-attributes
        
      - name: "name"
        type: "string"
        description: ""
        
      - name: "description"
        type: "string"
        description: ""
        
      - name: "external_url"
        type: "string"
        description: ""
        
      - name: "html_url"
        type: "string"
        description: ""
        
      - name: "created_at"
        type: "string"
        description: ""
        
      - name: "updated_at"
        type: "string"
        description: ""
        
      - name: "permissions"
        type: "object"
        description: ""
        subattributes:
        
      - name: "events"
        type: "array"
        description: ""
        subattributes:
          - name: "item"
            type: "string"
            description: ""
        
      - name: "installations_count"
        type: "integer"
        description: ""
        subattributes:
          - name: "issues"
            type: "string"
            description: ""
            
          - name: "checks"
            type: "string"
            description: ""
            
          - name: "metadata"
            type: "string"
            description: ""
            
          - name: "contents"
            type: "string"
            description: ""
            
          - name: "deployments"
            type: "string"
            description: ""
        
      - name: "client_id"
        type: "string"
        description: ""
        
      - name: "client_secret"
        type: "string"
        description: ""
        
      - name: "webhook_secret"
        type: "string"
        description: ""
        
      - name: "pem"
        type: "string"
        description: ""s
    
  - name: "timeline_url"
    type: "string"
    description: ""
    
  - name: "closed_by"
    type: "object"
    description: ""
    subattributes: *user-attributes

  - name: "body_text"
    type: "string"
    description: ""
    
  - name: "draft"
    type: "boolean"
    description: ""
---