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

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "gid"
    type: "string"
    description: ""
    primary-key: true

  - name: "name"
    type: "string"
    description: ""

  - name: "project"
    type: "object"
    description: ""
    subattributes:
    - name: "gid"
      type: "string"
      description: ""

    - name: "resource_type"
      type: "string"
      description: ""

    - name: "name"
      type: "string"
      description: ""


  - name: "projects"
    type: "array"
    description: ""
    subattributes:
    - name: "gid"
      type: "string"
      description: ""

    - name: "resource_type"
      type: "string"
      description: ""

    - name: "name"
      type: "string"
      description: ""


  - name: "resource_type"
    type: "string"
    description: ""


---