---
tap: "liveperson"
version: "1.0"
key: "agent-activity"

name: "agent_activity"
doc-link: "https://developers.liveperson.com/data-access-api-methods-agent-activity.html"
singer-schema: "https://github.com/singer-io/tap-liveperson/blob/master/tap_liveperson/schemas/agent_activity.json"
description: |
  The `{{ table.name }}` table contains info about agent session data. Activity data is a list of sessions that occur from the agent's login time to their logout time.

replication-method: "Full Table"

api-method:
    name: "Retrieve agent activity"
    doc-link: "https://developers.liveperson.com/data-access-api-methods-agent-activity.html"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    #foreign-key-id: "agent-activity-id"

  - name: "_meta"
    type: "object"
    description: ""
    subattributes:
      - name: "endTime"
        type: "integer"
        description: ""

      - name: "startTime"
        type: "integer"
        description: ""

  - name: "agentEmployeeId"
    type: "object"
    description: ""
    subattributes:
      - name: "string"
        type: "string"
        description: ""

  - name: "agentGroupID"
    type: "object"
    description: ""
    subattributes:
      - name: "long"
        type: "integer"
        description: ""

  - name: "agentID"
    type: "object"
    description: ""
    subattributes:
      - name: "long"
        type: "integer"
        description: ""

  - name: "agentLoginname"
    type: "object"
    description: ""
    subattributes:
      - name: "string"
        type: "string"
        description: ""

  - name: "agentNickname"
    type: "object"
    description: ""

    subattributes:
      - name: "string"
        type: "string"
        description: ""

  - name: "agentUsername"
    type: "object"
    description: ""
    subattributes:
      - name: "string"
        type: "string"
        description: ""

  - name: "concurrentEng"
    type: "object"
    description: ""
    subattributes:
      - name: "long"
        type: "integer"
        description: ""

  - name: "maxConcurrentEng"
    type: "object"
    description: ""
    subattributes:
      - name: "long"
        type: "integer"
        description: ""

  - name: "prevConcurrentEng"
    type: "object"
    description: ""
    subattributes:
      - name: "long"
        type: "integer"
        description: ""

  - name: "prevState"
    type: "object"
    description: ""
    subattributes:
      - name: "long"
        type: "integer"
        description: ""

  - name: "state"
    type: "object"
    description: ""
    subattributes:
      - name: "long"
        type: "integer"
        description: ""

  - name: "timestamp"
    type: "object"
    description: ""
    subattributes:
      - name: "long"
        type: "integer"
        description: ""

  - name: "type"
    type: "object"
    description: ""
    subattributes:
      - name: "long"
        type: "integer"
        description: ""
---