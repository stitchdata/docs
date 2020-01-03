---
tap: "listrak"
version: "1.0"

name: "message_opens"
doc-link:
singer-schema: https://github.com/singer-io/tap-listrak/blob/master/tap_listrak/schemas/message_opens.json
description: |
  The `{{ table.name }}` table contains info about contact opens for a message.

replication-method: "Full Table"

api-method:
  name: "ReportRangeMessageContactOpen"
  doc-link: https://webservices.listrak.com/v31/IntegrationService.asmx?op=ReportRangeMessageContactOpen

attributes:
  - name: "MsgID"
    type: "integer"
    primary-key: true
    description: "The ID of the message that was opened."
    foreign-key-id: "message-id"

  - name: "EmailAddress"
    type: "string"
    primary-key: true
    description: "The email address of the contact that opened the email."

  - name: "ContactID"
    type: "string"
    description: "The ID of the contact that opened the email."
    foreign-key-id: "contact-id"

  - name: "OpenDate"
    type: "string"
    description: "The date the contact opened the email."
---