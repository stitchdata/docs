---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "github"
version: "2"
key: "commit"

name: "commits"
doc-link:
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/commits.json
description: |
  The `{{ table.name }}` table contains info about repository commits in a project.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "List commits"
  doc-link: "https://docs.github.com/en/rest/reference/repos#list-commits"

replication-method: "Key-based Incremental"
replication-key:
  name: "since"
  tooltip: "This is a query parameter used to extract new/updated data from GitHub. It will not be included in the table's fields."


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "_sdc_repository"
    type: "string"
    description: ""
    
  - name: "node_id"
    type: "string"
    description: ""
    
  - name: "pr_id"
    type: "string"
    description: ""
    
  - name: "pr_number"
    type: "integer"
    description: ""
    
  - name: "id"
    type: "string"
    description: ""
    
  - name: "updated_at"
    type: "date-time"
    description: ""
    
  - name: "sha"
    type: "string"
    description: ""
    primary-key: true
    
  - name: "url"
    type: "string"
    description: ""
    
  - name: "parents"
    type: "array"
    description: ""
    subattributes:
      - name: "items"
        type: "object"
        description: ""
        subattributes:
          - name: "sha"
            type: "string"
            description: ""
          
          - name: "url"
            type: "string"
            description: ""
          
          - name: "html_url"
            type: "string"
            description: ""
          
        
      
    

    
  - name: "html_url"
    type: "string"
    description: ""
    
  - name: "comments_url"
    type: "string"
    description: ""
    
  - name: "commit"
    type: "object"
    description: ""
    subattributes:
      - name: "url"
        type: "string"
        description: ""
        
      - name: "tree"
        type: "object"
        description: ""
        subattributes:
          - name: "sha"
            type: "string"
            description: ""
            
          - name: "url"
            type: "string"
            description: ""
            
          
        
      - name: "author"
        type: "object"
        description: ""
        subattributes: &user-attributes-date
          - name: "name"
            type: "string"
            description: ""
            
          - name: "email"
            type: "string"
            description: ""
            
          - name: "login"
            type: "string"
            description: ""
            
          - name: "id"
            type: "integer"
            description: ""
            
          - name: "node_id"
            type: "string"
            description: ""
            
          - name: "avatar_url"
            type: "string"
            description: ""
            
          - name: "gravatar_id"
            type: "string"
            description: ""
            
          - name: "url"
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
            
          - name: "type"
            type: "string"
            description: ""
            
          - name: "site_admin"
            type: "boolean"
            description: ""
            
          - name: "starred_at"
            type: "string"
            description: ""
            
          - name: "date"
            type: "date-time"
            description: ""
            
          
        
      - name: "message"
        type: "string"
        description: ""
        
      - name: "committer"
        type: "object"
        description: ""
        subattributes: *user-attributes-date
          
      - name: "comment_count"
        type: "integer"
        description: ""
        
      
    
  - name: "committer"
    type: "object"
    description: "Details about the user who committed the change."
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
    
  - name: "author"
    type: "object"
    description: "Details about the author of the commit."
    subattributes: *user-attributes

---