---
tap: "freshdesk"
# version: ""

name: "agents"

doc-link: https://developers.freshdesk.com/api/#agents
singer-schema: https://github.com/singer-io/tap-freshdesk/blob/master/tap_freshdesk/schemas/agents.json
description: |
  The `agents` table contains info about the agents in your Freshdesk account.

replication-method: "Key-based Incremental"
api-method:
  name: "listAllAgents"
  doc-link: https://developers.freshdesk.com/api/#list_all_agents

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The agent ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the agent was updated."

  - name: "available"
    type: "boolean"
    description: "Indicates if the agent is taking new tickets. "

  - name: "available_since"
    type: "date-time"
    description: "Dependent on the value of the `available` attribute, this timestamp denotes when the agent became available/unavailable."

  - name: "occasional"
    type: "boolean"
    description: "Indicates if the agent is an occasional agent."

  - name: "signature"
    type: "string"
    description: "The HTML-formatted signature of the agent."

  - name: "ticket_scope"
    type: "integer"
    description: |
      The ticket permission of the agent. Possible values include:

      - `1` - Global Access
      - `2` - Group Access
      - `3` - Restricted Access

  - name: "group_ids"
    type: "array"
    description: "The group IDs associated with the agent."
    array-attributes:
      - name: "type"
        type: "integer"
        description: "The ID of the group."

  - name: "role_ids"
    type: "array"
    description: "The role IDs associated with the agent."
    array-attributes:
      - name: "type"
        type: "integer"
        description: "The ID of the role."

  - name: "created_at"
    type: "date-time"
    description: "The timestamp when the agent was created."

  - name: "contact"
    type: "object"
    description: "Details about the contact info associated with the agent."
    object-attributes:
      - name: "active"
        type: "boolean"
        description: "Indicates if the agent is verified."

      - name: "email"
        type: "string"
        description: "The email address associated with the agent."

      - name: "job_title"
        type: "string"
        description: "The job title of the agent."

      - name: "language"
        type: "string"
        description: "The language of the agent. `en` is the default."

      - name: "last_login_at"
        type: "date-time"
        description: "The timestamp when the agent last logged in."

      - name: "mobile"
        type: "string"
        description: "The mobile number of the agent."

      - name: "name"
        type: "string"
        description: "The agent's name."

      - name: "phone"
        type: "string"
        description: "The phone number of the agent."

      - name: "time_zone"
        type: "string"
        description: "The timezone of the agent."

      - name: "created_at"
        type: "date-time"
        description: "The timestamp when the agent's contact details were first created."

      - name: "updated_at"
        type: "date-time"
        description: "The timestamp of the last time the agent's contact details were updated."
---