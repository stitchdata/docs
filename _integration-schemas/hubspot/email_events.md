---
tap: "hubspot"
version: "2.0"

name: "email_events"
doc-link: https://developers.hubspot.com/docs/methods/email/email_events_overview
singer-schema: https://github.com/singer-io/tap-hubspot/blob/master/tap_hubspot/schemas/email_events.json
description: |
  The `email_events` table contains info about email events and how recipients interact with content.

notes: 

replication-method: "Key-based Incremental"
api-method:
  name: getEventsForCampaignOrRecipient
  doc-link: https://developers.hubspot.com/docs/methods/email/get_events

attributes:
## Primary & Replication Key
  - name: "id"
    type: "string"
    primary-key: true
    replication-key: true
    description: "The ID of the event."

  - name: "appId"
    type: "integer"
    description: "The ID of the HubSpot application that sent the email message."

  - name: "appName"
    type: "string"
    description: "The name of the HubSpot application that sent the email message."

  - name: "browser"
    type: "object"
    description: "Details about the browser that serviced the event."
    object-attributes:
      - name: "family"
        type: "string"
        description: "The family of the browser that serviced the event."

      - name: "name"
        type: "string"
        description: "The name of the browser that serviced the event."

      - name: "producer"
        type: "string"
        description: "The producer of the browser that serviced the event."

      - name: "producerUrl"
        type: "string"
        description: "The producer URL of the browser that serviced the event."

      - name: "type"
        type: "string"
        description: "The type of browser that serviced the event."

      - name: "url"
        type: "string"
        description: "The URL of the browser that serviced the event."

  - name: "created"
    type: "date-time"
    description: "The time the event was created."

  - name: "deviceType"
    type: "string"
    description: "The type of device used to service the event."

  - name: "duration"
    type: "integer"
    description: "The approximate number of milliseconds the user had opened the email message."

  - name: "emailCampaignId"
    type: "integer"
    description: "The ID of the email campaign that the email message is a part of."
    foreign-key: true
    table: "campaigns"

  - name: "emailCampaignGroupId"
    type: "integer"
    description: "The ID of the email campaign group associated with the email message."

  - name: "filteredEvent"
    type: "boolean"
    description: "Indicates if the event was filtered."

  - name: "from"
    type: "string"
    description: "The `from` field of the email message."

  - name: "hmid"
    type: "string"
    description: "An auto-generated ID that corresponds to the header `X-{{ integration.display_name }}-MID` in the email message."

  - name: "ipAddress"
    type: "string"
    description: "The IP address where the event originated."

  - name: "linkId"
    type: "integer"
    description: "The ID of the link the recipient clicked in the email message."

  - name: "location"
    type: "object"
    description: "Details about where the event occurred, including the city, state, and country."
    object-attributes:
      - name: "city"
        type: "string"
        description: "The city where the event occurred."

      - name: "country"
        type: "string"
        description: "The country where the event occurred."

      - name: "state"
        type: "string"
        description: "The state where the event occurred."

  - name: "portalId"
    type: "integer"
    description: "The ID of the {{ integration.display_name }} portal that sent the email message."

  - name: "recipient"
    type: "string"
    description: "The email address of the recipient of the email message."

  - name: "response"
    type: "string"
    description: "The full response from the recipient's email server."

  - name: "sentBy"
    type: "object"
    description: "Details about the email message's `SENT` event."
    object-attributes:
      - name: "created"
        type: "date-time"
        description: "The time the email message's `SENT` event occurred."

      - name: "id"
        type: "string"
        description: "The ID of the email message's `SENT` event."

  - name: "smtpId"
    type: "string"
    description: "The ID that {{ integration.display_name }} attaches to the email message."

  - name: "subject"
    type: "string"
    description: "The subject line of the email message."

  - name: "type"
    type: "string"
    description: "The type of event. Click the link in attribute's name for more details about email event types."
    doc-link: https://developers.hubspot.com/docs/methods/email/email_events_overview

  - name: "url"
    type: "string"
    description: "The URL in the email message that the recipient clicked."

  - name: "userAgent"
    type: "string"
    description: "The user agent responsible for the event."
---