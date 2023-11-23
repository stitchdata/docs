---
tap: "campaign-monitor"
version: "1"

name: "campaign_clicks"
doc-link: https://www.campaignmonitor.com/api/campaigns/#campaign-clicks
singer-schema: https://github.com/singer-io/tap-campaign-monitor/blob/master/tap_campaign_monitor/schemas/campaign_clicks.json
description: |
  The `{{ table.name }}` table contains info about subscribers who clicked a link in a given campaign.

replication-method: "Key-based Incremental"

api-method:
  name: "Get campaign clicks"
  doc-link: "https://www.campaignmonitor.com/api/campaigns/#campaign-clicks"

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
    description: "The date the click occurred."

  - name: "URL"
    type: "string"
    description: "The URL that was clicked."

  - name: "IPAddress"
    type: "string"
    description: "The IP address."

  - name: "Latitude"
    type: "number"
    description: "The latitude."

  - name: "Longitude"
    type: "number"
    description: "The longitude."

  - name: "City"
    type: "string"
    description: "The city."

  - name: "Region"
    type: "string"
    description: "The region."

  - name: "CountryCode"
    type: "string"
    description: "The country code."

  - name: "CountryName"
    type: "string"
    description: "The country name."
---