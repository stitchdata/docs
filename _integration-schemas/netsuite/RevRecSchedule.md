---
tap: "netsuite"
version: "1"

name: "RevRecSchedule"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/revrecschedule.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/RevRecSchedule.json"
description: |
  The `{{ table.name }}` table contains info about the revenue recognition schedules in your {{ integration.display_name }} account. A revenue recognition schedule indicates the posting periods in which revenue should be recognized, and the amount to be recognized in each period, for an item sale.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "rev-rec-schedule"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "revenue-recognition-schedule-id"

  - name: "amortizationPeriod"
    type: "integer, string"
    description: ""

  - name: "amortizationType"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "initialAmount"
    type: "number, string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "periodOffset"
    type: "integer, string"
    description: ""

  - name: "recogIntervalSrc"
    type: "varies"
    description: ""

  - name: "recurrenceList"
    type: "varies"
    description: ""

  - name: "recurrenceType"
    type: "varies"
    description: ""

  - name: "revRecOffset"
    type: "integer, string"
    description: ""
---