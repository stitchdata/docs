---
tap: "harvest"
version: "2.0"

name: "time_entry_external_reference"
doc-link: https://help.getharvest.com/api-v2/timesheets-api/timesheets/time-entries/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/time_entry_external_reference.json
description: |
  The `{{ table.name }}` table contains pairs of time entry IDs and external reference IDs. This data can be used to tie time entries tracked in external services (such as Trello) to your other Harvest data.

replication-method: "Key-based Incremental"

api-method:
  name: List all time entries
  doc-link: https://help.getharvest.com/api-v2/timesheets-api/timesheets/time-entries#list-all-time-entries

attributes:
  - name: "time_entry_id"
    type: "integer"
    description: "The time entry ID."
    foreign-key-id: "time-entry-id"

  - name: "external_reference_id"
    type: "integer"
    description: "The external reference ID."
    foreign-key-id: "external-reference-id"
---