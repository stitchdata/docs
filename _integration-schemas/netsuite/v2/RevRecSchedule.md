---
tap: "netsuite"
version: "2"
name: RevRecSchedule
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/RevRecSchedule.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/RevRecSchedule
description: |
  The `{{ table.name }}` table contains info about the revenue recognition schedules in your {{ integration.display_name }} account. A revenue recognition schedule indicates the posting periods in which revenue should be recognized, and the amount to be recognized in each period, for an item sale.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "rev-rec-schedule"
replication-method: "Full Table"
table-key-properties: internalId

attributes:
- name: amortizationType
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: name
  type: string
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: revRecOffset
  type: string, integer
  description: ""
- name: externalId
  type: string
  description: ""
- name: recogIntervalSrc
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: recurrenceList
  type: varies
  description: ""
- name: amortizationPeriod
  type: string, integer
  description: ""
- name: periodOffset
  type: string, integer
  description: ""
- name: recurrenceType
  type: varies
  description: ""
- name: initialAmount
  type: string, number
  description: ""
---