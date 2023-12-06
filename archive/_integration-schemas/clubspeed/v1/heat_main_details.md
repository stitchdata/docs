---
tap: "clubspeed"
version: "1"

name: "heat_main_details"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/heat_main_details.json"
description: |
  The `{{ table.name }}` table contains info about customers that were entered into finished heats.

replication-method: "Key-based Incremental"

replication-key:
  name: "heat_main.finish"

attributes:
  - name: "heatId"
    type: "integer"
    primary-key: true
    description: "The heat ID."
    foreign-key-id: "heat-id"

  - name: "customerId"
    type: "integer"
    primary-key: true
    description: "The customer ID."
    foreign-key-id: "customer-id"

  - name: "autoNo"
    type: "integer"
    description: "The kart number for the customer. **Note**: This is not assigned until during/after the heat."

  - name: "finishPosition"
    type: "integer"
    description: "The finish position for the customer."

  - name: "firstTime"
    type: "boolean"
    description: "Indicates whether or not this is the customer's first race."

  - name: "groupFinishPosition"
    type: "integer"
    description: "The finish position of the customer relative to their group."

  - name: "groupId"
    type: "integer"
    description: "The ID of the group the racer belongs to."

  - name: "lineUpPosition"
    type: "integer"
    description: "The line up position scheduled for the customer."

  - name: "pointHistoryId"
    type: "integer"
    description: "The ID of the point history utilized to add this customer to the heat."

  - name: "positionEditedDate"
    type: "date-time"
    description: "The timestamp at which the position was edited."

  - name: "proskill"
    type: "integer"
    description: "The proskill of the customer."

  - name: "proskillDiff"
    type: "integer"
    description: "The amount at which the proskill of the customer changed as an outcome of the heat."

  - name: "scores"
    type: "number"
    description: ""

  - name: "timeAdded"
    type: "date-time"
    description: "The time at which the customer was added to the heat."

  - name: "userId"
    type: "integer"
    description: "The ID of the user that added the customer to the heat."
    foreign-key-id: "user-id"
---