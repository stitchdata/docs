---
tap: "netsuite"
version: "2"
name: CalendarEvent
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/CalendarEvent.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/CalendarEvent
description: ""
replication-method: "Key-based Incremental"
table-key-properties: internalId
valid-replication-keys: lastModifiedDate
attributes:
- name: accessLevel
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: attendeeList
  type: varies
  description: ""
- name: reminderType
  type: varies
  description: ""
- name: recurrenceDowMaskList
  type: varies
  description: ""
- name: noEndDate
  type: boolean, string
  description: ""
- name: timeItemList
  type: varies
  description: ""
- name: endByDate
  type: string
  description: ""
- name: reminderMinutes
  type: varies
  description: ""
- name: sendEmail
  type: boolean, string
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: frequency
  type: varies
  description: ""
- name: startDate
  type: string
  description: ""
- name: resourceList
  type: varies
  description: ""
- name: transaction
  type: varies
  description: ""
- name: lastModifiedDate
  type: string
  description: ""
  replication-key: true
- name: exclusionDateList
  type: varies
  description: ""
- name: title
  type: string
  description: ""
- name: allDayEvent
  type: boolean, string
  description: ""
- name: endDate
  type: string
  description: ""
- name: externalId
  type: string
  description: ""
- name: status
  type: varies
  description: ""
- name: customForm
  type: varies
  description: ""
- name: recurrenceDowim
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: recurrence
  type: string
  description: ""
- name: createdDate
  type: string
  description: ""
- name: period
  type: string, integer
  description: ""
- name: supportCase
  type: varies
  description: ""
- name: location
  type: string
  description: ""
- name: contact
  type: varies
  description: ""
- name: company
  type: varies
  description: ""
- name: owner
  type: varies
  description: ""
- name: recurrenceDow
  type: varies
  description: ""
- name: organizer
  type: varies
  description: ""
- name: timedEvent
  type: boolean, string
  description: ""
- name: message
  type: string
  description: ""
- name: seriesStartDate
  type: string
  description: ""
---