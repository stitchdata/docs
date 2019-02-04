---
tap: "clubspeed"
version: "1.0"

name: "heat_main"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/heat_main.json"
description: |
  The `{{ table.name }}` table contains info about finished heat mains, which are instances of races on the standard venue calendar.

  **Note**: This table uses `{{ replication-keys | strip }}` as the [Replication Key]({{ link.replication.rep-keys | prepend: site.baseurl }}). This means that only finished heat mains will be selected for replication.

replication-method: "Key-based Incremental"

attributes:
  - name: "heatId"
    type: "integer"
    primary-key: true
    description: "The heat ID."
    foreign-key-id: "heat-id"

  - name: "finish"
    type: "date-time"
    replication-key: true
    description: "The actual finish time of the heat."

  - name: "beginning"
    type: "date-time"
    description: "The actual start time of the heat."

  - name: "eventRound"
    type: "integer"
    description: "The ID of the event round which corresponds to the heat."
    foreign-key-id: "event-round-id"

  - name: "heatColor"
    type: "integer"
    description: "An integer representation of the color to be used on the heat calendar."

  - name: "lapsOrMinutes"
    type: "integer"
    description: "The quantity of laps or minutes (depending on heat type) required for the heat to finish."

  - name: "memberOnly"
    type: "boolean"
    description: "Indicates whether a heat should only allow entrance to members."

  - name: "notes"
    type: "string"
    description: "Notes for the heat."

  - name: "numberOfReservation"
    type: "integer"
    description: "The number of additional reservations for the heat. **Note**: These typically represent purchased slots in a heat."

  - name: "pointsNeeded"
    type: "integer"
    description: "The number of points required to enter the heat."

  - name: "raceBy"
    type: "integer"
    description: |
      The indication of whether the heat will treat the value of `lapsOrMinutes` as laps or minutes. Possible values are:

      - `0` - Minutes
      - `1`- Laps

  - name: "racersPerHeat"
    type: "integer"
    description: "The total number of racers available for the heat."

  - name: "scheduleDuration"
    type: "integer"
    description: "The expected duration of the heat."

  - name: "scheduledTime"
    type: "date-time"
    description: "The scheduled start time of the heat."

  - name: "speedLevel"
    type: "integer"
    description: "The speed level for the heat."

  - name: "status"
    type: "integer"
    description: |
      The status of the heat. Possible values are:

      - `0` - Open
      - `1` - Racing
      - `2` - Finished
      - `3` - Aborted
      - `4` - Closed

  - name: "track"
    type: "integer"
    description: "The ID for the track for the heat."
    foreign-key-id: "track-id"

  - name: "type"
    type: "integer"
    description: "The heat type for the heat."
    foreign-key-id: "heat-type-id"

  - name: "winBy"
    type: "integer"
    description: |
      The indication of whether the heat is won by laps or position. Possible values are:

      - `0` - Best Time
      - `1` - Finish Position
---