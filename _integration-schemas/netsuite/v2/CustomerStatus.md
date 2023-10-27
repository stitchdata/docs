---
tap: "netsuite"
version: "2"
name: CustomerStatus
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/CustomerStatus.html
description: |
  The `{{ table.name }}` table contains info about the stages for leads, prospects, and customers in your {{ integration.display_name }} sales cycle.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "customer-status"

replication-method: "Full Table"

attributes:
- name: description
  type: string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: stage
  type: varies
  description: ""
- name: name
  type: string
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: probability
  type: string, number
  description: ""
- name: externalId
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: includeInLeadReports
  type: boolean, string
  description: ""
---