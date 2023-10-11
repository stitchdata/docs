---
tap: "stripe"
version: "2"
key: ""

name: "events"
doc-link: "https://stripe.com/docs/api/events"
singer-schema: https://github.com/singer-io/tap-stripe/tree/master/tap_stripe/schemas/events.json
description: |
  The `{{ table.name }}` table contains info about [events](https://stripe.com/docs/api/events){:target="new"}. When an  event occurs, a new event object is created. This table acts as the history of an object, allowing you to see how it has changed over time.

  For example: When an invoice is created, an `invoice.created` event is created. When the draft invoice is finalized and updated to be open, an `invoice.finalized` event is created. When the invoice is sent to the customer, an `invoice.sent` event is created.

  For more info about this table and how data is replicated, refer to the [Replication](#replication) section. Additionally, refer to [{{ integration.display_name }}'s documentation](https://stripe.com/docs/api/events/types){:target="new"} for info about event types and the objects they describe.

replication-method: "Key-based Incremental"

api-method:
    name: "List all events"
    doc-link: "https://stripe.com/docs/api/events/list"

attributes:
  - name: "id"
    type: "string"
    description: "The event ID."
    primary-key: true
    foreign-key-id: "event-id"

  - name: "created"
    type: "string"
    replication-key: true
    description: "The time at which the object was created. Measured in seconds since the Unix epoch."  

  - name: "api_version"
    type: "string"
    description: ""

  - name: "data"
    type: "object"
    description: ""

  - name: "livemode"
    type: "boolean"
    description: ""

  - name: "object"
    type: "string"
    description: ""

  - name: "pending_webhooks"
    type: "integer"
    description: ""

  - name: "request"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "updated"
    type: "string"
    description: ""
---