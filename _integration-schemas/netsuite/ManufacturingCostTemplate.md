---
tap: "netsuite"
version: "1.0"

name: "ManufacturingCostTemplate"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/manufacturingcosttemplate.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/ManufacturingCostTemplate.json"
description: |
  The `{{ table.name }}` table contains info about the manufacturing cost templates in your {{ integration.display_name }} account.

  A manufacturing cost template is a list of rates that can be associated with completing a specific operation. The template defines the activities that occur and related costs to be recorded each time this step is completed.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "manufacturing-cost-template"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "manufacturing-cost-template-id"

  - name: "costDetailList"
    type: "varies"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "subsidiary"
    type: "varies"
    description: ""
---