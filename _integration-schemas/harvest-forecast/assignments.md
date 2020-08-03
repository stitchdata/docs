---
tap: "harvest-forecast"
version: "1"

name: "assignments"
doc-link:
singer-schema: https://github.com/singer-io/tap-harvest-forecast/blob/master/tap_harvest_forecast/schemas/assignments.json
description: |
  The `{{ table.name }}` table contains info about the assignments assigned to the people in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The assignment ID."
    # foreign-key-id: "assignment-id"

  - name: "updated_at"
    type: "string"
    replication-key: true
    description: "The time the assignment was last updated."

  - name: "active_on_days_off"
    type: "boolean"
    description: "If `true`, the assignment takes place on a non-work day."

  - name: "allocation"
    type: "integer"
    description: "The number of hours allocated to the assignment."

  - name: "end_date"
    type: "string"
    description: "The day the assignment ended."

  - name: "notes"
    type: "string"
    description: "Any notes about the assignment."

  - name: "project_id"
    type: "integer"
    description: "The ID of the project associated with the assignment."
    foreign-key-id: "project-id"

  - name: "person_id"
    type: "integer"
    description: "The ID of the assignee."
    foreign-key-id: "person-id"

  - name: "placeholder_id"
    type: "integer"
    description: "If the assignment is a placeholder, this column will contain the placeholder ID."
    foreign-key-id: "placeholder-id"

  - name: "repeated_assignment_set_id"
    type: "integer"
    description: ""

  - name: "start_date"
    type: "string"
    description: "The day the assignment started."

  - name: "updated_by_id"
    type: "integer"
    description: "The ID of the person who last updated the assignment."
    foreign-key-id: "person-id"
---