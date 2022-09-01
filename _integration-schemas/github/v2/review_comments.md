---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "github"
version: "2"
key: "review-comment"

name: "review_comments"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/review_comments.json"
description: |
  The `{{ table.name }}` table contains info about comments made on pull request reviews in the repositories specified for the integration.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "List comments on a pull request"
  doc-link: "https://docs.github.com/en/rest/reference/pulls#list-review-comments-on-a-pull-request"

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
    description: "The review comment ID."
    # foreign-key-id: "review-comment-id"

  - name: "updated_at"
    type: "date-time"
    description: "The time the review comment was last updated."

  - name: "assignee"
    type: "string"
    description: ""

  - name: "assignees"
    type: "string"
    description: ""

  - name: "author_association"
    type: "string"
    description: ""

  - name: "base"
    type: "string"
    description: ""

  - name: "body"
    type: "string"
    description: "The body of the review comment."

  - name: "comments_url"
    type: "string"
    description: ""

  - name: "commit_id"
    type: "string"
    description: "The ID of the commit the review comment is associated with."
    foreign-key-id: "commit-id"

  - name: "commits_url"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: "The time the review comment was created."

  - name: "diff_hunk"
    type: "string"
    description: ""

  - name: "diff_url"
    type: "string"
    description: "The diff URL associated with the review comment."

  - name: "head"
    type: "string"
    description: ""

  - name: "html_url"
    type: "string"
    description: "The HTML URL of the review comment."

  - name: "in_reply_to_id"
    type: "integer"
    description: "If the review comment is a reply to another review comment, this will be the ID of the review comment it is in response to."
    foreign-key-id: "review-comment-id"

  - name: "issue_url"
    type: "string"
    description: "The URL of the issue associated with the review comment."

  - name: "labels"
    type: "string"
    description: ""

  - name: "locked"
    type: "string"
    description: ""

  - name: "merge_commit_sha"
    type: "string"
    description: ""

  - name: "milestone"
    type: "string"
    description: ""

  - name: "original_commit_id"
    type: "string"
    description: "The ID of the original comment the review comment is associated with."
    foreign-key-id: "commit-id"  

  - name: "original_position"
    type: "integer"
    description: "The original position of the review comment."

  - name: "patch_url"
    type: "string"
    description: ""

  - name: "path"
    type: "string"
    description: "The path of the file the review comment was made on."

  - name: "position"
    type: "integer"
    description: "The position of the review comment."

  - name: "pull_request_review_id"
    type: "integer"
    description: "The ID of the pull request review the comment is a part of."
    foreign-key-id: "review-id"

  - name: "pull_request_url"
    type: "string"
    description: "The URL of the pull request associated with the review comment."

  - name: "requested_reviewers"
    type: "string"
    description: ""

  - name: "requested_teams"
    type: "string"
    description: ""

  - name: "review_comment_url"
    type: "string"
    description: ""

  - name: "review_comments_url"
    type: "string"
    description: ""

  - name: "statuses_url"
    type: "string"
    description: ""

  - name: "url"
    type: "string"
    description: "The GitHub URL of the review comment."

  - name: "user"
    type: "object"
    description: "Details about the user who created the review comment."
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
    description: ""
    
  - name: "node_id"
    type: "string"
    description: ""
    
  - name: "_links"
    type: "object"
    description: ""
    subattributes:
      - name: "self"
        type: "object"
        description: ""
        subattributes:
          - name: "href"
            type: "string"
            description: ""
            
          
        
      - name: "html"
        type: "object"
        description: ""
        subattributes:
          - name: "href"
            type: "string"
            description: ""
            
          
        
      - name: "pull_request"
        type: "object"
        description: ""
        subattributes:
          - name: "href"
            type: "string"
            description: ""
            
          
        
      
    
  - name: "url"
    type: "string"
    description: ""
    
  - name: "original_start_line"
    type: "integer"
    description: ""
    
  - name: "start_side"
    type: "string"
    description: ""
    
  - name: "body_text"
    type: "string"
    description: ""
    
  - name: "original_line"
    type: "integer"
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
    
  - name: "start_line"
    type: "integer"
    description: ""
    
  - name: "body_html"
    type: "string"
    description: ""
    
  - name: "line"
    type: "integer"
    description: ""
    
  - name: "side"
    type: "string"
    description: ""
    
  - name: "pr_id"
    type: "string"
    description: ""
---