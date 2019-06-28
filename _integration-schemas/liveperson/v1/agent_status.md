---
tap: "liveperson"
version: "1.0"
key: "agent-status"

name: "agent_status"
doc-link: "https://developers.liveperson.com/agent-status-reason-api-overview.html#status-reason-object-description"
singer-schema: "https://github.com/singer-io/tap-liveperson/blob/master/tap_liveperson/schemas/agent_status.json"
description: |
  The `{{ table.name }}` table contains data for each of the agent statuses in your {{ integration.display_name }} account.

  **Note**: Stitch will query for and replicate deleted agent statuses.

replication-method: "Key-based Incremental"

replication-key:
  name: "startTime"

api-method:
    name: "List agent statuses"
    doc-link: "https://developers.liveperson.com/agent-status-reason-api-methods-agent-status-list.html#description"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    #foreign-key-id: "agent-status-id"

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "enabled"
    type: "boolean"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "text"
    type: "string"
    description: ""
---