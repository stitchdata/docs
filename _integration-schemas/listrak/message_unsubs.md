# version: ""

name: "message_unsubs"
doc-link:
singer-schema: https://github.com/singer-io/tap-listrak/blob/master/tap_listrak/schemas/message_unsubs.json
description: |
  The `message_unsubs` table contains info about contacts who requested to be removed from a list from the supplied message.

replication-method: "Full Table"

api-method:
  name: "ReportRangeMessageContactRemoval"
  doc-link: https://webservices.listrak.com/v31/IntegrationService.asmx?op=ReportRangeMessageContactRemoval

attributes:
  - name: "MsgID"
    type: "integer"
    description: ""

  - name: "ContactID"
    type: "string"
    description: ""

  - name: "EmailAddress"
    type: "string"
    description: ""

  - name: "AdditionDate"
    type: "string"
    description: ""

  - name: "RemovalDate"
    type: "string"
    description: ""

  - name: "RemovalMethod"
    type: "string"
    description: ""

Wrote out.md to the current directory!
