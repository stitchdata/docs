---
tap: "liveperson"
version: "1"
key: "agent-state-distribution"

name: "agent_state_distribution"
doc-link: "https://developers.liveperson.com/operational-realtime-api-methods-agent-activity.html"
singer-schema: "https://github.com/singer-io/tap-liveperson/blob/master/tap_liveperson/schemas/agent_state_distribution.json"
description: "The `{{ table.name }}` table contains info about the agent state distribution in your {{ integration.display_name }} account."

replication-method: "Full Table"

api-method:
    name: "Retrieve agent state distribution"
    doc-link: "https://developers.liveperson.com/operational-realtime-api-methods-agent-activity.html"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    #foreign-key-id: "agent-state-distribution-id"

  - name: "metricsData"
    type: "anything"
    description: ""

  - name: "timestamp"
    type: "integer"
    description: ""
---
