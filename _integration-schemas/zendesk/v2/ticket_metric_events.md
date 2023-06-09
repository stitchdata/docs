---
tap: "zendesk"
version: "2"
key: ""

name: "ticket_metric_events"
doc-link: "https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_metric_events/"
singer-schema: https://github.com/singer-io/tap-zendesk/blob/master/tap_zendesk/schemas/ticket_metric_events.json
description: "This table contains data about reply times, agent work times, and requester wait times."

api-method:
    name: "TicketMetricEvents"
    doc-link: "https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_metric_events/"

replication-method: "Key-based Incremental"

table-key-properties: "id"
valid-replication-keys: "time"

attributes:
  - name: "deleted"
    type: "boolean"
    description: "Available if type is `breach`. In general, you can ignore any breach event when deleted is true."

  - name: "id"
    type: "integer"
    description: "Automatically assigned when the record is created"
    primary-key: true

  - name: "instance_id"
    type: "integer"
    description: "The instance of the metric associated with the event"

  - name: "metric"
    type: "string"
    description: "The metric being tracked. Allowed values are `agent_work_time`, `pausable_update_time`, `periodic_update_time`, `reply_time`, `requester_wait_time`, or `resolution_time`."

  - name: "sla"
    type: "object"
    description: "Available if type is `apply_sla`. The SLA policy and target being enforced on the ticket and metric in question"
    subattributes:
    - name: "target"
      type: "integer"
      description: ""

    - name: "business_hours"
      type: "boolean"
      description: ""

    - name: "policy"
      type: "object"
      description: ""
      subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "title"
        type: "string"
        description: ""

      - name: "description"
        type: "string"
        description: ""



  - name: "status"
    type: "object"
    description: "Available if type is `update_status`. Minutes since the metric has been open"
    subattributes:
    - name: "calendar"
      type: "integer"
      description: ""

    - name: "business"
      type: "integer"
      description: ""


  - name: "ticket_id"
    type: "integer"
    description: "Id of the associated ticket"

  - name: "time"
    type: "string"
    description: "The time the event occurred"
    replication-key: true

  - name: "type"
    type: "string"
    description: "The type of the metric event. Allowed values are `activate`, `pause`, `fulfill`, `apply_sla`, `breach`, `update_status`, or `measure`."
---