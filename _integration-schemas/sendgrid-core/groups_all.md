---
tap: "sendgrid-core"

name: "groups_all"
doc-link: https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/groups.html#-GET
singer-schema: https://github.com/singer-io/tap-sendgrid/blob/master/tap_sendgrid/schemas/groups_all.json
description: |
  The `groups_all` table contains info about the groups in your SendGrid account. Groups are specific types of email you want your recipients to be able to unsubscribe from or subscribe to. For example: Newsletters, Invoices, Alerts, etc.

replication-method: "Full Table"

api-method:
  name: "List all suppression groups"
  doc-link: "https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/groups.html#-GET"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the suppression group."

  - name: "name"
    type: "string"
    description: "The name of the suppression group."

  - name: "description"
    type: "string"
    description: "A description of the suppression group."

  - name: "last_email_sent_at"
    type: "integer"
    description: "The Unix timestamp of when the suppression group was last emailed."

  - name: "is_default"
    type: "boolean"
    description: "If `true`, the suppression group is the default suppression group."

  - name: "unsubscribes"
    type: "integer"
    description: "The number of unsubscribes associated with the group."
---