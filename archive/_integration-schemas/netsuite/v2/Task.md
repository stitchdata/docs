---
tap: "netsuite"
version: "2"
name: Task
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Task.html
description: |
  The `{{ table.name }}` table contains info about the tasks in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "task"
replication-method: "Key-based Incremental"
table-key-properties: internalId
valid-replication-keys: lastModifiedDate
attributes:
- name: actualTime
  type: varies
  description: ""
- name: percentTimeComplete
  type: string, number
  description: ""
- name: accessLevel
  type: boolean, string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: reminderType
  type: varies
  description: ""
- name: parent
  type: varies
  description: ""
- name: timeItemList
  type: varies
  description: ""
- name: milestone
  type: varies
  description: ""
- name: estimatedTimeOverride
  type: varies
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
- name: assigned
  type: varies
  description: ""
- name: startDate
  type: string
  description: ""
- name: transaction
  type: varies
  description: ""
- name: lastModifiedDate
  type: string
  description: ""
  replication-key: true
- name: contactList
  type: varies
  description: ""
- name: title
  type: string
  description: ""
- name: endDate
  type: string
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
- name: percentComplete
  type: string, number
  description: ""
- name: customForm
  type: varies
  description: ""
- name: dueDate
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: createdDate
  type: string
  description: ""
- name: supportCase
  type: varies
  description: ""
- name: timeRemaining
  type: varies
  description: ""
- name: contact
  type: varies
  description: ""
- name: estimatedTime
  type: varies
  description: ""
- name: company
  type: varies
  description: ""
- name: owner
  type: varies
  description: ""
- name: timedEvent
  type: boolean, string
  description: ""
- name: completedDate
  type: string
  description: ""
- name: message
  type: string
  description: ""
---