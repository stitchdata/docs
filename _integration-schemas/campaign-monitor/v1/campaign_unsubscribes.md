---
tap: "campaign-monitor"
version: "1"

name: "campaign_unsubscribes"
doc-link: https://www.campaignmonitor.com/api/campaigns/#campaign-unsubscribes
singer-schema: https://github.com/fsinger-io/tap-campaign-monitor/blob/master/tap_campaign_monitor/schemas/campaign_unsubscribes.json
description: |
  The `{{ table.name }}` table contains info about the subscribers who unsubscribed from the email for a campaign.

replication-method: "Key-based Incremental"

api-method:
  name: "Get campaign unsubscribes"
  doc-link: "https://www.campaignmonitor.com/api/campaigns/#campaign-unsubscribes"

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

  - name: "IPAddress"
    type: "string"
    description: "The IP address."
---