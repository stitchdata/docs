---
tap: "freshdesk"
version:

name: "time_entries"
doc-link: https://developers.freshdesk.com/api/#time-entries
singer-schema: https://github.com/singer-io/tap-freshdesk/blob/master/tap_freshdesk/schemas/time_entries.json
description: |
  The `time_entries` table contains info about the time entries entered by agents working on tickets.

replication-method: "Key-based Incremental"
api-method:
  name: "listAllTimeEntries"
  doc-link: https://developers.freshdesk.com/api/#time-entries

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the time entry record."
    # foreign-key-id: "time-entry-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the time entry record was last updated."

  - name: "time_spent"
    type: "string"
    description: "The duration of the time entry record in `hh:mm` format."

  - name: "start_time"
    type: "date-time"
    description: "The time at which the time entry record is added or the time of the last invoked 'start-timer' action using a toggle."

  - name: "created_at"
    type: "date-time"
    description: "The time the time entry record was created."

  - name: "executed_at"
    type: "date-time"
    description: "The time the time entry record was added/created."

  - name: "timer_running"
    type: "boolean"
    description: "Indicates if the time is currently running."

  - name: "note"
    type: "string"
    description: "The description of the time entry."

  - name: "ticket_id"
    type: "integer"
    description: "The ID of the ticket associated with the time entry record."
    foreign-key-id: "ticket-id"

  - name: "billable"
    type: "boolean"
    description: "Indicates if the time entry record is billable."

  - name: "agent_id"
    type: "integer"
    description: "The agent ID associated with the time entry."
    foreign-key-id: "agent-id"
---