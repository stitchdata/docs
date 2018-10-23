---
tap: "campaign-monitor"
# version: "1.0"

name: "lists"
doc-link: https://www.campaignmonitor.com/api/lists/
singer-schema: https://github.com/singer-io/tap-campaign-monitor/blob/master/tap_campaign_monitor/schemas/lists.json
description: |
  The `{{ table.name }}` table contains info about the lists in your {{ integration.display_name }} account.

replication-method: "Full Table"

attributes:
  - name: "ListID"
    type: "string"
    primary-key: true
    description: "The list ID."

  - name: "Name"
    type: "string"
    description: "The name of the list."
---