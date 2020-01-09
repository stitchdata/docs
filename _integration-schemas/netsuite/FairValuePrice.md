---
tap: "netsuite"
version: "1.0"

name: "FairValuePrice"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/fairvalueprice.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/FairValuePrice.json"
description: |
  The `{{ table.name }}` table contains info about the fair value price list in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "fair-value-price"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "fair-value-price-id"

  - name: "currency"
    type: "varies"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "dimensionList"
    type: "varies"
    description: ""

  - name: "endDate"
    type: "date-time"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "fairValue"
    type: "number, string"
    description: ""

  - name: "fairValueFormula"
    type: "varies"
    description: ""

  - name: "fairValueRangePolicy"
    type: "varies"
    description: ""

  - name: "highValue"
    type: "number, string"
    description: ""

  - name: "highValuePercent"
    type: "number, string"
    description: ""

  - name: "isVsoePrice"
    type: "boolean, string"
    description: ""

  - name: "item"
    type: "varies"
    description: ""

  - name: "itemRevenueCategory"
    type: "varies"
    description: ""

  - name: "lowValue"
    type: "number, string"
    description: ""

  - name: "lowValuePercent"
    type: "number, string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "startDate"
    type: "date-time"
    description: ""

  - name: "units"
    type: "varies"
    description: ""

  - name: "unitsType"
    type: "varies"
    description: ""
---