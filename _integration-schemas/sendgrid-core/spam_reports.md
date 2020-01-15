---
tap: "sendgrid-core"
version: "1"

name: "spam_reports"
doc-link: 
singer-schema: https://github.com/singer-io/tap-sendgrid/blob/master/tap_sendgrid/schemas/spam_reports.json
description: |
  The `{{ table.name }}` table contains info about spam reports made against your messages. Spam reports occur when a recipient indicates they think your message is spam, which their email provider then reports to SendGrid.

replication-method: "Key-based Incremental"

replication-key:
  name: "end_time"

api-method:
  name: "List all spam reports"
  doc-link: "https://sendgrid.com/docs/API_Reference/Web_API_v3/spam_reports.html"

attributes:
  - name: "email"
    type: "string"
    primary-key: true
    description: "The email address of the recipient who marked the message as spam."
    foreign-key-id: "email-id"

  - name: "created"
    type: "integer"
    description: "The Unix timestamp of the time the spam report was made."

  - name: "status"
    type: "string"
    description: "The status of the spam report."
---