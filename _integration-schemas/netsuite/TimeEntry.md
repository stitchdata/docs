---
tap: "netsuite"
version: "1.0"

name: "TimeEntry"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/timeentry.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/TimeEntry.json"
description: |
  The `{{ table.name }}` table contains info about the time entries in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "time-entry"

replication-method: "Key-based Incremental"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "time-entry-id"

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "_class"
    type: "varies"
    description: ""

  - name: "approvalStatus"
    type: "varies"
    description: ""

  - name: "billingClass"
    type: "string"
    description: ""

  - name: "caseTaskEvent"
    type: "varies"
    description: ""

  - name: "createdDate"
    type: "date-time"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customer"
    type: "varies"
    description: ""

  - name: "department"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "hours"
    type: "varies"
    description: ""

  - name: "isBillable"
    type: "boolean, string"
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

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "overrideRate"
    type: "boolean, string"
    description: ""

  - name: "paidExternally"
    type: "boolean, string"
    description: ""

  - name: "payrollItem"
    type: "varies"
    description: ""

  - name: "price"
    type: "varies"
    description: ""

  - name: "rate"
    type: "number, string"
    description: ""

  - name: "subsidiary"
    type: "varies"
    description: ""

  - name: "timeType"
    type: "varies"
    description: ""
---