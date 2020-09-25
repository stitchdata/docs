---
tap: "github"
version: "1"
key: "project-card"

name: "project_cards"
doc-link: "https://docs.github.com/en/rest/reference/projects#cards"
singer-schema: "https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/project_cards.json"
description: |
  The `{{ table.name }}` table contains information about cards in your {{ integration.display_name }} project.

replication-method: "Key-based Incremental"

api-method:
    name: "listProjectCards"
    doc-link: "https://developer.github.com/v3/projects/cards/#list-project-cards"

attributes:
  - name: "id"
    type: "number"
    primary-key: true
    description: "The project card ID."

  - name: "updated_at"
    type: "date-time"
    description: "The time the card was last updated."
    replication-key: true
      
  - name: "_sdc_repository"
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
      - name: "id"
        type: "number"
        description: ""
      - name: "login"
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
