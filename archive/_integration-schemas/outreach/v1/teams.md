---
tap: "outreach"
version: "1"
key: "team"

name: "teams"
doc-link: "https://api.outreach.io/api/v2/docs#team"
singer-schema: "https://github.com/singer-io/tap-outreach/blob/master/tap_outreach/schemas/teams.json"
description: |
  The `{{ table.name}}` table contains information about groups of users in {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
  name: "Get teams"
  doc-link: "https://api.outreach.io/api/v2/docs#team"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The team ID."
    # foreign-key-id: "team-id"

  - name: "color"
    type: "string"
    description: ""

  - name: "createdAt"
    type: "date-time"
    description: ""

  - name: "creatorId"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "scimExternalId"
    type: "string"
    description: ""

  - name: "scimSource"
    type: "string"
    description: ""

  - name: "updatedAt"
    type: "date-time"
    description: ""
    replication-key: true

  - name: "updaterId"
    type: "integer"
    description: ""
---