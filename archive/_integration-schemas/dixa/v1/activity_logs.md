---
tap: "dixa"
version: "1"
key: ""

name: "activity_logs"
doc-link: "https://docs.dixa.io/openapi/dixa-api/tag/Conversations/#tag/Conversations/operation/getConversationsActivitylog"
singer-schema: https://github.com/singer-io/tap-dixa/blob/main/tap_dixa/schemas/activity_logs.json
description: |
  The `{{ table.name }}` lists all information from activity logs for an organization in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "List organization activity log"
  doc-link: "https://docs.dixa.io/openapi/dixa-api/tag/Conversations/#tag/Conversations/operation/getConversationsActivitylog"

table-key-properties: "id"
valid-replication-keys: "activityTimestamp"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The activity ID."
    #foreign-key-id: "activity-id"

  - name: "activityTimestamp"
    type: "date-time"
    replication-key: true
    description: "The time the activity happened."

  - name: "activityType"
    type: "string"
    description: ""

  - name: "attributes"
    type: "object"
    description: ""
    subattributes:
      - name: "agent"
        type: "object"
        description: ""
        subattributes:
          - name: "id"
            type: "string"
            description: ""
          - name: "name"
            type: "string"
            description: ""
          - name: "email"
            type: "string"
            description: ""
          - name: "phoneNumber"
            type: "string"
            description: ""
      - name: "agentNames"
        type: "array"
        description: ""
        subattributes: 
          - name: "items"
            type: "string"
            description: ""
      - name: "agentId"
        type: "string"
        description: ""
      - name: "agentName"
        type: "string"
        description: ""
      - name: "templateName"
        type: "string"
        description: ""
      - name: "conversationSubject"
        type: "string"
        description: ""
      - name: "messageId"
        type: "string"
        description: "The message ID."
        foreign-key-id: "message-id"
      - name: "fromEndpoint"
        type: "string"
        description: ""
      - name: "avatarUrl"
        type: "string"
        description: ""
      - name: "tagAdded"
        type: "string"
        description: ""
      - name: "note"
        type: "string"
        description: ""                   

  - name: "author"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
      - name: "name"
        type: "sting"
        description: ""
      - name: "email"
        type: "string"
        description: ""
      - name: "phoneNumber"
        type: "string"
        description: ""      

  - name: "conversationId"
    type: "integer"
    description: "The conversation ID."
    foreign-key-id: "conversation-id"
---