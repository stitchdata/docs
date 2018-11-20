---
tap: "stripe"
version: "1.0"

name: "events"
doc-link: "https://stripe.com/docs/api/events"
singer-schema: "https://github.com/singer-io/tap-stripe/blob/master/tap_stripe/schemas/events.json"
description: |
  The `{{ table.name }}` table contains info about [events](https://stripe.com/docs/api/events){:target="new"}. When an interesting event occurs, a new event object is created.

  For example: When a charge succeeds a `charge.succeeded` event is created; or, when an invoice can't be paid, an `invoice.payment_failed` event is created.

replication-method: "Key-based Incremental"

api-method:
    name: ""
    doc-link: ""

attributes:
  # - name: "api_version"
  #   type: "string"
  #   description: ""

  - name: "id"
    type: "string"
    description: "The event ID."
    foreign-key-id: "event-id"

  - name: "created"
    type: "date-time"
    description: "The time at which the object was created. Measured in seconds since the Unix epoch."

  - name: "data"
    type: ""
    description: |
      This object contains details about the event, relevant to the event's `type`.

      For example: For an `invoice.created` event, this will be a full [invoice object](#invoices). Refer to the object's dedicated table (ex: [`invoices`](#invoices)) for a list of possible attributes.

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