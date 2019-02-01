---
tap: "clubspeed"
version: "1.0"

name: "event_types"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/event_types.json"
description: |
  The `{{ table.name }}` table contains info about event types.

replication-method: "Full Table"

attributes:
  - name: "eventTypeId"
    type: "integer"
    primary-key: true
    description: "The event type ID."
    foreign-key-id: "event-type-id"

  - name: "deleted"
    type: "boolean"
    description: "Indicates if the event type was soft deleted."

  - name: "description"
    type: "string"
    description: "The description of the event type."

  - name: "displayAtRegistration"
    type: "boolean"
    description: "Indicates whether the event type should show during registration."

  - name: "enabled"
    type: "boolean"
    description: "Indicates whether the event type is currently enabled."

  - name: "eventTypeName"
    type: "string"
    description: "The name of the event type."

  - name: "eventTypeTheme"
    type: "integer"
    description: "The theme of the event type."

  - name: "memberOnly"
    type: "boolean"
    description: "Indicates whether or not a membership is required for this event type."

  - name: "onlineProductId"
    type: "integer"
    description: "The ID of the product used to purchase the event."
    foreign-key-id: "product-id"

  - name: "ptsPerReservation"
    type: "integer"
    description: "The number of points required per reservation."

  - name: "trackId"
    type: "integer"
    description: "The ID of the track for which this event can be added."
    foreign-key-id: "track-id"
---