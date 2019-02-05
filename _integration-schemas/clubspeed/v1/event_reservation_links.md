---
tap: "clubspeed"
version: "1.0"

name: "event_reservation_links"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/event_reservation_links.json"
description: |
  The `{{ table.name }}` table contains lists of [`check`](#checks) and [`reservation`](#reservations) IDs, or checks that are linked to event reservations.

replication-method: "Full Table"

attributes:
  - name: "eventReservationLinkId"
    type: "integer"
    primary-key: true
    description: "The event reservation link ID."
    # foreign-key-id: "event-reservation-link-id"

  - name: "checkId"
    type: "integer"
    description: "The ID of the check to be linked to an event reservation."
    foreign-key-id: "check-id"

  - name: "reservationId"
    type: "integer"
    description: "The ID for the event reservation to which the check is linked."
    foreign-key-id: "reservation-id"
---