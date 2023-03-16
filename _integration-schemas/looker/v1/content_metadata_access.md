---
tap: "looker"
version: "1"
key: "content-metadata-access"

name: "content_metadata_access"
doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/content#get_all_content_metadata_accesses"
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/content_metadata_access.json"
description: |
  The `{{ table.name }}` table contains information about content metadata access records in your {{ integration.display_name }} instance.
  
replication-method: "Full Table"

api-method:
    name: "Get all content metadata accesses"
    doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/content#get_all_content_metadata_accesses"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The access record ID."

  - name: "content_metadata_id"
    type: "string"
    description: ""
    foreign-key-id: "content-metadata-id"

  - name: "group_id"
    type: "string"
    description: ""
    foreign-key-id: "group-id"
  
  - name: "permission_type"
    type: "string"
    description: ""

  - name: "user_id"
    type: "string"
    description: ""
    foreign-key-id: "user-id"
---