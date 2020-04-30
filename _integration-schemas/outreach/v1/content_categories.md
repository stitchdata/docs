---
tap: "outreach"
version: "1"

name: "content_categories"
doc-link: "https://api.outreach.io/api/v2/docs#contentCategory"
singer-schema: "https://github.com/singer-io/tap-outreach/blob/master/tap_outreach/schemas/content_categories.json"
description: |
  The {{ table.name }} table contains information about content categories in {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
    name: "Content Category"
    doc-link: "https://api.outreach.io/api/v2/docs#contentCategory"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The content category ID."
    #foreign-key-id: "content-id"

  - name: "updatedAt"
    type: "date-time"
    description: "The time the content category was last updated."
    replication-key: true

  - name: "allowSequences"
    type: "string"
    description: ""
  - name: "allowSnippets"
    type: "string"
    description: ""
  - name: "allowTemplates"
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
---
