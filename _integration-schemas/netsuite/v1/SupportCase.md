---
tap: "netsuite"
version: "1"

name: "SupportCase"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/supportcase.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/SupportCase.json"
description: |
  The `{{ table.name }}` table contains info about the support cases in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "support-case"

replication-method: "Key-based Incremental"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "support-case-id"

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "assigned"
    type: "varies"
    description: ""

  - name: "caseNumber"
    type: "string"
    description: ""

  - name: "category"
    type: "varies"
    description: ""

  - name: "company"
    type: "varies"
    description: ""

  - name: "contact"
    type: "varies"
    description: ""

  - name: "createdDate"
    type: "date-time"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "emailEmployeesList"
    type: "varies"
    description: ""

  - name: "emailForm"
    type: "boolean, string"
    description: ""

  - name: "endDate"
    type: "date-time"
    description: ""

  - name: "escalateToList"
    type: "varies"
    description: ""

  - name: "escalationMessage"
    type: "string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "helpDesk"
    type: "boolean, string"
    description: ""

  - name: "inboundEmail"
    type: "string"
    description: ""

  - name: "incomingMessage"
    type: "string"
    description: ""

  - name: "insertSolution"
    type: "varies"
    description: ""

  - name: "internalOnly"
    type: "boolean, string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "issue"
    type: "varies"
    description: ""

  - name: "item"
    type: "varies"
    description: ""

  - name: "lastMessageDate"
    type: "date-time"
    description: ""

  - name: "lastModifiedDate"
    type: "date-time"
    description: ""

  - name: "lastReopenedDate"
    type: "date-time"
    description: ""

  - name: "module"
    type: "varies"
    description: ""

  - name: "newSolutionFromMsg"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "origin"
    type: "varies"
    description: ""

  - name: "outgoingMessage"
    type: "string"
    description: ""

  - name: "phone"
    type: "string"
    description: ""

  - name: "priority"
    type: "varies"
    description: ""

  - name: "product"
    type: "varies"
    description: ""

  - name: "profile"
    type: "varies"
    description: ""

  - name: "searchSolution"
    type: "string"
    description: ""

  - name: "serialNumber"
    type: "varies"
    description: ""

  - name: "solutionsList"
    type: "varies"
    description: ""

  - name: "startDate"
    type: "date-time"
    description: ""

  - name: "status"
    type: "varies"
    description: ""

  - name: "subsidiary"
    type: "varies"
    description: ""

  - name: "timeItemList"
    type: "varies"
    description: ""

  - name: "title"
    type: "string"
    description: ""
---