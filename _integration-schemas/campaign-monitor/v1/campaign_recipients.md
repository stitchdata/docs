---
tap: "campaign-monitor"
version: "1.0"

name: "campaign_recipients"
doc-link: https://www.campaignmonitor.com/api/campaigns/#campaign-recipients
singer-schema: https://github.com/singer-io/tap-campaign-monitor/blob/master/tap_campaign_monitor/schemas/campaign_recipients.json
description: |
  The `{{ table.name }}` table contains info about the subscribers that a campaign was sent to.

replication-method: "Key-based Incremental"

api-method:
  name: "Get campaign recipients"
  doc-link: "https://www.campaignmonitor.com/api/campaigns/#campaign-recipients"

attributes:
  - name: "CampaignID"
    type: "string"
    primary-key: true
    description: "The campaign ID."
    foreign-key-id: "campaign-id"

  - name: "EmailAddress"
    type: "string"
    primary-key: true
    description: "The email address."

  - name: "ListID"
    type: "string"
    primary-key: true
    description: "The list ID."
    foreign-key-id: "list-id"
---