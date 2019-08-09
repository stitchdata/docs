---
tap: "netsuite"
version: "1.0"

name: "ContactCategory"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/contactcategory.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/ContactCategory.json"
description: |
  The `{{ table.name }}` table contains info about the types of contacts in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "contact-category"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "contact-category-id"

  - name: "_private"
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

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "sync"
    type: "boolean, string"
    description: ""
---