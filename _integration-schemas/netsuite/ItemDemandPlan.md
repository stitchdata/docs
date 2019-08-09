---
tap: "netsuite"
version: "1.0"

name: "ItemDemandPlan"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/itemdemandplan.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/ItemDemandPlan.json"
description: |
  The `{{ table.name }}` table contains info about item demand plans in your {{ integration.display_name }} account. An item demand plan transaction stores the quantity expected to be needed, during specified time periods, for an item.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "item-demand-plan"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "item-demand-plan-id"

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "demandPlanCalendarType"
    type: "varies"
    description: ""

  - name: "demandPlanMatrix"
    type: "varies"
    description: ""

  - name: "endDate"
    type: "date-time"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "item"
    type: "varies"
    description: ""

  - name: "location"
    type: "varies"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "month"
    type: "varies"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "startDate"
    type: "date-time"
    description: ""

  - name: "subsidiary"
    type: "varies"
    description: ""

  - name: "units"
    type: "varies"
    description: ""

  - name: "year"
    type: "integer, string"
    description: ""
---