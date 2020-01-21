---
tap: "netsuite"
version: "1"

name: "PhoneCall"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/payrollitem.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/PhoneCall.json"
description: |
  The `{{ table.name }}` table contains info about the phone call records in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "phone-call"

replication-method: "Key-based Incremental"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "phone-call-id"

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "accessLevel"
    type: "boolean, string"
    description: ""

  - name: "assigned"
    type: "varies"
    description: ""

  - name: "company"
    type: "varies"
    description: ""

  - name: "completedDate"
    type: "date-time"
    description: ""

  - name: "contact"
    type: "varies"
    description: ""

  - name: "contactList"
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

  - name: "endDate"
    type: "date-time"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "message"
    type: "string"
    description: ""

  - name: "milestone"
    type: "varies"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "owner"
    type: "varies"
    description: ""

  - name: "phone"
    type: "string"
    description: ""

  - name: "priority"
    type: "varies"
    description: ""

  - name: "reminderMinutes"
    type: "varies"
    description: ""

  - name: "reminderType"
    type: "varies"
    description: ""

  - name: "sendEmail"
    type: "boolean, string"
    description: ""

  - name: "startDate"
    type: "date-time"
    description: ""

  - name: "status"
    type: "varies"
    description: ""

  - name: "supportCase"
    type: "varies"
    description: ""

  - name: "timeItemList"
    type: "varies"
    description: ""

  - name: "timedEvent"
    type: "boolean, string"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "transaction"
    type: "varies"
    description: ""
---