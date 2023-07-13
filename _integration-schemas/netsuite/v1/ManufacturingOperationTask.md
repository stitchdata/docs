---
tap: "netsuite"
version: "1"

name: "ManufacturingOperationTask"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/manufacturingoperationtask.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/ManufacturingOperationTask.json"
description: |
  The `{{ table.name }}` table contains info about manufacturing operation tasks in your {{ integration.display_name }} account.

  After a WIP work order that has a designated routing is saved in {{ integration.display_name }}, manufacturing operation tasks are created based on the routing. Each of these tasks is a step that must be done in order for the assembly process to be finished.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "manufacturing-operation-task"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "manufacturing-operation-task-id"

  - name: "actualWork"
    type: "number, string"
    description: ""

  - name: "autoCalculateLag"
    type: "boolean, string"
    description: ""

  - name: "completedQuantity"
    type: "number, string"
    description: ""

  - name: "costDetailList"
    type: "varies"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "endDate"
    type: "date-time"
    description: ""

  - name: "estimatedWork"
    type: "number, string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "inputQuantity"
    type: "number, string"
    description: ""

  - name: "laborResources"
    type: "integer, string"
    description: ""

  - name: "machineResources"
    type: "integer, string"
    description: ""

  - name: "manufacturingCostTemplate"
    type: "varies"
    description: ""

  - name: "manufacturingWorkCenter"
    type: "varies"
    description: ""

  - name: "message"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "operationSequence"
    type: "integer, string"
    description: ""

  - name: "order"
    type: "varies"
    description: ""

  - name: "predecessorList"
    type: "varies"
    description: ""

  - name: "remainingWork"
    type: "number, string"
    description: ""

  - name: "runRate"
    type: "number, string"
    description: ""

  - name: "setupTime"
    type: "number, string"
    description: ""

  - name: "startDate"
    type: "date-time"
    description: ""

  - name: "status"
    type: "varies"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "workOrder"
    type: "varies"
    description: ""
---