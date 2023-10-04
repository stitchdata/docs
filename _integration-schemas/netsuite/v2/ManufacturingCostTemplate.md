---
tap: "netsuite"
version: "2"
name: ManufacturingCostTemplate
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ManufacturingCostTemplate.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/ManufacturingCostTemplate
description: |
  The `{{ table.name }}` table contains info about the manufacturing cost templates in your {{ integration.display_name }} account.

  A manufacturing cost template is a list of rates that can be associated with completing a specific operation. The template defines the activities that occur and related costs to be recorded each time this step is completed.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "manufacturing-cost-template"

replication-method: "Full Table"

attributes:
- name: nullFieldList
  type: varies
  description: ""
- name: name
  type: string
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: costDetailList
  type: varies
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: subsidiary
  type: varies
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
- name: memo
  type: string
  description: ""
---