---
tap: "netsuite"
version: "1.0"

name: "TaxGroup"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/taxgroup.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/TaxGroup.json"
description: |
  The `{{ table.name }}` table contains info about the tax groups in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "tax-group"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "tax-group-id"

  - name: "city"
    type: "string"
    description: ""

  - name: "county"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "includeChildren"
    type: "boolean, string"
    description: ""

  - name: "isDefault"
    type: "boolean, string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "itemId"
    type: "string"
    description: ""

  - name: "nexusCountry"
    type: "varies"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "piggyback"
    type: "boolean, string"
    description: ""

  - name: "rate"
    type: "number, string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "subsidiaryList"
    type: "varies"
    description: ""

  - name: "taxItemList"
    type: "varies"
    description: ""

  - name: "taxType"
    type: "varies"
    description: ""

  - name: "taxitem1"
    type: "varies"
    description: ""

  - name: "taxitem2"
    type: "varies"
    description: ""

  - name: "unitprice1"
    type: "string"
    description: ""

  - name: "unitprice2"
    type: "string"
    description: ""

  - name: "zip"
    type: "string"
    description: ""
---