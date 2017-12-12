---
tap: "hubspot"
version: "01-03-2017"

name: "subscription_changes"
doc-link: https://developers.hubspot.com/docs/methods/timeline/timeline-overview
singer-schema: https://github.com/singer-io/tap-hubspot/blob/v0.11.0/tap_hubspot/schemas/subscription_changes.json
description: |
  The `subscription_changes` table contains info about changes made subscriptions.

replication-method: "Incremental"
api-method:
  name: getSubscriptionsTimeline
  doc-link: https://developers.hubspot.com/docs/methods/email/get_subscriptions_timeline

attributes:
## Primary Key
  - name: "recipient"
    type: "string"
    primary-key: true
    description: "The contact associated with the subscription change event."

## Primary Key
  - name: "portalId"
    type: "integer"
    primary-key: true
    description: "The ID of the portal associated with the subscription change event."

## Primary & Replication Key
  - name: "timestamp"
    type: "date-time"
    primary-key: true
    replication-key: true
    description: "The time that the subscription change event occurred."

  - name: "changes"
    type: "array"
    description: "Details about the subscription change event."
    array-attributes:
      - name: "change"
        type: "string"
        description: "The action associated with the change. Ex: `SUBSCRIBED`"

      - name: "timestamp"
        type: "date-time"
        description: "The time that this particular event occurred."

      - name: "source"
        type: "string"
        description: "The source of the change. Ex: `SOURCE_RECIPIENT`"

      - name: "portalId"
        type: "integer"
        description: "The ID of the portal associated with the change event."

      - name: "subscriptionId"
        type: "integer"
        description: "If applicable, the ID of the subscription involved in the change event."

      - name: "changeType"
        type: "string"
        description: "The type of change. Ex: `SUBSCRIPTION_STATUS`"

      - name: "causedByEvent"
        type: "object"
        description: "Details about the event that caused the change."
        object-attributes:
          - name: "id"
            type: "string"
            description: "The ID of the event that caused the change."

          - name: "created"
            type: "date-time"
            description: "The time that the event that caused the change occurred."
---