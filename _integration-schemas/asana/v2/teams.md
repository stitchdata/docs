---
tap: "asana"
version: "2"
key: "team"

name: "teams"
doc-link: "https://developers.asana.com/docs/teams"
singer-schema: "https://github.com/singer-io/tap-asana/blob/master/tap_asana/schemas/teams.json"
description: |
  The `{{ table.name }}` table contains info about teams that belong to a specified user in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: "Get teams for a user"
    doc-link: "https://developers.asana.com/docs/get-teams-for-a-user"

attributes:
  - name: "gid"
    type: "string"
    primary-key: true
    description: "The team GID."
    #foreign-key-id: "team-id"

  - name: "description"
    type: "string"
    description: ""
  
  - name: "html_description"
    type: "string"
    description: ""
  - name: "name"
    type: "string"
    description: ""
  - name: "organization"
    type: "object"
    description: ""
    subattributes:
      - name: "gid"
        type: "string"
        description: "The workspace'S GID."
        foreign-key-id: "workspace-id"
      - name: "name"
        type: "string"
        description: ""
      - name: "resource_type"
        type: "string"
        description: ""
  - name: "permalink_url"
    type: "string"
    description: ""
  - name: "resource_type"
    type: "string"
    description: ""
  - name: "users"
    type: "array"
    description: ""
    subattributes:
      - name: "gid"
        type: "string"
        description: "The user's GID."
        foreign-key-id: "user-id"
      - name: "name"
        type: "string"
        description: ""
      - name: "resource_type"
        type: "string"
        description: ""
---
