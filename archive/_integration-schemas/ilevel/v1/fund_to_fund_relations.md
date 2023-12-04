---
tap: "ilevel"
version: "1"
key: "fund-fund-relation"

name: "fund_to_fund_relations"
doc-link: "{{ integration.api-docs }}"
singer-schema: "https://github.com/singer-io/tap-ilevel/blob/master/tap_ilevel/schemas/fund_to_fund_relations.json"
description: |
  The `{{ table.name }}` table contains info about fund to fund relations in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "GetObjectRelationships(FundToFund)"
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
    foreign-key-id: "fund-id"

  - name: "type_id"
    type: "string"
    description: ""
---