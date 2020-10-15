---
tap: "looker"
version: "1"
key: ""

name: "content_metadata_access"
doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/content#get_all_content_metadata_accesses"
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/content_metadata_access.json"
description: |
  The `{{ table.name }}` table contains information about content metadata access records in your {{ integration.display_name }} account.
  
replication-method: "Full Table"

api-method:
    name: "Get All Content Metadata Accesses"
    doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/content#get_all_content_metadata_accesses"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The access record ID."

  - name: "content_metadata_id"
    type: "string"
    description: ""
  - name: "group_id"
    type: "string"
    description: ""
  
  - name: "permission_type"
    type: "string"
    description: ""
  - name: "user_id"
    type: "string"
    description: ""
---
