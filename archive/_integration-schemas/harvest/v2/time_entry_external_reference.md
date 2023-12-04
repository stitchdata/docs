---
tap: "harvest"
version: "2"

name: "time_entry_external_reference"
doc-link: https://help.getharvest.com/api-v2/timesheets-api/timesheets/time-entries/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/time_entry_external_reference.json
description: |
  The `{{ table.name }}` table contains pairs of time entry IDs and external reference IDs. This data can be used to tie time entries tracked in external services (such as Trello) to your other Harvest data.

  **Note**: This table is updated based on new and updated `time_entries`. This means that when a time entry is updated, this table will also be updated.

replication-method: "Key-based Incremental"

replication-key:
  name: "updated_at"
  ## This is replicated as part of the parent table, time_entries

api-method:
  name: List all time entries
  doc-link: https://help.getharvest.com/api-v2/timesheets-api/timesheets/time-entries#list-all-time-entries

attributes:
  - name: "time_entry_id"
    type: "integer"
    primary-key: true
    description: "The time entry ID."
    foreign-key-id: "time-entry-id"

  - name: "external_reference_id"
    type: "string"
    primary-key: true
    description: "The external reference ID."
    foreign-key-id: "external-reference-id"
---
