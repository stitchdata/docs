---
tap: "netsuite"
version: "1.0"

name: "GiftCertificate"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/giftcertificate.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/GiftCertificate.json"
description: |
  The `{{ table.name }}` table contains info about the gift certificates in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "gift-certificate"

replication-method: "Key-based Incremental"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "gift-certificate-id"

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "amountRemaining"
    type: "number, string"
    description: ""

  - name: "createdDate"
    type: "date-time"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "expirationDate"
    type: "date-time"
    description: ""

  - name: "giftCertCode"
    type: "string"
    description: ""

  - name: "message"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "originalAmount"
    type: "number, string"
    description: ""

  - name: "sender"
    type: "string"
    description: ""
---