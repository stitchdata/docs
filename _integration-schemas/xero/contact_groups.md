---
tap: "xero"
version: "1.0"

name: "contact_groups"
doc-link: &api-doc https://developer.xero.com/documentation/api/contactgroups
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/contact_groups.json
description: |
  The `contact_groups` table contains info about your contact groups. A contact group is a group of contacts that have something in common.

  **Note**: Due to the limits of Xero's API, only active contact groups (`Status: ACTIVE`) may be retrieved.

replication-method: "Full Table"

api-method:
  name: getContactGroups
  doc-link: *api-doc

attributes:
  - name: "ContactGroupID"
    type: "string"
    primary-key: true
    description: "The contact group ID."

  - name: "Name"
    type: "string"
    description: "The name of the contact group."

  - name: "Status"
    type: "string"
    description: "The status of the contact group. This will always be `ACTIVE`."

  - name: "HasValidationErrors"
    type: "boolean"
    description: "If `true`, there are validation errors associated with the contact group."
---