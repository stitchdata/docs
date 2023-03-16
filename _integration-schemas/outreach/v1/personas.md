---
tap: "outreach"
version: "1"
key: "persona"

name: "personas"
doc-link: "https://api.outreach.io/api/v2/docs#persona"
singer-schema: "https://github.com/singer-io/tap-outreach/blob/master/tap_outreach/schemas/personas.json"
description: |
  The `{{ table.name}}` table contains information about descriptions and types of people in {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
  name: "Get personas"
  doc-link: "https://api.outreach.io/api/v2/docs#persona"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The persona ID."
    foreign-key-id: "persona-id"

  - name: "updatedAt"
    type: "date-time"
    description: "The time the persona was last updated." 
    replication-key: true 

  - name: "createdAt"
    type: "date-time"
    description: ""

  - name: "description"
    type: "string"
    description: ""
    
  - name: "name"
    type: "string"
    description: ""
---