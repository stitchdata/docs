---
tap: "campaign-monitor"
version: "1.0"

name: "campaign_email_client_usage"
doc-link: https://www.campaignmonitor.com/api/campaigns/#campaign-email-client-usage
singer-schema: https://github.com/singer-io/tap-campaign-monitor/blob/master/tap_campaign_monitor/schemas/campaign_email_client_usage.json
description: |
  The `{{ table.name }}` table contains info about the email clients subscribers use to open campaigns.

replication-method: "Full Table"

api-method:
  name: "Get email client usage"
  doc-link: "https://www.campaignmonitor.com/api/campaigns/#campaign-email-client-usage"

attributes:
  - name: "CampaignID"
    type: "string"
    primary-key: true
    description: "The campaign ID."
    foreign-key-id: "campaign-id"

  - name: "Client"
    type: "string"
    primary-key: true
    description: "The name of the email client."

  - name: "Version"
    type: "string"
    primary-key: true
    description: "The version of the email client."

  - name: "Percentage"
    type: "number"
    description: "The percentage of users who use the email client and version."

  - name: "Subscribers"
    type: "integer"
    description: "The number of subscribers who used the email client and version to open the campaign."
---