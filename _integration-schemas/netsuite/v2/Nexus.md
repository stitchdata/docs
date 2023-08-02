---
tap: "netsuite"
version: "2"
name: Nexus
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Nexus.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Nexus
description: |
  The `{{ table.name }}` table contains info about the tax jurisdictions - or nexus - in your {{ integration.display_name }} account. A nexus is a tax jurisdiction, usually defined at the country level. 

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "nexus"

replication-method: "Full Table"

attributes:
- name: description
  type: string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: taxAgencyPst
  type: varies
  description: ""
- name: parentNexus
  type: varies
  description: ""
- name: taxAgency
  type: varies
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: state
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: taxDateFromFulfillment
  type: boolean, string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: taxCode
  type: varies
  description: ""
- name: country
  type: varies
  description: ""
---