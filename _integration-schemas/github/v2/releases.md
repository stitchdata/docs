---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "github"
version: "2"
key: "release"

name: "releases"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/releases.json"
description: |
  The `{{ table.name }}` table contains info about releases in the repositories specified for the integration.

  **Note**: {{ integration.display_name }} doesn't include regular Git tags that haven't been associated with a release.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "List releases"
  doc-link: "https://docs.github.com/en/rest/reference/repos#list-releases"

replication-method: "Full Table"


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The release ID."
    # foreign-key-id: "release-id"

  - name: "_sdc_repository"
    type: "string"
    description: ""

  - name: "author"
    type: "object"
    description: "Details about the author of the release."
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

  - name: "body"
    type: "string"
    description: "The text describing the tag."

  - name: "created_at"
    type: "date-time"
    description: "The date the release was created."

  - name: "draft"
    type: "boolean"
    description: "If `TRUE`, the release is a draft release."

  - name: "html_url"
    type: "string"
    description: "The HTML URL to the release." 

  - name: "name"
    type: "string"
    description: "The name of the release."

  - name: "prerelease"
    type: "boolean"
    description: "If `TRUE`, the release is a pre-release."

  - name: "published_at"
    type: "date-time"
    description: "The date the release was published."

  - name: "tag_name"
    type: "string"
    description: "The name of the tag."

  - name: "target_commitish"
    type: "string"
    description: "The commitish value that determines where the Git tag was created."

  - name: "node_id"
    type: "string"
    description: ""
    
  - name: "url"
    type: "string"
    description: ""
    
  - name: "zipball_url"
    type: "string"
    description: ""
    
  - name: "body_text"
    type: "string"
    description: ""
    
  - name: "upload_url"
    type: "string"
    description: ""
    
  - name: "assets_url"
    type: "string"
    description: ""
    
  - name: "tarball_url"
    type: "string"
    description: ""
    
  - name: "body_html"
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
    
  - name: "assets"
    type: "array"
    description: ""
    subattributes: 
        - name: "url"
          type: "string"
          description: ""
          
        - name: "browser_download_url"
          type: "string"
          description: ""
          
        - name: "id"
          type: "integer"
          description: ""
          
        - name: "node_id"
          type: "string"
          description: ""
          
        - name: "name"
          type: "string"
          description: ""
          
        - name: "label"
          type: "string"
          description: ""
          
        - name: "state"
          type: "string"
          description: ""
          
        - name: "content_type"
          type: "string"
          description: ""
          
        - name: "size"
          type: "integer"
          description: ""
          
        - name: "download_count"
          type: "integer"
          description: ""
          
        - name: "created_at"
          type: "string"
          description: ""  
          
        - name: "updated_at"
          type: "string"
          description: ""  
          
        - name: "uploader"
          type: "object"
          description: ""
          subattributes:
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

  - name: "mentions_count"
    type: "integer"
    description: ""
    
  - name: "discussion_url"
    type: "string"
    description: ""
---