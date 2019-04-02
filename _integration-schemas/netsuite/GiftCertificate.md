---
tap: "netsuite"
# version: "1.0"

name: "GiftCertificate"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/GiftCertificate.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
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

  - name: "internalId"
    type: "string"
    description: ""

  - name: "lastModifiedDate"
    type: "date-time"
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
