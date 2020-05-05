---
tap: "outreach"
version: "1"
key: "stage"

name: "stages"
doc-link: "https://api.outreach.io/api/v2/docs#stage"
singer-schema: "https://github.com/singer-io/tap-outreach/blob/master/tap_outreach/schemas/stages.json"
description: |
  The `{{ table.name}}` table contains information about different stages in a deal process.

replication-method: "Key-based Incremental"

api-method:
  name: "Get stages"
  doc-link: "https://api.outreach.io/api/v2/docs#stage"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The stage ID."
    #foreign-key-id: "stage-id"

  - name: "updatedAt"
    type: "date-time"
    description: "The time the stage was last updated." 
    replication-key: true 

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
  - name: "order"
    type: "integer"
    description: ""
  - name: "updaterId"
    type: "integer"
    description: ""
---