---
tap: "netsuite"
version: "1.0"

name: "Bin"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/bin.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Bin.json"
description: |
  The `{{ table.name }}` table contains info about bins, or places in your warehouse where you store inventory items.

  {{ integration.permission-for-table | flatify }}

permission:
  tab: "Lists"
  name: "Bins"

feature-requirements:
  - tab: "Items & Inventory"
    name: "Bin Management"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "bin-id"

  - name: "binNumber"
    type: "string"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "location"
    type: "varies"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""
---