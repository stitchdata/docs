---
tap: "intercom"
version: "1"

name: "tags"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-intercom/blob/master/tap_intercom/schemas/tags.json"
description: |
  The `{{ table.name }}` table contains information about tags within your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The tag ID."
    foreign-key-id: "tag-id"
    
  - name: "name"
    type: "string"
    description: ""
  - name: "type"
    type: "string"
    description: ""
---
