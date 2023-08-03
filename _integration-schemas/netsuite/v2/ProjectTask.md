---
tap: "netsuite"
version: "2"
name: ProjectTask
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ProjectTask.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/ProjectTask
description: |
  The `{{ table.name }}` table contains info about the project tasks in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "project-task"

replication-method: "Key-based Incremental"
table-key-properties: internalId
valid-replication-keys: lastModifiedDate
attributes:
- name: percentTimeComplete
  type: string, number
  description: ""
- name: finishByDate
  type: string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: estimatedWork
  type: string, number
  description: ""
- name: parent
  type: varies
  description: ""
- name: predecessorList
  type: varies
  description: ""
- name: timeItemList
  type: varies
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: startDate
  type: string
  description: ""
- name: isMilestone
  type: boolean, string
  description: ""
- name: nonBillableTask
  type: boolean, string
  description: ""
- name: lateEnd
  type: string
  description: ""
- name: lateStart
  type: string
  description: ""
- name: title
  type: string
  description: ""
- name: isOnCriticalPath
  type: string
  description: ""
- name: plannedWork
  type: string, number
  description: ""
- name: eventId
  type: varies
  description: ""
- name: actualWork
  type: string, number
  description: ""
- name: endDate
  type: string
  description: ""
- name: estimatedWorkBaseline
  type: string, number
  description: ""
- name: priority
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: status
  type: varies
  description: ""
- name: endDateBaseline
  type: string
  description: ""
- name: customForm
  type: varies
  description: ""
- name: remainingWork
  type: string, number
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: plannedWorkBaseline
  type: string, number
  description: ""
- name: order
  type: varies
  description: ""
- name: startDateBaseline
  type: string
  description: ""
- name: slackMinutes
  type: string, number
  description: ""
- name: assigneeList
  type: varies
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
- name: constraintType
  type: varies
  description: ""
- name: message
  type: string
  description: ""
---