---
tap: "netsuite"
version: "1.0"

name: "UnitsType"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/unitstype.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/UnitsType.json"
description: |
  The `{{ table.name }}` table contains info about the unit types, or Units of Measure, in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

permission:
  tab: "Lists"
  name: "Units"

feature-requirements:
  - tab: "Company"
    name: &uom "Multiple Units of Measure"
  - tab: "Accounting"
    name: *uom

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "unit-type-id"

  - name: "externalId"
    type: "string"
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

  - name: "uomList"
    type: "varies"
    description: ""
---