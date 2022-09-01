---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "github"
version: "2"
key: "review"

name: "reviews"
doc-link: https://developer.github.com/v3/pulls/reviews/
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/reviews.json
description: |
  The `{{ table.name }}` table contains info about pull request reviews in the repositories specified for the integration. A pull request review is a group of comments on a pull request.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "List reviews for a pull request"
  doc-link: "https://docs.github.com/en/rest/reference/pulls#list-reviews-for-a-pull-request"

replication-method: "Key-based Incremental"
replication-key:
  name: "since"
  based-on: "updated_at"
  tooltip: "This is a query parameter used to extract new/updated data from GitHub. It will not be included in the table's fields."

dependent-table-key: "pull-request"


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The review ID."
    # foreign-key-id: "review-id"

  - name: "body"
    type: "string"
    description: "The description of the review."

  - name: "commit_id"
    type: "string"
    description: "The ID of the commit the review was performed on."
    foreign-key-id: "commit-id"

  - name: "html_url"
    type: "string"
    description: "The HTML URL to the review."

  - name: "pull_request_url"
    type: "string"
    description: "The URL to the pull request being reviewed."

  - name: "state"
    type: "string"
    description: |
      The state of the review. Possible values are:

      - `APPROVED`
      - `PENDING`
      - `CHANGES_REQUESTED`

  - name: "submitted_at"
    type: "date-time"
    description: ""
    
  - name: "_links"
    type: "object"
    description: ""
    subattributes:
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
            
          
        
      
    
  - name: "body_html"
    type: "string"
    description: ""
    
  - name: "body_text"
    type: "string"
    description: ""
    
  - name: "node_id"
    type: "string"
    description: ""
    
  - name: "author_association"
    type: "string"
    description: ""

  - name: "user"
    type: "object"
    description: "Details about the user who submitted the review."
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
    
  - name: "pr_id"
    type: "string"
    description: ""


---