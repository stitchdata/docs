---
tap: "onfleet"
version: "1"

name: "workers"
doc-link: "http://docs.onfleet.com/docs/workers"
singer-schema: "https://github.com/singer-io/tap-onfleet/blob/master/tap_onfleet/schemas/workers.json"
description: |
  The `{{ table.name }}` table contains info about the workers (or drivers) in your {{ integration.display_name }} account. Workers are organization members who complete tasks.

replication-method: "Key-based Incremental"

api-method:
    name: "List workers"
    doc-link: "http://docs.onfleet.com/docs/workers#list-workers"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The worker ID."
    foreign-key-id: "worker-id"

  - name: "timeLastModified"
    type: "date-time"
    replication-key: true
    description: "The time the worker was last modified."

  - name: "accountStatus"
    type: "string"
    description: "The worker's account status."

  - name: "activeTask"
    type: "string"
    description: "The ID of the worker's active task."
    foreign-key-id: "task-id"

  - name: "capacity"
    type: "number"
    description: "The maximum number of units the worker can carry."

  - name: "delayTime"
    type: "number"
    description: |
      The number of seconds the worker is delayed by, based on the `delayTime` of all assigned tasks or `null` if the worker isn't delayed. Refer to [{{ integration.display_name }}'s documentation](https://support.onfleet.com/hc/en-us/articles/204752505-Dashboard-statuses){:target="new"} for more info on task statuses and delay times.

  - name: "displayName"
    type: "string"
    description: "The worker's display name."

  - name: "imageUrl"
    type: "string"
    description: "The URL to the image for the worker."

  - name: "location"
    type: "string"
    description: ""

  - name: "metadata"
    type: "array"
    description: "Additional metadata bout the worker."
    subattributes:
      - name: "value"
        type: "anything"
        description: ""

  - name: "name"
    type: "string"
    description: "The worker's full name."

  - name: "onDuty"
    type: "boolean"
    description: "Indicates if the worker is on duty."

  - name: "organization"
    type: "string"
    description: "The ID of the organization the worker is a member of."
    foreign-key-id: "organization-id"

  - name: "phone"
    type: "string"
    description: "The worker's phone number."

  - name: "tasks"
    type: "array"
    description: "A list of IDs of tasks the user has been assigned."
    subattributes:
      - name: "value"
        type: "string"
        description: "The task ID."
        foreign-key-id: "task-id"

  - name: "teams"
    type: "array"
    description: "A list of IDs of the teams the worker belongs to."
    subattributes:
      - name: "value"
        type: "string"
        description: "The team ID."
        foreign-key-id: "team-id"

  - name: "timeCreated"
    type: "date-time"
    description: "The time the worker was created."

  - name: "timeLastSeen"
    type: "date-time"
    description: "The time the worker was last seen."

  - name: "userData"
    type: "object"
    description: "Details about the device and platform the worker is using to access the {{ integration.display_name }} app."
    subattributes:
      - name: "appVersion"
        type: "string"
        description: "The version of the {{ integration.display_name }} app the worker is using."

      - name: "batteryLevel"
        type: "number"
        description: "The battery level of the user's device."

      - name: "deviceDescription"
        type: "string"
        description: "A description of the device."

      - name: "platform"
        type: "string"
        description: "The platform the worker is using. For example: `IOS`"

  - name: "vehicle"
    type: "object"
    description: "Details about the worker's vehicle."
    subattributes:
      - name: "color"
        type: "string"
        description: "The color of the vehicle."

      - name: "description"
        type: "string"
        description: "The description of the vehicle."

      - name: "id"
        type: "string"
        description: "The vehicle ID."

      - name: "licensePlate"
        type: "string"
        description: "The vehicle's license plate number."

      - name: "timeLastModified"
        type: "date-time"
        description: "The time the vehicle was last modified."

      - name: "type"
        type: "string"
        description: |
          The vehicle's type. Possible values are:

          - `CAR`
          - `MOTORCYLE`
          - `BICYCLE`
          - `TRUCK`
---