---
tap: "clubspeed"
version: "1.0"

name: "event_statuses"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/event_statuses.json"
description: |
  The `{{ table.name }}` table contains info about event statuses, which are statuses assigned to [`event_reservations`](#event_reservations).

replication-method: "Full Table"

attributes:
  - name: "eventStatusId"
    type: "integer"
    primary-key: true
    description: "The event status ID."
    # foreign-key-id: "event-status-id"

  - name: "colorId"
    type: "integer"
    description: "The ID of the color which will be used to highlight the event when given this status"

  - name: "seq"
    type: "integer"
    description: "The order in which the event status appears in dropdowns."

  - name: "status"
    type: "string"
    description: "The readable description of the status."
---