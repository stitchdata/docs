---
tap: "netsuite"
version: "1.0"

name: "Message"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/message.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Message.json"
description: |
  The `{{ table.name }}` table contains info about the messages in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "message"

replication-method: "Key-based Incremental"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "message-id"

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "activity"
    type: "varies"
    description: ""

  - name: "author"
    type: "varies"
    description: ""

  - name: "authorEmail"
    type: "string"
    description: ""

  - name: "bcc"
    type: "string"
    description: ""

  - name: "cc"
    type: "string"
    description: ""

  - name: "compressAttachments"
    type: "boolean, string"
    description: ""

  - name: "dateTime"
    type: "string"
    description: ""

  - name: "emailed"
    type: "boolean, string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "incoming"
    type: "boolean, string"
    description: ""

  - name: "mediaItemList"
    type: "varies"
    description: ""

  - name: "message"
    type: "string"
    description: ""

  - name: "messageDate"
    type: "date-time"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "recipient"
    type: "varies"
    description: ""

  - name: "recipientEmail"
    type: "string"
    description: ""

  - name: "recordName"
    type: "string"
    description: ""

  - name: "recordTypeName"
    type: "string"
    description: ""

  - name: "subject"
    type: "string"
    description: ""

  - name: "transaction"
    type: "varies"
    description: ""
---