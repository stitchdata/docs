---
tap: "harvest"
version: "1.0"

name: "time_entries"
doc-link: http://help.getharvest.com/api-v1/timesheets-api/timesheets/retrieving-time-entries#retrieving-a-single-entry
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/time_entries.json
description: |
  The `time_entries` table contains info about the time entries in your Harvest account.

replication-method: "Key-based Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The time entry ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the time entry was last updated."

  - name: "notes"
    type: "string"
    description: "Notes entered about the time entry."

  - name: "spent_at"
    type: "string"
    description: "The date of the time entry."

  - name: "hours"
    type: "number"
    description: "The number of hours tracked in the time entry."

  - name: "user_id"
    type: "integer"
    description: "The ID of the user associated with the time entry."

  - name: "project_id"
    type: "integer"
    description: "The ID of the project associated with the time entry."

  - name: "task_id"
    type: "integer"
    description: "The ID of the task associated with the time entry."

  - name: "created_at"
    type: "date-time"
    description: "The time the time entry was created."

  - name: "adjustment_record"
    type: "boolean"
    description: "Indicates if there is an adjustment record associated with the time entry."

  - name: "timer_started_at"
    type: "date-time"
    description: "The date and time the timer was started, if tracked by duration."

  - name: "is_closed"
    type: "boolean"
    description: "The time the time entry was ended, if tracking by start/end times."

  - name: "is_billed"
    type: "boolean"
    description: "Indicates if the time entry has been marked as invoiced."

  - name: "hours_with_timer"
    type: "number"
    description: "If a timer is running, this will contain the currently tracked value."
---