---
tap: "listrak"
version: "1.0"

name: "message_sends"
doc-link:
singer-schema: https://github.com/singer-io/tap-listrak/blob/master/tap_listrak/schemas/message_sends.json
description: |
  The `{{ table.name }}` table contains `MsgID` and `EmailAddress` pairs, allowing you to identify the messages that your contacts have been sent.

replication-method: "Full Table"

api-method:
  name: "ReportMessageContactSent"
  doc-link: https://webservices.listrak.com/v31/IntegrationService.asmx?op=ReportMessageContactSent 

attributes:
  - name: "MsgID"
    type: "integer"
    primary-key: true
    description: "The ID of the message that was sent."
    foreign-key-id: "message-id"

  - name: "EmailAddress"
    type: "string"
    primary-key: true
    description: "The email address that the message was sent to."
---