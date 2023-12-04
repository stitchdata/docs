---
tap: "chargify"
version: "1"
key: "event"

name: "events"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-chargify/blob/master/tap_chargify/schemas/events.json"
description: |
  The `{{ table.name }}` table contains info about activity on your {{ integration.display_name }} site.

replication-method: "Full Table"

api-method:
  name: "List events for a site"
  doc-link: "https://reference.chargify.com/v1/events/list-events-for-a-site"
  
attributes:
  - name: "id"
    type: "number"
    primary-key: true
    description: "The event ID."
    foreign-key-id: "event-id"

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "event_specific_data"
    type: "object"
    description: ""
    subattributes:
      - name: "account_transaction_id"
        type: "number"
        description: ""
        foreign-key-id: "transaction-id"

      - name: "product_id"
        type: "number"
        description: ""
        foreign-key-id: "product-id"

  - name: "key"
    type: "string"
    description: ""

  - name: "message"
    type: "string"
    description: ""

  - name: "subscription_id"
    type: "number"
    description: "The ID of the subscription associated with the event."
    foreign-key-id: "subscription-id"
---