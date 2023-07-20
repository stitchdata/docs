---
tap: "netsuite"
version: "1"

name: "CustomList"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/customlist.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/CustomList.json"
description: |
  The `{{ table.name }}` table contains info about 

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "custom-list"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "custom-list-id"

  - name: "convertToCustomRecord"
    type: "boolean, string"
    description: ""

  - name: "customValueList"
    type: "varies"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "isMatrixOption"
    type: "boolean, string"
    description: ""

  - name: "isOrdered"
    type: "boolean, string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "owner"
    type: "varies"
    description: ""

  - name: "scriptId"
    type: "string"
    description: ""

  - name: "translationsList"
    type: "varies"
    description: ""
---