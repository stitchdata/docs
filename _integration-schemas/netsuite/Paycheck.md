---
tap: "netsuite"
version: "1.0"

name: "Paycheck"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/paycheck.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Paycheck.json"
description: |
  The `{{ table.name }}` table contains info about the paycheck records in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "paycheck"

replication-method: "Key-based Incremental"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "paycheck-id"

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "_class"
    type: "varies"
    description: ""

  - name: "account"
    type: "varies"
    description: ""

  - name: "address"
    type: "string"
    description: ""

  - name: "balance"
    type: "number, string"
    description: ""

  - name: "batchNumber"
    type: "string"
    description: ""

  - name: "createdDate"
    type: "date-time"
    description: ""

  - name: "department"
    type: "varies"
    description: ""

  - name: "entity"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "location"
    type: "varies"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "payContribList"
    type: "varies"
    description: ""

  - name: "payDeductList"
    type: "varies"
    description: ""

  - name: "payDisburseList"
    type: "varies"
    description: ""

  - name: "payEarnList"
    type: "varies"
    description: ""

  - name: "payExpList"
    type: "varies"
    description: ""

  - name: "payFrequency"
    type: "string"
    description: ""

  - name: "payPtoList"
    type: "varies"
    description: ""

  - name: "paySummaryList"
    type: "varies"
    description: ""

  - name: "payTaxList"
    type: "varies"
    description: ""

  - name: "payTimeList"
    type: "varies"
    description: ""

  - name: "periodEnding"
    type: "date-time"
    description: ""

  - name: "postingPeriod"
    type: "varies"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "tranDate"
    type: "date-time"
    description: ""

  - name: "tranId"
    type: "string"
    description: ""

  - name: "userAmount"
    type: "number, string"
    description: ""

  - name: "workplace"
    type: "varies"
    description: ""
---