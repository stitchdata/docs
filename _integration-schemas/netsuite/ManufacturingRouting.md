---
tap: "netsuite"
version: "1"

name: "ManufacturingRouting"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/manufacturingrouting.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/ManufacturingRouting.json"
description: |
  The `{{ table.name }}` table contains info about the manufacturing routing templates in your {{ integration.display_name }} account.

  A manufacturing routing is a template that contains a list of steps required to build an assembly item. Each step is in a sequential order necessary to complete the operational sequence for completing the assembly. After you have created a routing record, that routing can be selected on a work order to direct the completion of the assembly. The routing determines the work center, cost template, labor resources, and machine resources that will be used during the assembly.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "manufacturing-routing"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "manufacturing-routing-id"

  - name: "autoCalculateLag"
    type: "boolean, string"
    description: ""

  - name: "billOfMaterials"
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

  - name: "isDefault"
    type: "boolean, string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "item"
    type: "varies"
    description: ""

  - name: "locationList"
    type: "varies"
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

  - name: "routingComponentList"
    type: "varies"
    description: ""

  - name: "routingStepList"
    type: "varies"
    description: ""

  - name: "subsidiary"
    type: "varies"
    description: ""
---