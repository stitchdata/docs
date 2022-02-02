---
tap: "hubspot"
version: "2"
key: "subscription-change"

name: "subscription_changes"
doc-link: https://developers.hubspot.com/docs/methods/timeline/timeline-overview
singer-schema: https://github.com/singer-io/tap-hubspot/blob/master/tap_hubspot/schemas/subscription_changes.json
description: |
  The `{{ table.name }}` table contains info about changes made subscriptions.

replication-method: "Key-based Incremental"
replication-key:
  name: "startTimestamp"

api-method:
  name: "Get subscriptions timeline"
  doc-link: https://developers.hubspot.com/docs/methods/email/get_subscriptions_timeline

attributes:
  - name: "recipient"
    type: "string"
    primary-key: true
    description: "The contact associated with the subscription change event."
    # foreign-key-id: ""

  - name: "portalId"
    type: "integer"
    primary-key: true
    description: "The ID of the portal associated with the subscription change event."
    foreign-key-id: "portal-id"

  - name: "timestamp"
    type: "date-time"
    primary-key: true
    description: "The time that the subscription change event occurred."

  - name: "changes"
    type: "array"
    description: "Details about the subscription change event."
    subattributes:
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
        foreign-key-id: "portal-id"

      - name: "subscriptionId"
        type: "integer"
        description: "If applicable, the ID of the subscription involved in the change event."
        # foreign-key-id: "subscription-id"

      - name: "changeType"
        type: "string"
        description: "The type of change. Ex: `SUBSCRIPTION_STATUS`"

      - name: "causedByEvent"
        type: "object"
        description: "Details about the event that caused the change."
        subattributes:
          - name: "id"
            type: "string"
            description: "The ID of the event that caused the change."

          - name: "created"
            type: "date-time"
            description: "The time that the event that caused the change occurred."
---