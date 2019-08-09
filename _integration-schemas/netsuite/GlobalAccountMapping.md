---
tap: "netsuite"
version: "1.0"

name: "GlobalAccountMapping"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/globalaccountmapping.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/GlobalAccountMapping.json"
description: |
  The `{{ table.name }}` table contains the global account mapping record details in your {{ integration.display_name }} account. 

  For {{ integration.display_name }} accounts using Multi-Book Accounting, the global account mapping record enables you to configure secondary accounting books to post to accounts different from the primary book. These mappings are used by transactions where the user can manually select the account to which the transaction posts.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "global-account-mapping"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "global-account-mapping-id"

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