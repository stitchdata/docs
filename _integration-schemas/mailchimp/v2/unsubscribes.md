---
tap: "mailchimp"
version: "1"

key: "unsubscribe"
name: "unsubscribes"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-mailchimp/blob/master/tap_mailchimp/schemas/unsubscribes.json"
description: |
  The `{{ table.name }}` table contains info about members who have unsubscribed from a specific campaign.

replication-method: "Full Table"

api-method:
    name: "Get unsubscribed list members"
    doc-link: "https://developer.mailchimp.com/documentation/mailchimp/reference/reports/unsubscribed/#read-get_reports_campaign_id_unsubscribed"

attributes:
  - name: "campaign_id"
    type: "string"
    primary-key: true
    description: "The campaign ID."
    foreign-key-id: "campaign-id"

  - name: "email_id"
    type: "string"
    primary-key: true
    description: "The MD5 hash of the lowercase version of the list member’s email address."

  - name: "email_address"
    type: "string"
    description: "Email address for a subscriber."

  - name: "list_id"
    type: "string"
    description: "The list ID."
    foreign-key-id: "list-id"

  - name: "list_is_active"
    type: "boolean"
    description: "The status of the list used, namely if it’s deleted or disabled."

  - name: "merge_fields"
    type: "anything"
    description: "An individual merge var and value for a member."

  - name: "reason"
    type: "string"
    description: "If available, the reason listed by the member for unsubscribing."

  - name: "timestamp"
    type: "date-time"
    description: "The date and time the member opted-out in ISO 8601 format."

  - name: "vip"
    type: "boolean"
    description: "The VIP status for the subscriber."
    doc-link: "https://mailchimp.com/help/designate-and-send-to-vip-contacts/?_ga=2.138092912.1967669071.1563545438-786188311.1561484332"
---