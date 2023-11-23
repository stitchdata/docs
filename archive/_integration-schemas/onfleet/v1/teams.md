---
tap: "onfleet"
version: "1"

name: "teams"
doc-link: "http://docs.onfleet.com/docs/teams"
singer-schema: "https://github.com/singer-io/tap-onfleet/blob/master/tap_onfleet/schemas/teams.json"
description: |
  The `{{ table.name }}` table contains info about the teams in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List teams"
    doc-link: "http://docs.onfleet.com/docs/teams#list-teams"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The team ID."
    foreign-key-id: "team-id"

  - name: "timeLastModified"
    type: "date-time"
    replication-key: true
    description: "The time the team was last modified."

  - name: "hub"
    type: "string"
    description: "The ID of the hub associated with the team."
    foreign-key-id: "hub-id"

  - name: "managers"
    type: "array"
    description: "The IDs of the managing administrators associated with the team."
    subattributes:
      - name: "value"
        type: "string"
        description: "The adminstrator ID."
        foreign-key-id: "administrator-id"

  - name: "name"
    type: "string"
    description: "The name of the team."

  - name: "tasks"
    type: "array"
    description: "The IDs of the tasks assigned to the team."
    subattributes:
      - name: "value"
        type: "string"
        description: "The task ID."
        foreign-key-id: "task-id"

  - name: "timeCreated"
    type: "date-time"
    description: "The time the team was created."

  - name: "workers"
    type: "array"
    description: "The IDs of the workers belonging to the team."
    subattributes:
      - name: "value"
        type: "string"
        description: " The worker ID."
        foreign-key-id: "worker-id"
---