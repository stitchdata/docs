---
tap: "clubspeed"
version: "1.0"

name: "event_tasks"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/event_tasks.json"
description: |
  The `{{ table.name }}` table contains info about the tasks to be completed for a given [`event_reservation`](#event_reservations).

replication-method: "Key-based Incremental"

attributes:
  - name: "eventTaskId"
    type: "integer"
    primary-key: true
    description: "The event task ID."
    foreign-key-id: "event-task-id"

  - name: "completedAt"
    type: "date-time"
    replication-key: true
    description: "The date on which the task was completed. This field will be populated only if the task has been completed."

  - name: "completedBy"
    type: "integer"
    description: "The ID of the user that completed the task. This field will be populated only if the task has been completed."
    foreign-key-id: "user-id"

  - name: "eventReservationId"
    type: "integer"
    description: "The ID of the event reservation."
    foreign-key-id: "event-reservation-id"

  - name: "eventTaskTypeId"
    type: "integer"
    description: "The event task ID."
    foreign-key-id: "event-task-type-id"
---