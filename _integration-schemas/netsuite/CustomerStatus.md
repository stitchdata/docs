---
tap: "netsuite"
version: "1"

name: "CustomerStatus"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/customerstatus.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/CustomerStatus.json"
description: |
  The `{{ table.name }}` table contains info about the stages for leads, prospects, and customers in your {{ integration.display_name }} sales cycle.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "customer-status"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "customer-status-id"

  - name: "description"
    type: "string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "includeInLeadReports"
    type: "boolean, string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "probability"
    type: "number, string"
    description: ""

  - name: "stage"
    type: "varies"
    description: ""
---