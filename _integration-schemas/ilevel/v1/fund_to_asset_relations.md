---
tap: "ilevel"
version: "1"
key: "fund-asset-relation"

name: "fund_to_asset_relations"
doc-link: "{{ integration.api-docs }}"
singer-schema: "https://github.com/singer-io/tap-ilevel/blob/master/tap_ilevel/schemas/fund_to_asset_relations.json"
description: |
  The `{{ table.name }}` table contains info about fund to asset relations in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "GetObjectRelationships(FundToAsset)"
  doc-link: "{{ integration.api-docs }}"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The relationship ID."
    foreign-key-id: "relationship-id"

  - name: "from_id"
    type: "integer"
    description: ""
    foreign-key-id: "fund-id"

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