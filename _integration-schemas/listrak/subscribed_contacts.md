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
  - name: "ContactID"
    type: "string"
    primary-key: true
    description: "The ID of the contact."
    foreign-key-id: "contact-id"

  - name: "ListID"
    type: "integer"
    primary-key: true
    description: "The ID of the list the contact is subscribed to."
    foreign-key-id: "list-id"

  - name: "AdditionDate"
    type: "string"
    description: "The date the contact was added to the list."

  - name: "AdditionMethod"
    type: "string"
    description: "The method used to add the contact to the list."

  - name: "EmailAddress"
    type: "string"
    description: "The email address associated with the contact."
---