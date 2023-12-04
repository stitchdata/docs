---
tap: "sailthru"
version: "1"
key: ""

name: "purchase_log"
doc-link: "https://getstarted.sailthru.com/developers/api/job/#export-purchase-log"
singer-schema: "https://github.com/singer-io/tap-sailthru/blob/master/tap_sailthru/schemas/purchase_log.json"
description: |
  The `{{ table.name }}` table contains a a list of user data in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "get PurchaseLog"
    doc-link: "https://getstarted.sailthru.com/developers/api/job/#export-purchase-log"

attributes:
  - name: "channel"
    type: "string"
    primary-key: true
    description: "The channel."
    #foreign-key-id: "channel-id"

  - name: "email_hash"
    type: "string"
    primary-key: true
    description: "The email hash."
    #foreign-key-id: "email-hash-id"

  - name: "extid"
    type: "string"
    primary-key: true
    description: "The external ID."
    #foreign-key-id: "external-id" 

  - name: "message_id"
    type: "string"
    primary-key: true
    description: "The message ID."
    #foreign-key-id: "message-id"

  - name: "price"
    type: "string"
    primary-key: true
    description: "The price."

  - name: "date"
    type: "date-time"
    description: "The date list was created"
    replication-key: true
 
  - name: "items"
    type: "string"
    description: ""
  
  - name: "quantities"
    type: "string"
    description: ""
  - name: "unit_prices"
    type: "string"
    description: ""
  - name: "urls"
    type: "string"
    description: ""
---
