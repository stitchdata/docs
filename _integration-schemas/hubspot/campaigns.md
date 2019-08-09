---
tap: "hubspot"
version: "2.0"

name: "campaigns"
doc-link: http://developers.hubspot.com/docs/methods/email/get_campaign_data
singer-schema: https://github.com/singer-io/tap-hubspot/blob/master/tap_hubspot/schemas/campaigns.json
description: |
  The `{{ table.name }}` table contains info about the campaigns in your HubSpot account.

replication-method: "Full Table"
api-method:
  name: "Get campaign for particular campaign"
  doc-link: https://developers.hubspot.com/docs/methods/email/get_campaign_data

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the campaign."
    foreign-key-id: "campaign-id"

  - name: "appId"
    type: "integer"
    description: "The Application ID for the given email."

  - name: "appName"
    type: "string"
    description: "The Application Name for the given email."

  - name: "contentId"
    type: "integer"
    description: "The ID associated with the content."

  - name: "counters"
    type: "object"
    description: "Event count summaries for the given email."
    doc-link: https://developers.hubspot.com/docs/methods/email/email_events_overview
    subattributes:
      - name: "bounce"
        type: "integer"
        description: |
          The count of bounce events for the given email. A `bounce` event occurs when the recipient's email server could not or would not accept the message. No further attempts to deliver the message are made.

      - name: "deferred"
        type: "integer"
        description: |
          The count of deferred events for the given email. A `deferred` event occurs when the recipient's email server temporarily rejects the message. Additional attempts to deliver the message are made.

      - name: "dropped"
        type: "integer"
        description: |
          The count of dropped events for the given email. A `dropped` event occurs when the message is rejected, either by HubSpot or their delivery provider. No further attempts to deliver the message are made.

      - name: "delivered"
        type: "integer"
        description: |
          The count of delivered events for the given email. A `delivered` event occurs when the recipient's email server accepts the message and successfully delivers it to the recipient.

      - name: "mta_dropped"
        type: "integer"
        description: |
          The count of drop events (by delivery provider) for the given email.

      - name: "open"
        type: "integer"
        description: |
          The count of open events for the given email. An `open` event occurs when the recipient opens the message.

      - name: "processed"
        type: "integer"
        description: |
          The count of processed events for the given email. A `processed` event occurs when the message is received by HubSpot's delivery provider.

      - name: "sent"
        type: "integer"
        description: |
          The count of sent events for the given email. A `sent` event occurs when the message was sent to and received by HubSpot's delivery provider, and is queued for further handling.

      - name: "statuschange"
        type: "integer"
        description: |
          The count of status change events for the given email. A `statuschange` event occurs when the recipient changes their email subscription in some way.

      - name: "suppressed"
        type: "integer"
        description: |
          The count of suppression events for the given email.

      - name: "unsubscribed"
        type: "integer"
        description: "The count of unsubscribe events for the given email."

  - name: "name"
    type: "string"
    description: "The name of the email."

  - name: "numIncluded"
    type: "integer"
    description: "The number of included emails."

  - name: "numQueued"
    type: "integer"
    description: "The number of queued emails."

  - name: "subType"
    type: "string"
    description: "The subtype of the email. For example: `VariantB`"

  - name: "subject"
    type: "string"
    description: "The subject of the email."

  - name: "type"
    type: "string"
    description: "The type of the email. For example: `AB`"
---