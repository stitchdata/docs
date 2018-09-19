---
tap: "listrak"
# version: ""

name: "message_reads"
doc-link:
singer-schema: https://github.com/singer-io/tap-listrak/blob/master/tap_listrak/schemas/message_reads.json
description: |
  The `message_reads` table contains info about contact reads for a message.

replication-method: "Full Table"

api-method:
  name: "ReportRangeMessageContactRead"
  doc-link: https://webservices.listrak.com/v31/IntegrationService.asmx?op=ReportRangeMessageContactRead

attributes:
  - name: "MsgID"
    type: "integer"
    primary-key: true
    description: "The ID of the message that was read."
    foreign-key-id: "contact-id"

  - name: "EmailAddress"
    type: "string"
    primary-key: true
    description: "The email address of the contact who read the message."

  - name: "ContactID"
    type: "string"
    description: "The ID of the contact who read the message."
    foreign-key-id: "contact-id"

  - name: "ReadDate"
    type: "string"
    description: "The date the contact read the message."
---