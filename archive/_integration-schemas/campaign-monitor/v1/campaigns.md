---
tap: "campaign-monitor"
version: "1"

name: "campaigns"
doc-link: https://www.campaignmonitor.com/api/campaigns/
singer-schema: https://github.com/singer-io/tap-campaign-monitor/blob/master/tap_campaign_monitor/schemas/campaigns.json
description: |
   The `{{ table.name }}` table contains info about the the campaigns in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

attributes:
  - name: "CampaignID"
    type: "string"
    primary-key: true
    description: "The campaign ID."
    foreign-key-id: "campaign-id"

  - name: "FromName"
    type: "string"
    description: "The campaign's from name."

  - name: "FromEmail"
    type: "string"
    description: "The email address campaign emails are sent from."

  - name: "ReplyTo"
    type: "string"
    description: "The email address that replies to the campaign will be sent to."

  - name: "WebVersionURL"
    type: "string"
    description: "The campaign's web version URL."

  - name: "WebVersionTextURL"
    type: "string"
    description: "The campaign's web version text URL."

  - name: "Subject"
    type: "string"
    description: "The subject of the campaign."

  - name: "Name"
    type: "string"
    description: "The name of the campaign."

  - name: "SentDate"
    type: "string"
    description: "The date the campaign was sent."

  - name: "TotalRecipients"
    type: "number"
    description: "The total number of subscribers who received the campaign."
---