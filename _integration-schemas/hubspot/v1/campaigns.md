---
tap: "hubspot"
version: "1.0"

name: "campaigns"
doc-link: http://developers.hubspot.com/docs/methods/email/get_campaign_data
singer-schema: https://github.com/singer-io/tap-hubspot/blob/master/tap_hubspot/schemas/campaigns.json
description: |
  The `campaigns` table contains info about the campaigns in your HubSpot account.

notes: 

replication-method: "Full Table"
api-method:
  name: getCampaignForParticularCampaign
  doc-link: https://developers.hubspot.com/docs/methods/email/get_campaign_data

attributes:
## Primary Key
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the campaign."

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
    object-attributes:
      - name: "delivered"
        type: "integer"
        description: "The count of delivered events for the given email."

      - name: "open"
        type: "integer"
        description: "The count of open events for the given email."

      - name: "processed"
        type: "integer"
        description: "The count of processed events for the given email."

      - name: "sent"
        type: "integer"
        description: "The count of sent events for the given email."

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