---
tap: "github"
version: "1"
key: "project-card"

name: "project_cards"
doc-link: "https://docs.github.com/en/rest/reference/projects#cards"
singer-schema: "https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/project_cards.json"
description: |
  The `{{ table.name }}` table contains information about project cards in the repositories specified for the integration.

  **Note**: In order to replicate this table, you must also set the [`projects`](#projects) table to replicate.

replication-method: "Key-based Incremental"
replication-key:
  name: "since"
  based-on: "updated_at"
  tooltip: "This is a query parameter used to extract new/updated data from GitHub. It will not be included in the table's fields."

dependent-on: "projects"

api-method:
  name: "List project cards"
  doc-link: "https://docs.github.com/en/rest/reference/projects#list-project-cards"

attributes:
  - name: "id"
    type: "number"
    primary-key: true
    description: "The project card ID."
    foreign-key-id: "project-card-id"

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