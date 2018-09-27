---
tap: "campaign-monitor"
# version: "1.0"

name: "campaign_bounces"
doc-link: "https://www.campaignmonitor.com/api/campaigns/#campaign-bounces"
singer-schema: https://github.com/singer-io/tap-campaign-monitor/blob/master/tap_campaign_monitor/schemas/campaign_bounces.json
description: |
  The `{{ table.name }}` table contains info about the subscribers who bounced for a given campaign.

replication-method: "Key-based Incremental"

api-method:
  name: "Get campaign bounces"
  doc-link: "https://www.campaignmonitor.com/api/campaigns/#campaign-bounces"

attributes:
  - name: "CampaignID"
    type: "string"
    primary-key: true
    description: "The campaign ID."
    foreign-key-id: "campaign-id"

  - name: "EmailAddress"
    type: "string"
    primary-key: true
    description: "The email address of the subscriber who bounced."

  - name: "Date"
    type: "string"
    primary-key: true
    replication-key: true
    description: "The date the bounce occurred."

  - name: "ListID"
    type: "string"
    primary-key: true
    description: "The list ID."
    foreign-key-id: "list-id"

  - name: "BounceType"
    type: "string"
    description: |
      The type of bounce that occurred. Possible values are:

      - `Hard`
      - `Soft`

  - name: "Reason"
    type: "string"
    description: "The reason the bounce occurred. For example: `Invalid Email Address`"
---