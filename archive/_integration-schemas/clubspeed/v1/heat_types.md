---
tap: "clubspeed"
version: "1"

name: "heat_types"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/heat_types.json"
description: |
  The `{{ table.name }}` table contains info about heat types.

replication-method: "Full Table"

attributes:
  - name: "heatTypesId"
    type: "integer"
    primary-key: true
    description: "The heat type ID."
    foreign-key-id: "heat-type-id"

  - name: "cannotBelow"
    type: "integer"
    description: "The minimum cut off for lap times, in milliseconds."

  - name: "cannotExceed"
    type: "integer"
    description: "The maximum cut off for lap times, in milliseconds."

  - name: "cost"
    type: "integer"
    description: "The number of points required for the heat type."

  - name: "deleted"
    type: "boolean"
    description: "Indicates whether the heat type has been soft deleted."

  - name: "enabled"
    type: "boolean"
    description: "Indicates whether the heat type is enabled."

  - name: "isEventHeatOnly"
    type: "boolean"
    description: "Indicates whether the heat type is meant only for events."

  - name: "isPracticeHeat"
    type: "boolean"
    description: "Indicates whether this heat type is meant to be a practice round."

  - name: "lapsOrMinutes"
    type: "integer"
    description: "The quantity of laps or minutes (depending on the heat type) required for the heat type to finish."

  - name: "memberOnly"
    type: "boolean"
    description: "Indicates whether a heat type should only allow entrance to members."

  - name: "name"
    type: "string"
    description: "The name of the heat type."

  - name: "raceBy"
    type: "integer"
    description: |
      Indicates whether the heat type should treat `lapsOrMinutes` as laps or minutes. Possible values are:

      - `0` - Minutes
      - `1` - Laps

  - name: "racersPerHeat"
    type: "integer"
    description: "The total number of racers available for the heat type."

  - name: "scheduleDuration"
    type: "integer"
    description: "The expected duration of the heat type."

  - name: "speedLevel"
    type: "integer"
    description: "The speed level for the heat type."

  - name: "trackId"
    type: "integer"
    description: "The default track ID for the heat type."
    foreign-key-id: "track-id"

  - name: "winBy"
    type: "integer"
    description: |
      The indication of whether the heat type is won by laps or position. Possible values are:

      - `0` - Best Time
      - `1` - Finish Position
---