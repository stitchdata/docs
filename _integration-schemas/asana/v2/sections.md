---
tap: "asana"
version: "2"
key: "section"

name: "sections"
doc-link: "https://developers.asana.com/docs/sections"
singer-schema: "https://github.com/singer-io/tap-asana/blob/master/tap_asana/schemas/sections.json"
description: |
  The `{{ table.name }}` table contains info about sections within specified projects in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: "Get sections in a project"
    doc-link: "https://developers.asana.com/docs/get-sections-in-a-project"

attributes:
  - name: "gid"
    type: "string"
    primary-key: true
    description: "The section GID."
    foreign-key-id: "section-id"

  - name: "created_at"
    type: "date-time"
    description: ""
  
  - name: "name"
    type: "string"
    description: ""
  - name: "project"
    type: "object"
    description: ""
    subattributes:
      - name: "gid"
        type: "string"
        description: "The project's GID."
        foreign-key-id: "project-id"
      - name: "name"
        type: "string"
        description: ""
      - name: "resource_type"
        type: "string"
        description: ""
  - name: "projects"
    type: "array"
    description: ""
    subattributes:
      - name: "gid"
        type: "string"
        description: "The project's GID."
        foreign-key-id: "project-id"
      - name: "name"
        type: "string"
        description: ""
      - name: "resource_type"
        type: "string"
        description: ""
  - name: "resource_type"
    type: "string"
    description: ""
---
