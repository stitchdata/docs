---
tap: "campaign-monitor"
# version: "1.0"

name: "list_bounced_subscribers"
doc-link: https://www.campaignmonitor.com/api/lists/#bounced-subscribers
singer-schema: https://github.com/singer-io/tap-campaign-monitor/blob/master/tap_campaign_monitor/schemas/list_bounced_subscribers.json
description: |
  The `{{ table.name }}` table contains info about the bounced subscribers for lists.

replication-method: "Key-based Incremental"

api-method:
  name: "Get list bounced subscribers"
  doc-link: "https://www.campaignmonitor.com/api/lists/#bounced-subscribers"

attributes:
  - name: "ListID"
    type: "string"
    primary-key: true
    description: "The list ID."
    foreign-key-id: "list-id"

  - name: "EmailAddress"
    type: "string"
    primary-key: true
    description: "The email address."

  - name: "Date"
    type: "string"
    primary-key: true
    replication-key: true
    description: "The date."

  - name: "Name"
    type: "string"
    description: "The name of the subscriber."

  - name: "State"
    type: "string"
    description: "The subscriber's state."

  - name: "CustomFields"
    type: "object"
    description: "Custom fields about the subscriber."
    subattributes: 
      - name: "Key"
        type: "string"
        description: "The key name of the custom field."

      - name: "Value"
        type: "string"
        description: "The value of the custom field."

  - name: "ReadsEmailWith"
    type: "string"
    description: "The email client the subscriber uses to read email."

  - name: "ConsentToTrack"
    type: "string"
    description: "Indicates if the subscriber has consented to tracking."
---