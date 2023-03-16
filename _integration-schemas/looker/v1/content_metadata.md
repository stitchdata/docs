---
tap: "looker"
version: "1"
key: "content-metadata"

name: "content_metadata"
doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/content#get_all_content_metadatas"
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/content_metadata.json"
description: |
  The `{{ table.name }}` table contains information about content metadata in your {{ integration.display_name }} instance.
  
replication-method: "Full Table"
api-method:
    name: "Get all content metadatas"
    doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/content#get_all_content_metadatas"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The content metadata ID."
    foreign-key-id: "content-metadata-id"

  - name: "content_type"
    type: "string"
    description: ""

  - name: "dashboard_id"
    type: "string"
    description: ""
    foreign-key-id: "dashboard-id"

  - name: "folder_id"
    type: "string"
    description: ""
    foreign-key-id: "folder-id"
  
  - name: "inheriting_id"
    type: "string"
    description: ""

  - name: "inherits"
    type: "boolean"
    description: ""

  - name: "look_id"
    type: "string"
    description: ""
    foreign-key-id: "look-id"

  - name: "name"
    type: "string"
    description: ""

  - name: "parent_id"
    type: "string"
    description: ""
    foreign-key-id: "content-metadata-id"

  - name: "slug"
    type: "string"
    description: ""

  - name: "space_id"
    type: "string"
    description: ""
    foreign-key-id: "space-id"
---