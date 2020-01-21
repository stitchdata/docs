---
tap: "liveperson"
version: "1"
key: "agent-group"

name: "agent_groups"
doc-link: "https://developers.liveperson.com/agent-groups-api-overview.html#use-cases-for-the-agent-groups-api"
singer-schema: "https://github.com/singer-io/tap-liveperson/blob/master/tap_liveperson/schemas/agent_groups.json"
description: |
  The `{{ table.name }}` table contains info about the agent groups in your {{ integration.display_name }} account.

  **Note**: Stitch will query for and replicate deleted agent groups.

replication-method: "Full Table"

replication-key:
  name: "startTime"

api-method:
    name: "Get all agent groups"
    doc-link: "https://developers.liveperson.com/agent-groups-api-methods-get-all-agent-groups.html#request"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    #foreign-key-id: "agent-group-id"

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "isEnabled"
    type: "boolean"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "parentGroupId"
    type: "string"
    description: ""
---