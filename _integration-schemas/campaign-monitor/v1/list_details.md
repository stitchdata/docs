---
tap: "campaign-monitor"
version: "1.0"

name: "list_details"
doc-link: https://www.campaignmonitor.com/api/lists/#list-details
singer-schema: https://github.com/singer-io/tap-campaign-monitor/blob/master/tap_campaign_monitor/schemas/list_details.json
description: |
  The `{{ table.name }}` table contains summary info about lists in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get list details"
  doc-link: "https://www.campaignmonitor.com/api/lists/#list-details"

attributes:
  - name: "ListID"
    type: "string"
    primary-key: true
    description: "The list ID."
    foreign-key-id: "list-id"

  - name: "ConfirmedOptIn"
    type: "boolean"
    description: "If `true`, the list is a confirmed opt-in list."

  - name: "Title"
    type: "string"
    description: "The title of the list."

  - name: "UnsubscribePage"
    type: "string"
    description: "The URL of the list's unsubscribe page."

  - name: "UnsubscribeSetting"
    type: "string"
    description: "The list's unsubscribe setting."

  - name: "ConfirmationSuccessPage"
    type: "string"
    description: "The URL of the list's confirmation page."
---