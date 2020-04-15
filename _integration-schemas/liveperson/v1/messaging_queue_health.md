---
tap: "liveperson"
version: "1"
key: "messaging-queue-health"

name: "messaging_queue_health"
doc-link: "https://developers.liveperson.com/messaging-operations-api-methods-messaging-queue-health.html"
singer-schema: "https://github.com/singer-io/tap-liveperson/blob/master/tap_liveperson/schemas/messaging_queue_health.json"
description: |
  The `{{ table.name }}` table contains messaging queue-related metrics.

replication-method: "Full Table"

api-method:
    name: "Retrieve messaging queue metrics"
    doc-link: "https://developers.liveperson.com/messaging-operations-api-methods-messaging-queue-health.html"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    #foreign-key-id: "messaging-queue-health-id"

  - name: "actionableAndConsumerLastMessage"
    type: "number"
    description: ""

  - name: "actionableAndDuringTransfer"
    type: "number"
    description: ""

  - name: "actionableAndManualSla"
    type: "number"
    description: ""

  - name: "actionableConversations"
    type: "number"
    description: ""

  - name: "avgWaitTimeForAgentAssignment_AfterTransfer"
    type: "number"
    description: ""

  - name: "avgWaitTimeForAgentAssignment_AfterTransferFromAgent"
    type: "number"
    description: ""

  - name: "avgWaitTimeForAgentAssignment_AfterTransferFromBot"
    type: "number"
    description: ""

  - name: "avgWaitTimeForAgentAssignment_NewConversation"
    type: "number"
    description: ""

  - name: "maxWaitTimeForAgentAssignment"
    type: "number"
    description: ""

  - name: "maxWaitTimeForAgentAssignment_AfterTransferFromAgent"
    type: "number"
    description: ""

  - name: "notActionableAndManualSla"
    type: "number"
    description: ""

  - name: "notActionableConversations"
    type: "number"
    description: ""

  - name: "notActionableDuringTransfer"
    type: "number"
    description: ""

  - name: "skill"
    type: "string"
    description: ""

  - name: "timestamp"
    type: "integer"
    description: ""

  - name: "unassignedConversations"
    type: "number"
    description: ""

  - name: "unassignedConversationsAndFirstTimeConsumer"
    type: "number"
    description: ""

  - name: "waitTimeForAgentAssignment_50thPercentile"
    type: "number"
    description: ""

  - name: "waitTimeForAgentAssignment_90thPercentile"
    type: "number"
    description: ""
---
