---
tap: "clubspeed"
version: "1"

name: "event_heat_details"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/event_heat_details.json"
description: |
  The `{{ table.name }}` table contains info about [`customers`](#customers) who have been placed in a queue for a specific [`event`](#events).

replication-method: "Key-based Incremental"

attributes:
  - name: "customerId"
    type: "integer"
    primary-key: true
    description: "The ID of the customer in the queue."
    foreign-key-id: "customer-id"

  - name: "eventId"
    type: "integer"
    primary-key: true
    description: "The ID of the event."
    foreign-key-id: "event-id"

  - name: "added"
    type: "date-time"
    replication-key: true
    description: "The date at which the customer was added to the event queue."

  - name: "proskill"
    type: "integer"
    description: "The proskill for the customer."

  - name: "roundLoseNum"
    type: "integer"
    description: "The round at which the customer dropped out of the event."

  - name: "totalRaces"
    type: "integer"
    description: "The total number of races in the event."
---