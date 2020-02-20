---
tap: "liveperson"
version: "1"
key: "queue-health"

name: "queue_health"
doc-link: "https://developers.liveperson.com/operational-realtime-api-methods-queue-health.html"
singer-schema: "https://github.com/singer-io/tap-liveperson/blob/master/tap_liveperson/schemas/queue_health.json"
description: |
  The `{{ table.name }}` table contains queue-related metrics.

replication-method: "Full Table"

api-method:
    name: "Retrieve queue metrics"
    doc-link: "https://developers.liveperson.com/operational-realtime-api-methods-queue-health.html"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    #foreign-key-id: "queue-health-id"

  - name: "abandonedEng"
    type: "number"
    description: ""

  - name: "abandonmentRate"
    type: "number"
    description: ""

  - name: "availableSlotsCount"
    type: "number"
    description: ""

  - name: "availableSlotsSum"
    type: "number"
    description: ""

  - name: "averageAvailableSlots"
    type: "number"
    description: ""

  - name: "averageQueueSize"
    type: "number"
    description: ""

  - name: "avgTimeToAbandon"
    type: "number"
    description: ""

  - name: "avgTimeToAnswer"
    type: "number"
    description: ""

  - name: "connectedEng"
    type: "number"
    description: ""

  - name: "currentAvailableSlots"
    type: "number"
    description: ""

  - name: "currentQueueSize"
    type: "number"
    description: ""

  - name: "enteredQEng"
    type: "number"
    description: ""

  - name: "maxAvailableSlots"
    type: "number"
    description: ""

  - name: "maxQueueSize"
    type: "number"
    description: ""

  - name: "minAvailableSlots"
    type: "number"
    description: ""

  - name: "minQueueSize"
    type: "number"
    description: ""

  - name: "queueSizeCount"
    type: "number"
    description: ""

  - name: "queueSizeSum"
    type: "number"
    description: ""

  - name: "skill"
    type: "string"
    description: ""

  - name: "timestamp"
    type: "integer"
    description: ""

  - name: "totalTimeToAbandon"
    type: "number"
    description: ""

  - name: "totalTimeToAnswer"
    type: "number"
    description: ""
---