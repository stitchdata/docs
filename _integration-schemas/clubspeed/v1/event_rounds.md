---
tap: "clubspeed"
version: "1.0"

name: "event_rounds"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/event_rounds.json"
description: |
  The `{{ table.name }}` table contains info about event rounds. This table acts as a link between [`events`](#events) and their corresponding rounds in the [`heat_main`](#heat_main).

replication-method: "Full Table"

attributes:
  - name: "eventRoundId"
    type: "integer"
    primary-key: true
    description: "The event round ID."
    foreign-key-id: "event-round-id"

  - name: "cadetsPerHeat"
    type: "integer"
    description: "The maximum number of cadet racers for the event round."

  - name: "eventId"
    type: "integer"
    description: "The ID of the parent event."
    foreign-key-id: "event-id"

  - name: "heatDescription"
    type: "string"
    description: "The description of the heat."

  - name: "heatTypeId"
    type: "integer"
    description: "The heat type ID of the heat."
    foreign-key-id: "heat-type-id"

  - name: "heatsPerRacer"
    type: "integer"
    description: "The number of heats in which each racer will participate."

  - name: "racersPerHeat"
    type: "integer"
    description: "The maximum number of racers for this event round."

  - name: "roundNumber"
    type: "integer"
    description: "The ordered round number in the event."
---