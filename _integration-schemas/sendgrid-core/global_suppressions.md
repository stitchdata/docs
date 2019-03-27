---
tap: "sendgrid-core"
version: "1.0"

name: "global_suppressions"
doc-link: https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/global_suppressions.html#-Global-Unsubscribes
singer-schema: https://github.com/singer-io/tap-sendgrid/blob/master/tap_sendgrid/schemas/global_suppressions.json
description: |
  The `{{ table.name }}` table contains info about global suppressions, or global unsubscribes. Recipients who are globally suppressed will be removed from any email you send.

replication-method: "Key-based Incremental"

replication-key:
  name: "end_time"

api-method:
  name: "List all globally unsubscribed email addresses"
  doc-link: "https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/global_suppressions.html#-Global-Unsubscribes"

attributes:
  - name: "email"
    type: "string"
    primary-key: true
    description: "The email address of the recipient who is globally suppressesd."
    foreign-key-id: "email-id"

  - name: "created"
    type: "integer"
    description: "The Unix timestamp of the time the recipient was added to the global suppression list."
---