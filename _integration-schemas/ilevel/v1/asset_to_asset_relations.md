---
tap: "ilevel"
version: "1"
key: "asset-relation"

name: "asset_to_asset_relations"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-ilevel/blob/master/tap_ilevel/schemas/asset_to_asset_relations.json"
description: |
  The `{{ table.name }}` table contains info about asset to asset relations in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "GetObjectRelationships(AssetToAsset)"
  doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The relationship ID."
    foreign-key-id: "relationship-id"

  - name: "from_id"
    type: "integer"
    description: ""
    foreign-key-id: "asset-id"

  - name: "is_soft_deleted"
    type: "boolean"
    description: ""

  - name: "status_id"
    type: "integer"
    description: ""

  - name: "to_id"
    type: "integer"
    description: ""
    foreign-key-id: "asset-id"

  - name: "type_id"
    type: "string"
    description: ""
---