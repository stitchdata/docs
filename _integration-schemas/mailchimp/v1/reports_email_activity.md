---
tap: "mailchimp"
version: "1.0"

key: "report-email-activity"
name: "reports_email_activity"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-mailchimp/blob/master/tap_mailchimp/schemas/reports_email_activity.json"
description: |
  The `{{ table.name }}` table contains info about a member's subscriber activity in a specific campaign.

replication-method: ""

api-method:
    name: ""
    doc-link: "https://developer.mailchimp.com/documentation/mailchimp/guides/how-to-use-batch-operations/"

attributes:
  - name: "action"
    type: "string"
    primary-key: true
    description: |
      The action performed on the email. Possible values are:

      - `open`
      - `click`
      - `bounce`

  - name: "campaign_id"
    type: "string"
    primary-key: true
    description: "The campaign ID."
    foreign-key-id: "campaign-id"

  - name: "email_id"
    type: "string"
    primary-key: true
    description: "The MD5 hash of the lowercase version of the list member’s email address."

  - name: "timestamp"
    type: "date-time"
    primary-key: true
    description: "The date and time recorded for the action in ISO 8601 format."

  - name: "email_address"
    type: "string"
    description: "Email address for a subscriber."

  - name: "ip"
    type: "string"
    description: "The IP address recorded for the action."

  - name: "list_id"
    type: "string"
    description: "The list ID."
    foreign-key-id: "list-id"

  - name: "list_is_active"
    type: "boolean"
    description: ""

  - name: "type"
    type: "string"
    description: |
      **Applicable to `bounce` actions only**. The type of bounce received. Possible values are:

      - `hard`
      - `soft`

  - name: "url"
    type: "string"
    description: |
      **Applicable to `click` actions only**. The URL on which the member clicked.
---