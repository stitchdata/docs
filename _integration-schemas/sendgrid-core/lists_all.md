---
tap: "sendgrid-core"
version: "1.0"

name: "lists_all"
doc-link: 
singer-schema: https://github.com/singer-io/tap-sendgrid/blob/master/tap_sendgrid/schemas/lists_all.json
description: |
  The `{{ table.name }}` table contains info about your recipient lists.

replication-method: "Full Table"

api-method:
  name: "List all lists"
  doc-link: "https://sendgrid.com/docs/API_Reference/Web_API_v3/Marketing_Campaigns/contactdb.html#List-All-Lists-GET"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The list ID."
    foreign-key-id: "list-id"

  - name: "name"
    type: "string"
    description: "The name of the list."

  - name: "recipient_count"
    type: "integer"
    description: "The current number of recipients currently in the list."
---