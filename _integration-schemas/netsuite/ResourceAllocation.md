---
tap: "netsuite"
version: "1.0"

name: "ResourceAllocation"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/resourceallocation.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/ResourceAllocation.json"
description: |
  The `{{ table.name }}` table contains info about resource allocations, or employee time reservations, in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "resource-allocation"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "revenue-recognition-id"

  - name: "allocationAmount"
    type: "number, string"
    description: ""

  - name: "allocationResource"
    type: "varies"
    description: ""

  - name: "allocationType"
    type: "varies"
    description: ""

  - name: "allocationUnit"
    type: "varies"
    description: ""

  - name: "approvalStatus"
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

  - name: "externalId"
    type: "string"
    description: ""

  - name: "nextApprover"
    type: "varies"
    description: ""

  - name: "notes"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "numberHours"
    type: "number, string"
    description: ""

  - name: "percentOfTime"
    type: "number, string"
    description: ""

  - name: "project"
    type: "varies"
    description: ""

  - name: "requestedby"
    type: "varies"
    description: ""

  - name: "startDate"
    type: "date-time"
    description: ""
---