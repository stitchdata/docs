---
tap: "clubspeed"
version: "1"

name: "event_heat_types"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/event_heat_types.json"
description: |
  The `{{ table.name }}` table contains info about event type classifications, which are used to look up [`event_rounds`](#event_rounds) when creating [`events`](#events).

replication-method: "Full Table"

attributes:
  - name: "eventHeatTypeId"
    type: "integer"
    primary-key: true
    description: "The event heat type ID."
    # foreign-key-id: "event-heat-type-id"

  - name: "cadetsPerHeat"
    type: "integer"
    description: "The maximum number of cadet racers for an event round."

  - name: "description"
    type: "string"
    description: "The description of the event round."

  - name: "eventTypeId"
    type: "integer"
    description: "The event type for the default event round information."
    foreign-key-id: "event-type-id"

  - name: "heatTypeId"
    type: "integer"
    description: "The heat type to be used with the resulting heat."
    foreign-key-id: "heat-type-id"

  - name: "heatsPerRacer"
    type: "integer"
    description: "The number of heats in which each racer will participate."

  - name: "racersPerHeat"
    type: "integer"
    description: "The maximum number of racers for the event round."

  - name: "roundNumber"
    type: "integer"
    description: "The ordered round number in the event."
---