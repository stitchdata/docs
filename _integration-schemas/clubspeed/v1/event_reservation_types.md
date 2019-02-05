---
tap: "clubspeed"
version: "1.0"

name: "event_reservation_types"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/event_reservation_types.json"
description: |
  The `{{ table.name }}` table contains info about the descriptions for event reservation types.

replication-method: "Full Table"

attributes:
  - name: "eventReservationTypeId"
    type: "integer"
    primary-key: true
    description: "The event reservation type ID."
    foreign-key-id: "event-reservation-type-id"

  - name: "description"
    type: "string"
    description: "The description of the event reservation type."
---