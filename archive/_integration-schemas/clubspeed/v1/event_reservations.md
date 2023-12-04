---
tap: "clubspeed"
version: "1"

name: "event_reservations"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/event_reservations.json"
description: |
  The `{{ table.name }}` table contains info about event reservations, which are linked to [`events`](#events).
  
  {% capture replication-note %}
  **Note**: This table uses `{{ replication-keys | strip }}` as the [Replication Key]({{ link.replication.rep-keys | prepend: site.baseurl }}). This means that unless an event reservation's `startTime` is updated, changes to event reservation records will not be selected for replication.
  {% endcapture %}

  {% include note.html type="single-line" content=replication-note %}

replication-method: "Key-based Incremental"

attributes:
  - name: "eventReservationId"
    type: "integer"
    primary-key: true
    description: "The event reservation ID."
    foreign-key-id: "event-reservation-id"

  - name: "startTime"
    type: "date-time"
    replication-key: true
    description: "The expected start time of the event reservation."

  - name: "allowOnlineReservation"
    type: "boolean"
    description: "Indicates whether reservations can be made online."

  - name: "deleted"
    type: "boolean"
    description: "Indicates whether the event reservation has been soft deleted."

  - name: "description"
    type: "string"
    description: "The description for the event reservation."

  - name: "endTime"
    type: "date-time"
    description: "The time at which the event reservation is expected to end."

  - name: "eventTypeId"
    type: "integer"
    description: "The ID for the event type of the event."
    foreign-key-id: "event-type-id"

  - name: "externalSystemId"
    type: "integer"
    description: "A field for storing an external reference for the event reservation."

  - name: "isEventClosure"
    type: "boolean"
    description: ""

  - name: "mainId"
    type: "integer"
    description: "The ID for the parent event reservation."
    foreign-key-id: "event-reservation-id"

  - name: "minNoOfAdultsPerBooking"
    type: "integer"
    description: "The minimum number of customers per booking."

  - name: "noOfRacers"
    type: "integer"
    description: "The current number of booked customers."

  - name: "notes"
    type: "string"
    description: "The notes for the event reservation."

  - name: "ptsPerReservation"
    type: "integer"
    description: "The number of points required to make a reservation."

  - name: "repId"
    type: "integer"
    description: ""

  - name: "status"
    type: "integer"
    description: "The index for the event status of the event reservation."

  - name: "subject"
    type: "string"
    description: "The name for the event reservation."

  - name: "typeId"
    type: "integer"
    description: "The event reservation type ID."
    foreign-key-id: "event-reservation-type-id"

  - name: "userId"
    type: "integer"
    description: "The ID of the user that made the event reservation."
    foreign-key-id: "user-id"
---