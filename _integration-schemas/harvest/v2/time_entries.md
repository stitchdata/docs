---
tap: "harvest"
version: "2.0"

name: "time_entries"
doc-link: https://help.getharvest.com/api-v2/timesheets-api/timesheets/time-entries/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/time_entries.json
description: |
  The `{{ table.name }}` table contains info about the time entries in your Harvest account.

replication-method: "Key-based Incremental"

api-method:
  name: List all time entries
  doc-link: https://help.getharvest.com/api-v2/timesheets-api/timesheets/time-entries#list-all-time-entries

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The time entry ID."
    foreign-key-id: "time-entry-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the time entry was last updated."

  - name: "billable"
    type: "boolean"
    description: "If `true`, the time entry is billable."

  - name: "billable_rate"
    type: "number"
    description: "The billable rate for the time entry."

  - name: "budgeted"
    type: "number"
    description: "If `true`, the time entry counts towards the project budget."

  - name: "client_id"
    type: "integer"
    description: "he ID of the client associated with the time entry."
    foreign-key-id: "client-id"

  - name: "cost_rate"
    type: "number"
    description: "The cost rate for the time entry."

  - name: "created_at"
    type: "string"
    description: "The time the time entry was created."

  - name: "ended_time"
    type: "string"
    description: "The time the time entry was ended, if tracking by start/end times."

  - name: "external_reference_id"
    type: "integer"
    description: "The ID of the associated external reference, if any."
    foreign-key-id: "external-reference-id"

  - name: "hours"
    type: "number"
    description: "The number of hours tracked in the time entry."

  - name: "is_billed"
    type: "boolean"
    description: "If `true`, the time entry has been marked as invoiced."

  - name: "is_closed"
    type: "boolean"
    description: "If `true`, the time entry has been approved via Timesheet Approval."

  - name: "is_locked"
    type: "boolean"
    description: "If `true`, the time entry is locked."

  - name: "is_running"
    type: "boolean"
    description: "If `true`, the time entry is currently running."

  - name: "invoice_id"
    type: "integer"
    description: "The ID of the invoice associated with the time entry."
    foreign-key-id: "invoice-id"

  - name: "locked_reason"
    type: "string"
    description: "The reason why the time entry is locked."

  - name: "notes"
    type: "string"
    description: "Notes entered about the time entry."

  - name: "project_id"
    type: "integer"
    description: "The ID of the project associated with the time entry."
    foreign-key-id: "project-id"

  - name: "spent_date"
    type: "date-time"
    description: "The date of the time entry."

  - name: "started_time"
    type: "string"
    description: "The time the time entry was started, if tracking by start/end times."

  - name: "task_id"
    type: "integer"
    description: "The ID of the task associated with the time entry."
    foreign-key-id: "task-id"

  - name: "task_assignment_id"
    type: "integer"
    description: "The ID of the task assignment associated with the time entry."

  - name: "timer_started_at"
    type: "date-time"
    description: "The date and time the timer was started, if tracked by duration."

  - name: "user_id"
    type: "integer"
    description: "The ID of the user associated with the time entry."
    foreign-key-id: "user-id"

  - name: "user_assignment_id"
    type: "integer"
    description: "The ID of the user assignment associated with the time entry."
---