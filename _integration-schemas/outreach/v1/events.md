---
tap: "outreach"
version: "1"
key: "event"

name: "events"
doc-link: "https://api.outreach.io/api/v2/docs#event"
singer-schema: "https://github.com/singer-io/tap-outreach/blob/master/tap_outreach/schemas/events.json"
description: |
  The `{{ table.name}}` table contains information about application events in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get events"
  doc-link: "https://api.outreach.io/api/v2/docs#event"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The event ID."
    #foreign-key-id: "event-id"

  - name: "eventAt"
    type: "date-time"
    replication-key: true
    description: "The time the event occurred."

  - name: "accountId"
    type: "integer"
    description: ""

  - name: "body"
    type: "string"
    description: ""

  - name: "callId"
    type: "integer"
    description: ""

  - name: "createdAt"
    type: "date-time"
    description: ""

  - name: "externalUrl"
    type: "string"
    description: ""

  - name: "mailingId"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "opportunityId"
    type: "integer"
    description: ""

  - name: "payload"
    type: "object"
    description: ""

  - name: "prospectId"
    type: "integer"
    description: ""

  - name: "requestCity"
    type: "string"
    description: ""

  - name: "requestDevice"
    type: "string"
    description: ""

  - name: "requestHost"
    type: "string"
    description: ""

  - name: "requestProxied"
    type: "boolean"
    description: ""

  - name: "requestRegion"
    type: "boolean"
    description: ""

  - name: "taskId"
    type: "integer"
    description: ""

  - name: "userId"
    type: "integer"
    description: ""
---