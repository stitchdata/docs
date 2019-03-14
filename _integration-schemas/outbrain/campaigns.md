---
tap: "outbrain"


name: "campaigns"
doc-link: http://docs.amplifyv01.apiary.io/#reference/campaigns
singer-schema: https://github.com/singer-io/tap-outbrain/blob/master/tap_outbrain/schemas.py#L86
description: |
  The `campaigns` table contains info about your Outbrain campaigns.

replication-method: "Full Table"
api-method:
  name: listAllCampaignsAssociatedWithAMarketer
  doc-link: http://docs.amplifyv01.apiary.io/#reference/campaigns/campaigns-collection-via-marketer/list-all-campaigns-associated-with-a-marketer

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The campaign ID."

  - name: "name"
    type: "string"
    description: "The name of the campaign."

  - name: "campaignOnAir"
    type: "boolean"
    description: "Indicates if the campaign is on air."

  - name: "onAirReason"
    type: "string"
    description: "The reason for the campaign's on air status."

  - name: "enabled"
    type: "boolean"
    description: "Indicates if the campaign is enabled."

  - name: "budget"
    type: "object"
    description: "Details about the budget associated with the campaign."
    subattributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The budget ID."

      - name: "name"
        type: "string"
        description: "The name of the budget."

      - name: "shared"
        type: "boolean"
        description: "Indicates if the budget is shared between campaigns."

      - name: "amount"
        type: "number"
        description: "The monetary amount of the budget."

      - name: "currency"
        type: "string"
        description: "The currency denomination applied to the budget."

      - name: "amountRemaining"
        type: "number"
        description: "The unspent monetary amount remaining on the budget."

      - name: "amountSpent"
        type: "number"
        description: "The spent monetary amount of the budget."

      - name: "creationTime"
        type: "date-time"
        description: "The time when the budget was created."

      - name: "lastModified"
        type: "date-time"
        description: "The time the budget was last updated."

      - name: "startDate"
        type: "date"
        description: "The date the budget is scheduled to begin spending."

      - name: "endDate"
        type: "date"
        description: "The date the budget is scheduled to stop spending. If the `runForever` attribute is true, this attribute will not be present for the budget."

      - name: "runForever"
        type: "boolean"
        description: "Indicates if the budget has an end date. If `true`, the `endDate` attribute will not be present for the budget."

      - name: "type"
        type: "string"
        description: "Indicates the period on which the budget refreshes. Ex: `monthly`"

      - name: "pacing"
        type: "string"
        description: "Indicates how fast the budget will be spent. Ex: `automatic`"

      - name: "dailyTarget"
        type: "number"
        description: "The maximum amount of spend that is allowed per day."

      - name: "maximumAmount"
        type: "number"
        description: "The maximum amount allowed, if defined."

  - name: "cpc"
    type: "number"
    description: "The cost per monetized user action. For example: cost per click."
---
