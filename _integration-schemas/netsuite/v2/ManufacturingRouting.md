---
tap: "netsuite"
version: "2"
name: ManufacturingRouting
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ManufacturingRouting.html
description: |
  The `{{ table.name }}` table contains info about the manufacturing routing templates in your {{ integration.display_name }} account.

  A manufacturing routing is a template that contains a list of steps required to build an assembly item. Each step is in a sequential order necessary to complete the operational sequence for completing the assembly. After you have created a routing record, that routing can be selected on a work order to direct the completion of the assembly. The routing determines the work center, cost template, labor resources, and machine resources that will be used during the assembly.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "manufacturing-routing"

replication-method: "Full Table"

attributes:
- name: nullFieldList
  type: varies
  description: ""
- name: isDefault
  type: boolean, string
  description: ""
- name: name
  type: string
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: item
  type: varies
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: subsidiary
  type: varies
  description: ""
- name: autoCalculateLag
  type: boolean, string
  description: ""
- name: externalId
  type: string
  description: ""
- name: customForm
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: routingStepList
  type: varies
  description: ""
- name: routingComponentList
  type: varies
  description: ""
- name: billOfMaterials
  type: varies
  description: ""
- name: locationList
  type: varies
  description: ""
- name: memo
  type: string
  description: ""
---