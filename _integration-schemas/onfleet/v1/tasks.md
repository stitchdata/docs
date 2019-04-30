---
tap: "onfleet"
version: "1.0"

name: "tasks"
doc-link: "http://docs.onfleet.com/docs/tasks"
singer-schema: "https://github.com/singer-io/tap-onfleet/blob/master/tap_onfleet/schemas/tasks.json"
description: |
  The `{{ table.name }}` table contains info about the tasks in your {{ integration.display_name }} account. Tasks are units of work that [`administrators`](#administrators) create and assign to [`workers`](#workers) for completion.

replication-method: "Key-based Incremental"

api-method:
    name: "List tasks"
    doc-link: "http://docs.onfleet.com/docs/tasks#list-tasks"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The task ID."
    foreign-key-id: "task-id"

  - name: "timeLastModified"
    type: "date-time"
    replication-key: true
    description: "The time the task was last modified."

  - name: "completeAfter"
    type: "number"
    description: "The time the task must be completed after."

  - name: "completeBefore"
    type: "number"
    description: "The time the task must be completed for."

  - name: "completionDetails"
    type: "object"
    description: "Details about the completion of the task."
    subattributes:
      - name: "events"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "anything"
            description: ""

      - name: "failureReason"
        type: "string"
        description: ""

      - name: "firstLocation"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "anything"
            description: ""

      - name: "lastLocation"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "anything"
            description: ""

      - name: "time"
        type: "date-time"
        description: ""

      - name: "unavailableAttachments"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "anything"
            description: ""

  - name: "creator"
    type: "string"
    description: "The ID of the administrator that created the task."
    foreign-key-id: "administrator-id"

  - name: "delayTime"
    type: "number"
    description: ""

  - name: "dependencies"
    type: "array"
    description: "Details about the dependencies associated with the task. This requires usage of the **Dependency Management** feature in {{ integration.display_name }}."
    subattributes:
      - name: "value"
        type: "anything"
        description: ""

  - name: "destination"
    type: "object"
    description: "Details about the destination associated with the task."
    subattributes:
      - name: "address"
        type: "object"
        description: "The destination's address."
        subattributes:
          - name: "apartment"
            type: "string"
            description: "The apartment or unit for the address, if applicable."

          - name: "city"
            type: "string"
            description: "The city for the address."

          - name: "country"
            type: "string"
            description: "The country for the address."

          - name: "number"
            type: "string"
            description: "The street number for the address."

          - name: "postalCode"
            type: "string"
            description: "The postal code for the address."

          - name: "state"
            type: "string"
            description: "The state for the address."

          - name: "street"
            type: "string"
        description: "The street for the address."

      - name: "id"
        type: "string"
        description: "The destination ID."

      - name: "location"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "anything"
            description: ""

      - name: "metadata"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "anything"
            description: ""

      - name: "notes"
        type: "string"
        description: "Notes about the destination."

      - name: "timeCreated"
        type: "date-time"
        description: "The time the destination was created."

      - name: "timeLastModified"
        type: "date-time"
        description: "The time the destination was last modified."

  - name: "estimatedCompletionTime"
    type: "number"
    description: ""

  - name: "executor"
    type: "string"
    description: ""

  - name: "feedback"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "anything"
        description: ""

  - name: "identity"
    type: "object"
    description: ""
    subattributes:
      - name: "checksum"
        type: "string"
        description: ""

      - name: "failedScanCount"
        type: "number"
        description: ""

  - name: "merchant"
    type: "string"
    description: ""

  - name: "metadata"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "anything"
        description: ""

  - name: "notes"
    type: "string"
    description: "Notes about the task."

  - name: "organization"
    type: "string"
    description: "The ID of the organization associated with the task."
    foreign-key-id: "organization-id"

  - name: "overrides"
    type: "object"
    description: "Details about the recipient overrides associated with the task."

  - name: "pickupTask"
    type: "boolean"
    description: "Indicates if the task is a pick-up task."

  - name: "quantity"
    type: "number"
    description: "**Applicable only if Route Optimization is enabled.** The quantity of the task."

  - name: "recipients"
    type: "array"
    description: "Details about the task recipient(s)."
    subattributes:
      - name: "id"
        type: "string"
        description: "The ID of the recipient."

      - name: "metadata"
        type: "array"
        description: "Metadata about the recipient."
        subattributes:
          - name: "value"
            type: "anything"
            description: ""

      - name: "name"
        type: "string"
        description: "The name of the recipient."

      - name: "notes"
        type: "string"
        description: "Notes about the recipient."

      - name: "organization"
        type: "string"
        description: "The ID of the organization the recipient is associated with."

      - name: "phone"
        type: "string"
        description: "The recipient's phone number."

      - name: "skipSMSNotifications"
        type: "boolean"
        description: "Indicates if "

      - name: "timeCreated"
        type: "date-time"
        description: "The time the recipient was created."

      - name: "timeLastModified"
        type: "date-time"
        description: "The time the recipient was last modified."

  - name: "serviceTime"
    type: "number"
    description: "**Applicable only if Route Optimization is enabled.** The service time for the task, in minutes."

  - name: "shortId"
    type: "string"
    description: ""

  - name: "sourceTaskId"
    type: "string"
    description: ""

  - name: "state"
    type: "number"
    description: |
      The state of the task. Possible values include:

      - `0` - Unassigned. The task has not yet been assigned to a worker.
      - `1` - Assigned. The task has been assigned to a worker.
      - `2` - Active. The task has been started by the assigned worker.
      - `3` - Completed. The task has been completed by its assigned worker. This inludes successful and failed completions.

  - name: "timeCreated"
    type: "date-time"
    description: "The time the task was created."

  - name: "trackingURL"
    type: "string"
    description: ""

  - name: "trackingViewed"
    type: "boolean"
    description: ""

  - name: "worker"
    type: "string"
    description: "The ID of the worker assigned to the task."
    foreign-key-id: "worker-id"
---