---
tap: "stripe"
version: "1"

name: "events"
doc-link: "https://stripe.com/docs/api/events"
singer-schema: "https://github.com/singer-io/tap-stripe/blob/master/tap_stripe/schemas/events.json"
description: |
  The `{{ table.name }}` table contains info about [events](https://stripe.com/docs/api/events){:target="new"}. When an  event occurs, a new event object is created. This table acts as the history of an object, allowing you to see how it has changed over time.

  For example: When an invoice is created, an `invoice.created` event is created. When the draft invoice is finalized and updated to be open, an `invoice.finalized` event is created. When the invoice is sent to the customer, an `invoice.sent` event is created.

  For more info about this table and how data is replicated, refer to the [Replication](#replication) section. Additionally, refer to [{{ integration.display_name }}'s documentation](https://stripe.com/docs/api/events/types){:target="new"} for info about event types and the objects they describe.

replication-method: "Key-based Incremental"

api-method:
    name: "List all events"
    doc-link: "https://stripe.com/docs/api/events/list"

attributes:
  # - name: "api_version"
  #   type: "string"
  #   description: ""

  - name: "id"
    type: "string"
    description: "The event ID."
    primary-key: true
    foreign-key-id: "event-id"

  - name: "created"
    type: "date-time"
    replication-key: true
    description: "The time at which the object was created. Measured in seconds since the Unix epoch."

  - name: "data"
    type: ""
    description: |
      This object contains details about the event, relevant to the event's `type`.

      For example: For an `invoice.*` event, this will be a full [invoice object](#invoices). Refer to the object's dedicated table (ex: [`invoices`](#invoices)) for a list of possible attributes.

      **Note**: To join specific events with the corresponding object record, this attribute must be set to replicate. It contains the object's `id`, which is necessary to join events to objects correctly.

  - name: "livemode"
    type: "boolean"
    description: "Indicates if the object exists in live mode (`true`) or in test mode (`false`)."

  - name: "object"
    type: "string"
    description: "The type of {{ integration.display_name }} object. This will be `event`."

  - name: "pending_webhooks"
    type: "integer"
    description: "The number of webhooks that have yet to be successfully delivered to the URLs you've specified."

  - name: "request"
    type: "string"
    description: "The info on the API request that triggered the event."

  - name: "type"
    type: "string"
    description: "The description of the event. For example: `invoice.created`"

  - name: "updated"
    type: "date-time"
    description: "The time at which the object was last updated."
---