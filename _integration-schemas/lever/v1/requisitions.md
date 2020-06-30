---
tap: "lever"
version: "1"
key: "requisition"

name: "requisitions"
doc-link: "https://hire.lever.co/developer/documentation#requisitions"
singer-schema: "https://github.com/singer-io/tap-lever/blob/master/tap_lever/schemas/requisitions.json"
description: |
  The `{{ table.name }}` table contains info about requisitions in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "List all requisitions"
  doc-link: "https://hire.lever.co/developer/documentation#list-all-requisitions"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The requisition ID."
    foreign-key-id: "requisition-id"

  - name: "createdAt"
    type: "date-time"
    replication-key: true
    description: "The datetime when the requisition was created."

  - name: "backfill"
    type: "boolean"
    description: "If `true`, the requisition represents a backfill. If `false`, the requisition hasn't been specified or represents a new headcount."

  - name: "compensationBand"
    type: "object"
    description: "Details about the compensation band associated with the requisition band."
    subattributes:
      - name: "currency"
        type: "string"
        description: "The ISO currency code associated with the requisition's compensation band."

      - name: "interval"
        type: "string"
        description: "The interval of payment for the compensation band."

      - name: "min"
        type: "integer"
        description: "The low-bound number for the compensation band."

      - name: "max"
        type: "integer"
        description: "The high-bound number for the compensation band."

  - name: "creator"
    type: "string"
    description: "The user ID of the requisition's creator."
    foreign-key-id: "user-id"

  - name: "customFields"
    type: "object"
    description: "The custom fields associated with the requisition."
    subattributes:

  - name: "department"
    type: "string"
    description: ""

  - name: "employmentStatus"
    type: "string"
    description: |
      The work type of the requisition. Possible values are:

      - `full-time`
      - `part-time`
      - `intern`
      - `contractor`
      - `temp-worker`

  - name: "headcountHired"
    type: "integer"
    description: "The number of filled seats or openings on the requisition."

  - name: "headcountTotal"
    type: "string"
    description: "The total headcount alloted for this requisition."

  - name: "hiringManager"
    type: "string"
    description: "The user ID of the hiring manager for this requisition."
    foreign-key-id: "user-id"

  - name: "internalNotes"
    type: "string"
    description: "Details about the requisition."

  - name: "location"
    type: "string"
    description: "The location associated with the requisition."

  - name: "name"
    type: "string"
    description: "The name of the requisition."

  - name: "offerIds"
    type: "array"
    description: "A list of offer IDs associated with the requisition."
    subattributes:
      - name: "value"
        type: "string"
        description: "The offer ID."
        foreign-key-id: "offer-id"

  - name: "owner"
    type: "string"
    description: "The user ID of the requisition's owner."
    foreign-key-id: "user-id"

  - name: "postings"
    type: "array"
    description: "A list of posting IDs associated with the requisition."
    subattributes:
      - name: "value"
        type: "string"
        description: "The posting ID."
        foreign-key-id: "posting-id"

  - name: "requisitionCode"
    type: "string"
    description: "The unique HRIS code for the requisition."

  - name: "status"
    type: "string"
    description: |
      The status of the requisition. Possible values are:

      - `open`
      - `onHold`
      - `closed`
      - `draft`

  - name: "team"
    type: "string"
    description: "The team associated with the requisition."
---