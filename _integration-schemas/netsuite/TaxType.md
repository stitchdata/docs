---
tap: "netsuite"
version: "1.0"

name: "TaxType"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/taxtype.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/TaxType.json"
description: |
  The `{{ table.name }}` table contains info about the tax types in your {{ integration.display_name }} account. A tax type determines where the tax paid or collected is tracked on the balance sheet. The balance sheet account to which {{ integration.display_name }} posts the collection or payment of tax is called the tax control account.

  {{ integration.permission-for-table | flatify }}

permission:
  tab: "Lists"
  name: "Tax Groups"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "tax-type-id"

  - name: "country"
    type: "varies"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "doesNotAddToTotal"
    type: "boolean, string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nexusAccountsList"
    type: "varies"
    description: ""

  - name: "nexusesTaxList"
    type: "varies"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "postToItemCost"
    type: "boolean, string"
    description: ""

  - name: "reverseCharge"
    type: "boolean, string"
    description: ""

  - name: "taxInNetAmount"
    type: "boolean, string"
    description: ""
---