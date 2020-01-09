---
tap: "netsuite"
version: "1.0"

name: "PriceLevel"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/pricelevel.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/PriceLevel.json"
description: |
  The `{{ table.name }}` table contains info about the price level list in your {{ integration.display_name }} account. Price level defines a list of values that are used by opportunity and item records to set the price level for a specific item.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "price-level"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "price-level-id"

  - name: "discountpct"
    type: "number, string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "isOnline"
    type: "boolean, string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "updateExistingPrices"
    type: "boolean, string"
    description: ""
---