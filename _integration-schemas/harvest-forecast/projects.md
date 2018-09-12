---
tap: "harvest-forecast"
version: "1.0"

name: "projects"
doc-link:
singer-schema: https://github.com/singer-io/tap-harvest-forecast/blob/master/tap_harvest_forecast/schemas/projects.json
description: |
  The `{{ table.name }}` table contains info about the projects in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The project ID."
    foreign-key-id: "project-id"

  - name: "updated_at"
    type: "string"
    replication-key: true
    description: "The time the project was last updated."

  - name: "archived"
    type: "boolean"
    description: "If `true`, the project has been archived."

  - name: "code"
    type: "string"
    description: "The code associated with the project."

  - name: "color"
    type: "string"
    description: "The color label associated with the project."

  - name: "client_id"
    type: "integer"
    description: "The ID of the client associated with the project."
    foreign-key-id: "client-id"

  - name: "end_date"
    type: "string"
    description: "The end date of the project."

  - name: "harvest_id"
    type: "integer"
    description: "The ID of the project in Harvest."

  - name: "name"
    type: "string"
    description: "The name of the project."

  - name: "notes"
    type: "string"
    description: "Any notes about the project."

  - name: "start_date"
    type: "string"
    description: "The start date of the project."

  - name: "tags"
    type: "array"
    description: "A list of the tags associated with the project."
    array-attributes: 
      - name: "value"
        type: "string"
        description: "The tag associated with the project."

  - name: "updated_by_id"
    type: "string"
    description: "The ID of the person who last updated the project."
    foreign-key-id: "person-id"
---