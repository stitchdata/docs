---
tap: "campaign-monitor"
# version: "1.0"

name: "campaign_spam_complaints"
doc-link: https://www.campaignmonitor.com/api/campaigns/#campaign-spam-complaints
singer-schema: https://github.com/singer-io/tap-campaign-monitor/blob/master/tap_campaign_monitor/schemas/campaign_spam_complaints.json
description: |
  The `{{ table.name }}` table contains info about subscribers who marked a campaign as spam.

replication-method: "Key-based Incremental"

api-method:
  name: "Get campaign spam complaints"
  doc-link: "https://www.campaignmonitor.com/api/campaigns/#campaign-spam-complaints"

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

  - name: "Date"
    type: "string"
    primary-key: true
    replication-key: true
    description: "The date."
---