---
tap: "netsuite"
version: "2"
name: BillingSchedule
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/BillingSchedule.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/BillingSchedule
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
attributes:
- name: milestoneList
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: monthDom
  type: string, integer
  description: ""
- name: recurrencePattern
  type: varies
  description: ""
- name: recurrenceDowMaskList
  type: varies
  description: ""
- name: scheduleType
  type: varies
  description: ""
- name: yearDowimMonth
  type: varies
  description: ""
- name: name
  type: string
  description: ""
- name: yearDow
  type: varies
  description: ""
- name: yearDom
  type: string, integer
  description: ""
- name: repeatEvery
  type: varies
  description: ""
- name: frequency
  type: varies
  description: ""
- name: monthMode
  type: varies
  description: ""
- name: billForActuals
  type: boolean, string
  description: ""
- name: yearMode
  type: varies
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: transaction
  type: varies
  description: ""
- name: recurrenceTerms
  type: varies
  description: ""
- name: isPublic
  type: boolean, string
  description: ""
- name: monthDowim
  type: varies
  description: ""
- name: yearMonth
  type: varies
  description: ""
- name: numberRemaining
  type: string, integer
  description: ""
- name: project
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: applyToSubtotal
  type: boolean, string
  description: ""
- name: recurrenceList
  type: varies
  description: ""
- name: dayPeriod
  type: string, integer
  description: ""
- name: monthDow
  type: varies
  description: ""
- name: yearDowim
  type: varies
  description: ""
- name: initialTerms
  type: varies
  description: ""
- name: initialAmount
  type: string
  description: ""
- name: inArrears
  type: boolean, string
  description: ""
- name: seriesStartDate
  type: string
  description: ""
---