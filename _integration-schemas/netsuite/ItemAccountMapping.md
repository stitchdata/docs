---
tap: "netsuite"
version: "1.0"

name: "ItemAccountMapping"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/itemaccountmapping.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/ItemAccountMapping.json"
description: |
  The `{{ table.name }}` table contains details about the item account mapping record in your {{ integration.display_name }} account.

  For accounts using {{ integration.display_name }} Multi-Book Accounting, the item account mapping record enables you to configure secondary accounting books to post to accounts different from the primary book, based on the item that is the subject of the transaction. These mappings are used by transactions where the item determines the account to which the transaction posts.

  {{ integration.permission-for-table | flatify }}

permission:
  tab: "Setup"
  name: "Item Account Mapping"

feature-requirements:
  - name: "NetSuite OneWorld"
  - tab: &accounting "Accounting"
    name: "Multi-Book Accounting"
  - tab: *accounting
    name: "Chart of Accounts Mapping"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "item-account-mapping-id"

  - name: "_class"
    type: "varies"
    description: ""

  - name: "accountingBook"
    type: "varies"
    description: ""

  - name: "customDimension"
    type: "varies"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "department"
    type: "varies"
    description: ""

  - name: "destinationAccount"
    type: "varies"
    description: ""

  - name: "effectiveDate"
    type: "date-time"
    description: ""

  - name: "endDate"
    type: "date-time"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "itemAccount"
    type: "varies"
    description: ""

  - name: "location"
    type: "varies"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "sourceAccount"
    type: "varies"
    description: ""

  - name: "subsidiary"
    type: "varies"
    description: ""
---