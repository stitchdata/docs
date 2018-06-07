---
tap: "listrak"
# version: ""

name: "subscribed_contacts"
doc-link:
singer-schema: https://github.com/singer-io/tap-listrak/blob/master/tap_listrak/schemas/subscribed_contacts.json
description: |
  The `subscribed_contacts` table contains info about contacts who are currently subscribed to the specified list.

replication-method: "Full Table"

api-method:
  name: "ReportRangeSubscribedContacts"
  doc-link: https://webservices.listrak.com/v31/IntegrationService.asmx?op=ReportRangeSubscribedContacts

attributes:
  - name: "AdditionDate"
    type: "string"
    description: ""

  - name: "EmailAddress"
    type: "string"
    description: ""

  - name: "AdditionMethod"
    type: "string"
    description: ""

  - name: "ContactID"
    type: "string"
    description: ""

  - name: "ListID"
    type: "integer"
    description: ""

Wrote out.md to the current directory!
