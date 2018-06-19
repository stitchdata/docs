---
tap: "sendgrid-core"

name: "bounces"
doc-link: https://sendgrid.com/docs/API_Reference/Web_API_v3/bounces.html#List-all-bounces-GET
singer-schema: https://github.com/singer-io/tap-sendgrid/blob/master/tap_sendgrid/schemas/bounces.json
description: |
  The `bounces` table contains info about bounced emails. A bounced email is when the message is undeliverable and returned to the server that sent it.

replication-method: "Key-based Incremental"

replication-key:
  name: "end_time"

api-method:
  name: "List all bounces"
  doc-link: "https://sendgrid.com/docs/API_Reference/Web_API_v3/bounces.html#List-all-bounces-GET"

attributes:
  - name: "email"
    type: "string"
    primary-key: true
    description: "The email address that bounced."

  - name: "created"
    type: "integer"
    description: "The Unix timestamp of the time the bounce occurred."

  - name: "reason"
    type: "string"
    description: "An explanation for the reason the email bounced."

  - name: "status"
    type: "string"
    description: "The status of the bounce."
---