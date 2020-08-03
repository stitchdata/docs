---
tap: "pardot"
version: "1"
key: "email-click"

name: "email_clicks"
doc-link: "http://developer.pardot.com/kb/object-field-references/#email-clicks"
singer-schema: "https://github.com/singer-io/tap-pardot/blob/master/tap_pardot/schemas/email_clicks.json"
description: |
  The `{{ table.name }}` table contains info about email click events.

replication-method: "Key-based Incremental"

api-method:
  name: "Query email clicks"
  doc-link: "http://developer.pardot.com/kb/api-version-3/batch-email-clicks/"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The email click ID."
    foreign-key-id: "email-click-id"

  - name: "created_at"
    type: "date-time"
    replication-key: true
    description: "The time that the email click occurred."

  - name: "drip_program_action_id"
    type: "integer"
    description: "The ID for the drip program action associated with the email click."

  - name: "email_template_id"
    type: "integer"
    description: "The ID for the email template associated with the email click."
    foreign-key-id: "email-template-id"

  - name: "list_email_id"
    type: "integer"
    description: "The ID for the list email associated with the email click."
    foreign-key-id: "list-email-id"

  - name: "prospect_id"
    type: "integer"
    description: "The ID of the prospect associated with the email click."
    foreign-key-id: "prospect-id"

  - name: "tracker_redirect_id"
    type: "integer"
    description: "The ID of the tracker redirect associated with the email click."

  - name: "url"
    type: "string"
    description: "The URL of the email click."
---
