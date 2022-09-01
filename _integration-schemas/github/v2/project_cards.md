---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "github"
version: "2"
key: "project-card"

name: "project_cards"
doc-link: "https://docs.github.com/en/rest/reference/projects#cards"
singer-schema: "https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/project_cards.json"
description: |
  The `{{ table.name }}` table contains information about project cards in the repositories specified for the integration.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "List project cards"
  doc-link: "https://docs.github.com/en/rest/reference/projects#list-project-cards"

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
    description: "The project card ID."
    foreign-key-id: "project-card-id"

  - name: "updated_at"
    type: "date-time"
    description: "The time the card was last updated."
      
  - name: "_sdc_repository"
    type: "string"
    description: ""
    
  - name: "project_id"
    type: "string"
    description: ""
    
  - name: "column_name"
    type: "string"
    description: ""

  - name: "archived"
    type: "boolean"
    description: "Whether or not the card has been archived."

  - name: "cards_url"
    type: "string"
    description: "The URL where the cards are located."

  - name: "column_url"
    type: "string"
    description: "The column URL."

  - name: "content_url"
    type: "string"
    description: "The content URL."

  - name: "created_at"
    type: "date-time"
    description: "The time the card was created."

  - name: "creator"
    type: "object"
    description: "Information about the card's creator."
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
        type: "number"
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
 
  - name: "name"
    type: "string"
    description: "The name of the card."

  - name: "node_id"
    type: "string"
    description: "The card's node ID."

  - name: "note"
    type: "string"
    description: "Notes in the card."

  - name: "project_url"
    type: "string"
    description: "The project URL."

  - name: "url"
    type: "string"
    description: "The card URL."
---