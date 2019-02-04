---
tap: "clubspeed"
version: "1.0"

name: "events"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/events.json"
description: |
  The `{{ table.name }}` table contains info about events.

  **Note**: This table uses `{{ replication-keys | strip }}` as the [Replication Key]({{ link.replication.rep-keys | prepend: site.baseurl }}). This means that unless an event's `{{ replication-keys | strip }}` value is updated, changes to event records will not be selected for replication.

replication-method: "Key-based Incremental"

attributes:
  - name: "eventId"
    type: "integer"
    primary-key: true
    description: "The event ID."
    foreign-key-id: "event-id"

  - name: "eventScheduledTime"
    type: "date-time"
    replication-key: true
    description: "The scheduled time for the event."

  - name: "createdHeatSpots"
    type: "integer"
    description: "The number of heat spots that have been created for the event."

  - name: "createdHeatTime"
    type: "date-time"
    description: "The time at which the relevant heat will start."

  - name: "eventDesc"
    type: "string"
    description: "The description of the event."

  - name: "eventDuration"
    type: "integer"
    description: "The expected duration of the event, in minutes."

  - name: "eventNotes"
    type: "string"
    description: "The notes for the event."

  - name: "eventTheme"
    type: "integer"
    description: "The theme for the event."

  - name: "eventTypeId"
    type: "integer"
    description: "The ID for the event type."
    foreign-key-id: "event-type-id"

  - name: "eventTypeName"
    type: "string"
    description: "The name of the type of the event."

  - name: "memberOnly"
    type: "boolean"
    description: "Indicates whether entry into the event requires a membership."

  - name: "reservationId"
    type: "integer"
    description: "The ID of the reservation for the event."
    foreign-key-id: "reservation-id"

  - name: "totalRacers"
    type: "integer"
    description: "The total number of racers for the event."

  - name: "trackNo"
    type: "integer"
    description: "The number of the track to be used for the event."
---