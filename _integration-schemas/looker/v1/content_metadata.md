---
tap: "looker"
version: "1"
key: ""

name: "content_metadata"
doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/content#get_all_content_metadatas"
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/content_metadata.json"
description: |
  The `{{ table.name }}` table contains information about content metadata in your {{ integration.display_name }} account.
  
replication-method: "Full Table"
api-method:
    name: "Get All Content Metadatas"
    doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/content#get_all_content_metadatas"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The content metadata ID."

  - name: "content_type"
    type: "string"
    description: ""
  - name: "dashboard_id"
    type: "string"
    description: ""
  - name: "folder_id"
    type: "string"
    description: ""
  
  - name: "inheriting_id"
    type: "string"
    description: ""
  - name: "inherits"
    type: "boolean"
    description: ""
  - name: "look_id"
    type: "string"
    description: ""
  - name: "name"
    type: "string"
    description: ""
  - name: "parent_id"
    type: "string"
    description: ""
  - name: "slug"
    type: "string"
    description: ""
  - name: "space_id"
    type: "string"
    description: ""
---
