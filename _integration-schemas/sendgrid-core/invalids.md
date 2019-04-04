---
tap: "sendgrid-core"
version: "1.0"

name: "invalids"
doc-link: 
singer-schema: https://github.com/singer-io/tap-sendgrid/blob/master/tap_sendgrid/schemas/invalids.json
description: |
  The `{{ table.name }}` table contains info about invalid email addresses. An invalid email occurs when you attempt to send an email to an address that is formatted in a manner that doesn't meet internet email format standards, or the email doesn't exist at the recipient's email server.

  For example: Email addresses that don't include the `@` symbol.

replication-method: "Key-based Incremental"

replication-key:
  name: "end_time"

api-method:
  name: "List all invalid emails"
  doc-link: "https://sendgrid.com/docs/API_Reference/Web_API_v3/invalid_emails.html#List-all-invalid-emails-GET"

attributes:
  - name: "email"
    type: "string"
    primary-key: true
    description: "The email address marked as invalid."
    foreign-key-id: "email-id"

  - name: "created"
    type: "integer"
    description: "The Unix timestamp of when the email address was added to the invalid emails list."

  - name: "reason"
    type: "string"
    description: "The reason the email address was marked as invalid. For example: `Mail domain mentioned in email address is unknown`"
---