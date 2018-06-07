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
    description: ""

  - name: "ReadDate"
    type: "string"
    description: ""

  - name: "EmailAddress"
    type: "string"
    description: ""

  - name: "ContactID"
    type: "string"
    description: ""
