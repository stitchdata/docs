---
tap: "activecampaign"
version: "1"
key: ""

name: "tags"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/tags.json"
description: |
  The `{{ table.name }}` table contains information about labels that you can apply to contacts in your {{ integration.display_name }} account.


replication-method: "Full Table"

api-method:
    name: "List all tags"
    doc-link: "https://developers.activecampaign.com/reference#retrieve-all-tags"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The tag ID."
    foreign-key-id: "tag-id"

  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "created_by"
    type: "integer"
    description: ""
  - name: "created_timestamp"
    type: "date-time"
    description: ""
  - name: "description"
    type: "string"
    description: ""
  
  - name: "tag"
    type: "string"
    description: ""
  - name: "tag_type"
    type: "string"
    description: ""
  - name: "updated_by"
    type: "integer"
    description: ""
  - name: "updated_timestamp"
    type: "date-time"
    description: ""
---
