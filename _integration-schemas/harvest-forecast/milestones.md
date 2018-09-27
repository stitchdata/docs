---
tap: "harvest-forecast"
version: "1.0"

name: "milestones"
doc-link:
singer-schema: https://github.com/singer-io/tap-harvest-forecast/blob/master/tap_harvest_forecast/schemas/milestones.json
description: |
  The `{{ table.name }}` table contains info about the project milestones in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The milestone ID."
    foreign-key-id: "milestone-id"

  - name: "updated_at"
    type: "string"
    replication-key: true
    description: "The time the milestone was last updated."

  - name: "date"
    type: "string"
    description: "The date of the milestone."

  - name: "name"
    type: "string"
    description: "The name of the milestone."

  - name: "project_id"
    type: "integer"
    description: "The ID of the project associated with the milestone."
    foreign-key-id: "project-id"

  - name: "updated_by_id"
    type: "integer"
    description: "The ID of the person who last updated the milestone."
    foreign-key-id: "person-id"
---