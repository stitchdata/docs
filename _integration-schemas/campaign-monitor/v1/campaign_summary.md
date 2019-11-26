---
tap: "campaign-monitor"
version: "1.0"

name: "campaign_summary"
doc-link: https://www.campaignmonitor.com/api/campaigns/#campaign-summary
singer-schema: https://github.com/singer-io/tap-campaign-monitor/blob/master/tap_campaign_monitor/schemas/campaign_summary.json
description: |
  The `{{ table.name }}` table contains summary info about sent campaigns.

replication-method: "Full Table"

api-method:
  name: "Get campaign summary"
  doc-link: "https://www.campaignmonitor.com/api/campaigns/#campaign-summary"

attributes:
  - name: "CampaignID"
    type: "string"
    primary-key: true
    description: "The campaign ID."
    foreign-key-id: "campaign-id"

  - name: "Recipients"
    type: "integer"
    description: "The number of campaign recipients."

  - name: "TotalOpened"
    type: "integer"
    description: "The total number of opens for the campaign."

  - name: "Clicks"
    type: "integer"
    description: "The total number of clicks for the campaign."

  - name: "Unsubscribed"
    type: "integer"
    description: "The total number of unsubscribes for the campaign."

  - name: "Bounced"
    type: "integer"
    description: "The total number of bounces for the campaign."

  - name: "UniqueOpened"
    type: "integer"
    description: "The unique number of opens for the campaign."

  - name: "SpamComplaints"
    type: "integer"
    description: "The number of spam complaints for the campaign."

  - name: "WebVersionURL"
    type: "string"
    description: "The campaign's web version URL."

  - name: "WebVersionTextURL"
    type: "string"
    description: "The campaign's web version text URL."

  - name: "WorldviewURL"
    type: "string"
    description: "The campaign's public Worldview URL."

  - name: "Forwards"
    type: "integer"
    description: "The number of forwards for the campaign."

  - name: "Likes"
    type: "integer"
    description: "The number of likes for the campaign."

  - name: "Mentions"
    type: "integer"
    description: "The number of mentions for the campaign."
---