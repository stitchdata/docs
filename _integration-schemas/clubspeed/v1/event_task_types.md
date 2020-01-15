---
tap: "clubspeed"
version: "1"

name: "event_task_types"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/event_task_types.json"
description: |
  The `{{ table.name }}` table contains info about event task types, which are [`event_tasks`](#event_tasks) to be tracked for completion.

replication-method: "Full Table"

attributes:
  - name: "eventTaskId"
    type: "integer"
    primary-key: true
    description: "The event task ID."
    foreign-key-id: "event-task-type-id"

  - name: "deleted"
    type: "boolean"
    description: "Indicates whether the event task has been soft deleted."

  - name: "description"
    type: "string"
    description: "The description of the task type."

  - name: "name"
    type: "string"
    description: "The name of the task type."

  - name: "seq"
    type: "integer"
    description: "The sequence in which the task type should appear."
---