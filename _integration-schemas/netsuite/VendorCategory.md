---
tap: "netsuite"
version: "1"

name: "VendorCategory"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/vendorcategory.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/VendorCategory.json"
description: |
  The `{{ table.name }}` table contains info about the categories that can be applied to vendors in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "vendor-category"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "vendor-category-id"

  - name: "externalId"
    type: "string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "isTaxAgency"
    type: "boolean, string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""
---